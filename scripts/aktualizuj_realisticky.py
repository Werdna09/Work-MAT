#!/usr/bin/env python3
"""Sekvenční, obnovitelná lokální knihovna veřejné učebnice Matematika SŠ.

Použití: python3 scripts/aktualizuj_realisticky.py
         python3 scripts/aktualizuj_realisticky.py --offline
         python3 scripts/aktualizuj_realisticky.py --refresh-index --refresh-pdfs
Bez závislostí Pythonu; používá curl, pdfinfo a pdftotext. Viz KATALOG.md.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
import unicodedata
from urllib.parse import parse_qs, quote, unquote, urljoin, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / 'externi_zdroje/realisticky'
META = LIB / '.knihovna'
STATE = META / 'stav.json'
BASE = 'http://www.realisticky.cz/'
INDEX = BASE + 'ucebnice.php?id=2'
LICENSE = BASE + 'clanky.php?id=licence'
UA = 'MAT-LokalniKnihovna/1.0 (sekvencni archivace pro osobni studium)'
VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'base', 'area', 'source', 'wbr'}
PDFROOT = '/ucebnice/01 Matematika SŠ/'


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_') or 'Dokument'


def url(href, parent=BASE):
    p = urlsplit(urljoin(parent, href))
    if p.hostname not in ('realisticky.cz', 'www.realisticky.cz'):
        raise ValueError('Odkaz mimo Realisticky.cz: ' + href)
    path = re.sub('/+', '/', unquote(p.path))
    if any(x in ('.', '..') for x in path.split('/')):
        raise ValueError('Neplatná cesta: ' + href)
    return urlunsplit(('http', 'www.realisticky.cz', quote(path, safe="/()[],-_.~"), p.query, ''))


def page_kind(href):
    p = urlsplit(href)
    kind = {'dil.php': 'part', 'kapitola.php': 'chapter', 'hodina.php': 'lesson'}.get(p.path.rsplit('/', 1)[-1])
    key = parse_qs(p.query).get('id', [''])[0]
    return (kind, key) if kind and key.isdigit() else (None, None)


def atomic_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


class ContentLinks(HTMLParser):
    """Čte pouze hlavní obsah, nikoli navigaci, přihlášení či diskusi.

    Zachovává číslo řádku u odkazu i v historickém nevalidním HTML tabulek.
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.blocked = False
        self.cell = None
        self.number = None
        self.anchor = None
        self.links = []
        self.title = ''
        self.h2 = False
        self.base = BASE

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'base':
            self.base = a.get('href', BASE)
        if tag == 'div':
            if self.depth:
                self.depth += 1
            elif a.get('id') == 'content':
                self.depth = 1
            if self.depth and a.get('class', '').split()[:1] == ['comments']:
                self.blocked = True
        if not self.depth or self.blocked:
            return
        if tag == 'td' and 'id_objektu' in a.get('class', '').split():
            self.cell = ''
        if tag == 'a':
            self.anchor = {'href': a.get('href', ''), 'title': '', 'number': self.number}
        if tag == 'h2':
            self.h2 = True

    def handle_data(self, data):
        if not self.depth or self.blocked:
            return
        if self.cell is not None:
            self.cell += data
        if self.anchor is not None:
            self.anchor['title'] += data
        if self.h2:
            self.title += data

    def handle_endtag(self, tag):
        if self.depth and not self.blocked:
            if tag == 'td' and self.cell is not None:
                s = self.cell.strip()
                self.number = s if re.fullmatch(r'\d+', s) else None
                self.cell = None
            if tag == 'a' and self.anchor is not None:
                self.anchor['title'] = ' '.join(self.anchor['title'].split())
                self.links.append(self.anchor)
                self.anchor = None
            if tag == 'h2':
                self.h2 = False
        if tag == 'div' and self.depth:
            self.depth -= 1


def parse_page(html):
    p = ContentLinks()
    p.feed(html)
    if not p.title.strip():
        raise ValueError('Stránka neobsahuje očekávaný hlavní obsah')
    links = []
    for a in p.links:
        try:
            a['url'] = url(a['href'], p.base)
        except ValueError:
            continue
        links.append(a)
    return {'title': p.title.strip(), 'links': links}


def empty_state():
    return {'version': 1, 'parts': {}, 'chapters': {}, 'lessons': {}, 'documents': {},
            'pages': {}, 'moves': [], 'errors': {}, 'policies': {}}


def merge_page(s, parsed, source, context=None):
    context = dict(context or {})
    part = context.get('part')
    chapter = context.get('chapter')
    lesson = context.get('lesson')
    found = []
    # Replace occurrences from a refreshed page, preserving other source pages.
    for d in s['documents'].values():
        d['sources']=[c for c in d['sources'] if c['page']!=source]
    for a in parsed['links']:
        kind, key = page_kind(a['url'])
        num = a['number']
        if kind:
            coll = s[{'part': 'parts', 'chapter': 'chapters', 'lesson': 'lessons'}[kind]]
            # Breadcrumbs have no row number; use their already known identity.
            if key not in coll and num:
                rec = {'id': key, 'number': num, 'title': a['title'], 'url': a['url']}
                if kind == 'chapter': rec['part'] = part
                if kind == 'lesson': rec.update(part=part, chapter=chapter)
                coll[key] = rec
            if key in coll:
                coll[key]['active'] = True
                if kind == 'part': part, chapter, lesson = key, None, None
                if kind == 'chapter':
                    chapter, lesson = key, None
                    part = coll[key].get('part', part)
                if kind == 'lesson':
                    lesson = key
                    part = coll[key].get('part', part)
                    chapter = coll[key].get('chapter', chapter)
            continue
        path = unquote(urlsplit(a['url']).path)
        if not path.lower().endswith('.pdf'):
            continue
        rec = s['documents'].setdefault(a['url'], {'url': a['url'], 'sources': [], 'status': 'pending'})
        occurrence = {'page': source, 'part': part, 'chapter': chapter, 'lesson': lesson,
                      'label': a['title'], 'number': num}
        # The two global appendix tables follow the last lesson in the old HTML.
        # Their URL hierarchy, not that preceding lesson, determines placement.
        if path.startswith(PDFROOT+'99 Přílohy/'):
            group=path[len(PDFROOT+'99 Přílohy/'):].split('/')[0]
            groups=s.setdefault('appendix_groups',{})
            if group not in groups:groups[group]=len(groups)+1
            occurrence.update(part=None,chapter=None,lesson=None,section='appendix',
                              group=group,group_order=groups[group])
        elif path.startswith(PDFROOT+'00 Úvod/'):
            occurrence.update(part=None,chapter=None,lesson=None,section='intro')
        if occurrence not in rec['sources']:
            rec['sources'].append(occurrence)
        rec['active'] = True
        rec['seen_at'] = s['started_at']
        if source == INDEX or 'placement' not in rec:
            rec['placement'] = occurrence
        if a['href'] not in rec.setdefault('original_hrefs', []):
            rec['original_hrefs'].append(a['href'])
        found.append(a['url'])
    return found


def destination(s, doc):
    c = doc['placement']
    if c.get('section')=='appendix':
        basename=Path(unquote(urlsplit(doc['url']).path)).stem
        return Path('99_Prilohy')/f"{c.get('group_order',1):02d}_{slug(c['group'])}"/(slug(basename)+'.pdf')
    part = s['parts'].get(c.get('part'))
    chapter = s['chapters'].get(c.get('chapter'))
    lesson = s['lessons'].get(c.get('lesson'))
    # Introductory PDFs precede the numbered parts in the actual index.
    if not part:
        prefix = Path('00_Uvod')
    else:
        prefix = Path(f"{int(part['number']):02d}_{slug(part['title'])}")
        if chapter:
            prefix /= f"{int(chapter['number']):02d}_{slug(chapter['title'])}"
    basename = Path(unquote(urlsplit(doc['url']).path)).stem
    if lesson:
        ident = lesson['number'].zfill(6)
        prefix /= ident + '_' + slug(lesson['title'])
        label = c['label']
        name = ident + '_' + (slug(label) if label in ('Lekce', 'Příklady', 'Řešení') else slug(basename))
    else:
        name = slug(basename)
    return prefix / (name + '.pdf')


def validate_pdf(path):
    if not path.is_file() or path.stat().st_size < 40:
        raise ValueError('Prázdný či chybějící soubor')
    with path.open('rb') as f:
        if not f.read(1024).lstrip().startswith(b'%PDF-'):
            raise ValueError('Soubor nemá hlavičku PDF (může jít o HTML chybu)')
        f.seek(max(0, path.stat().st_size - 4096))
        if b'%%EOF' not in f.read():
            raise ValueError('Chybí závěrečný marker PDF')
    info = subprocess.run(['pdfinfo', str(path)], capture_output=True, timeout=60)
    out = info.stdout.decode('utf-8', 'replace')
    m = re.search(r'^Pages:\s*(\d+)', out, re.M)
    if info.returncode or not m or int(m[1]) < 1:
        raise ValueError('pdfinfo: ' + info.stderr.decode('utf-8', 'replace')[-400:])
    text = subprocess.run(['pdftotext', str(path), '/dev/null'], capture_output=True, timeout=90)
    if text.returncode:
        raise ValueError('pdftotext: ' + text.stderr.decode('utf-8', 'replace')[-400:])
    warnings = sorted(set((info.stderr + text.stderr).decode('utf-8', 'replace').splitlines()))
    return {'pages': int(m[1]), 'warnings': warnings, 'validated_at': now()}


class StopAccess(RuntimeError):
    pass


class Fetcher:
    def __init__(self, delay):
        self.delay = max(1.0, delay)
        self.last = 0.0
        self.robot = None
        self.requests = 0

    def get(self, address, output=None, conditional=None):
        if self.robot and not self.robot.can_fetch(UA, address):
            raise StopAccess('robots.txt zakazuje: ' + address)
        for attempt in range(3):
            wait = self.delay - (time.monotonic() - self.last)
            if wait > 0: time.sleep(wait)
            cmd = ['curl', '-fL', '-sS', '--globoff', '--connect-timeout', '15', '--max-time', '60',
                   '--proto', '=http,https', '--proto-redir', '=http,https',
                   '--user-agent', UA, '--write-out', '\n%{http_code}\n%{url_effective}']
            if conditional:
                for key, header in [('etag', 'If-None-Match'), ('last_modified', 'If-Modified-Since')]:
                    if conditional.get(key):cmd += ['-H', header + ': ' + conditional[key]]
            # Headers are kept only while processing the request; PDF bytes go straight
            # to their final directory, with a .part suffix until validation succeeds.
            headers = META / 'prenos.headers'
            cmd += ['--dump-header', str(headers)]
            if output: cmd += ['-o', str(output)]
            cmd += [address]
            self.last = time.monotonic()
            r = subprocess.run(cmd, capture_output=True)
            self.requests += 1
            chunks = r.stdout.rsplit(b'\n', 2)
            body = chunks[0] if len(chunks) == 3 else b''
            status = int(chunks[-2]) if len(chunks) == 3 and chunks[-2].isdigit() else 0
            effective = chunks[-1].decode('utf-8', 'replace')
            hs = headers.read_text(errors='replace') if headers.exists() else ''
            hdr = {}
            for line in hs.splitlines():
                if ':' in line:
                    k, v = line.split(':', 1);hdr[k.strip().lower()] = v.strip()
            headers.unlink(missing_ok=True)
            if status in (401, 403, 429):
                # Do not bypass authentication, a prohibition or rate limiting.
                raise StopAccess(f'HTTP {status}: {address}; stahování zastaveno')
            if r.returncode == 0 and status in (200, 304):
                url(effective)  # Reject a redirect to an unrelated host.
                return body, status, hdr
            if status in (404, 410):
                raise FileNotFoundError(f'HTTP {status}: {address}')
            if attempt < 2 and (status >= 500 or status == 0):
                time.sleep(3 * (attempt + 1));continue
            raise RuntimeError(f'HTTP {status}, curl {r.returncode}: ' + r.stderr.decode('utf-8', 'replace').strip()[-350:])
        raise RuntimeError('Přenos se nezdařil')


def save(s):
    s['saved_at'] = now()
    atomic_json(STATE, s)


def page(s, fetcher, address, refresh=False):
    rec = s['pages'].get(address, {})
    # Cached pages make interruption recovery inexpensive. Normal updates refresh
    # pages older than one day; --refresh-index forces a complete fresh traversal.
    age = time.time() - rec.get('fetched_epoch', 0)
    if not refresh and rec.get('parsed') and age < 86400:
        return rec['parsed']
    body, status, headers = fetcher.get(address)
    parsed = parse_page(body.decode('utf-8', 'replace'))
    s['pages'][address] = {'parsed': parsed, 'fetched_at': now(), 'fetched_epoch': time.time(),
                           'sha256': hashlib.sha256(body).hexdigest()}
    s['errors'].pop(address, None)
    save(s)
    return parsed


def policies(s, fetcher):
    try:
        body, _, _ = fetcher.get(BASE + 'robots.txt')
        robot = RobotFileParser();robot.set_url(BASE + 'robots.txt')
        robot.parse(body.decode('utf-8', 'replace').splitlines())
        fetcher.robot = robot
        wait = robot.crawl_delay(UA) or robot.crawl_delay('*')
        rate = robot.request_rate(UA) or robot.request_rate('*')
        if wait: fetcher.delay = max(fetcher.delay, wait)
        if rate: fetcher.delay = max(fetcher.delay, rate.seconds / rate.requests)
        s['policies']['robots'] = {'checked_at': now(), 'status': 200, 'text': body.decode('utf-8', 'replace')}
    except FileNotFoundError as e:
        s['policies']['robots'] = {'checked_at': now(), 'status': 404, 'note': str(e)}
    body, _, _ = fetcher.get(LICENSE)
    parsed = parse_page(body.decode('utf-8', 'replace'))
    raw = body.decode('utf-8', 'replace')
    if 'creativecommons.org/licenses/by-nc-nd/3.0/cz/' not in raw or 'Martin Krynický' not in raw:
        raise StopAccess('Licence se změnila nebo ji nelze ověřit; nejprve je nutná kontrola podmínek.')
    s['policies']['license'] = {'url': LICENSE, 'author': 'Martin Krynický',
                              'license': 'CC BY-NC-ND 3.0 Česko', 'checked_at': now()}
    save(s)


def discover(s, fetcher, refresh):
    for doc in s['documents'].values(): doc['active'] = False
    for coll in ('parts', 'chapters', 'lessons'):
        for rec in s[coll].values(): rec['active'] = False
    parsed = page(s, fetcher, INDEX, refresh=True)
    merge_page(s, parsed, INDEX)
    if len(s['parts']) < 1 or len(s['chapters']) < 1 or len(s['lessons']) < 1:
        raise RuntimeError('Prázdná struktura učebnice; stahování neprovádím')
    print(f"Index: {len(s['parts'])} dílů, {len(s['chapters'])} kapitol, {len(s['lessons'])} lekcí, {len(s['documents'])} URL PDF.", flush=True)
    # The index already expands all lessons. Still inspect each part, chapter and
    # lesson detail, so a separately linked appendix is not silently missed.
    visited = set()
    while True:
        todo = []
        for coll, role in [('parts', 'part'), ('chapters', 'chapter'), ('lessons', 'lesson')]:
            for key, rec in list(s[coll].items()):
                if not rec.get('active',True) or rec['url'] in visited: continue
                ctx = {role: key}
                if role != 'part': ctx['part'] = rec.get('part')
                if role == 'lesson': ctx['chapter'] = rec.get('chapter')
                todo.append((rec['url'], ctx))
        if not todo:break
        for address, ctx in todo:
            visited.add(address)
            try:
                parsed = page(s, fetcher, address, refresh=refresh)
                merge_page(s, parsed, address, ctx)
            except StopAccess:raise
            except (ValueError, RuntimeError, FileNotFoundError) as e:
                s['errors'][address] = str(e)
            if len(visited) % 25 == 0:
                save(s)
                print(f"Průzkum stránek: {len(visited)}/{len(s['parts'])+len(s['chapters'])+len(s['lessons'])}; PDF {sum(d.get('active',False) for d in s['documents'].values())}.", flush=True)
    ensure_directories(s)
    s['discovery_finished_at'] = now()
    save(s)


def ensure_directories(s):
    """I prázdná veřejná kapitola patří do ověřeného členění webu."""
    (LIB/'00_Uvod').mkdir(parents=True,exist_ok=True)
    for key,p in s['parts'].items():
        if not p.get('active',True):continue
        dest=LIB/f"{int(p['number']):02d}_{slug(p['title'])}"
        dest.mkdir(parents=True,exist_ok=True)
        for c in s['chapters'].values():
            if c.get('active',True) and c.get('part')==key:
                (dest/f"{int(c['number']):02d}_{slug(c['title'])}").mkdir(parents=True,exist_ok=True)


def pdf_index():
    by_hash = {}
    for p in sorted(LIB.rglob('*.pdf')):
        if '.knihovna' in p.relative_to(LIB).parts: continue
        by_hash.setdefault(sha(p), []).append(p)
    return by_hash


def download(s, fetcher, refresh=False, limit=None):
    hashes = pdf_index()
    count = 0
    reused = 0
    active = [d for d in s['documents'].values() if d.get('active')]
    paths = {}
    for doc in active:
        address = doc['url']
        dest = LIB / destination(s, doc)
        if dest in paths and paths[dest] != address:
            dest = dest.with_name(dest.stem + '_' + hashlib.sha256(address.encode()).hexdigest()[:10] + '.pdf')
        paths[dest] = address
        current = LIB / doc['local'] if doc.get('local') else None
        try:
            if current and current.exists() and sha(current) == doc.get('sha256'):
                doc.update(validate_pdf(current), status='ok')
                owners=[d for d in active if d.get('local')==doc['local']]
                target=dest
                if target.exists() and sha(target)!=doc['sha256']:
                    target=target.with_name(target.stem+'_rev_'+doc['sha256'][:12]+'.pdf')
                if current!=target and owners[0] is doc and not target.exists():
                    target.parent.mkdir(parents=True,exist_ok=True)
                    oldrel=doc['local'];current.rename(target)
                    for owner in owners:owner['local']=str(target.relative_to(LIB))
                    s['moves'].append({'from':oldrel,'to':doc['local'],'sha256':doc['sha256'],'reason':'aktualizace_zarazeni'})
                    hashes.setdefault(doc['sha256'],[]).append(target)
                    current=target
                    save(s)
                if not refresh:
                    reused+=1
                    if reused%100==0:
                        save(s)
                        print(f'Místně ověřeno {reused} hotových PDF, bez opětovného stahování.',flush=True)
                    continue
            if limit is not None and count >= limit:break
            dest.parent.mkdir(parents=True, exist_ok=True)
            part = dest.with_suffix('.pdf.part')
            # A .part is owned by this updater, never a completed library document.
            part.unlink(missing_ok=True)
            conditional = doc if refresh and current and current.exists() else None
            _, status, headers = fetcher.get(address, output=part, conditional=conditional)
            count += 1
            if status == 304:
                part.unlink(missing_ok=True)
                doc.update(validate_pdf(current), status='ok', remote_checked_at=now())
                save(s);continue
            integrity = validate_pdf(part)
            digest = sha(part)
            matching = [p for p in hashes.get(digest, []) if p.exists()]
            if matching:
                # Prefer a file already assigned to another URL. Otherwise move an
                # exact old copy into its proper numbered location, byte-for-byte.
                assigned = {LIB / d['local'] for d in s['documents'].values() if d.get('local') and d.get('status') == 'ok'}
                old = next((p for p in matching if p in assigned), matching[0])
                if old not in assigned and old != dest:
                    if dest.exists() and sha(dest) != digest:
                        dest = dest.with_name(dest.stem + '_rev_' + digest[:12] + '.pdf')
                    if not dest.exists():
                        old.rename(dest)
                        s['moves'].append({'from': str(old.relative_to(LIB)), 'to': str(dest.relative_to(LIB)), 'sha256': digest})
                        old = dest
                part.unlink()
                local = old
            else:
                if dest.exists() and sha(dest) != digest:
                    # Preserve a different existing or historical file.
                    dest = dest.with_name(dest.stem + '_rev_' + digest[:12] + '.pdf')
                if dest.exists():part.unlink()
                else:part.replace(dest)
                local = dest
            hashes.setdefault(digest, []).append(local)
            doc.update(integrity, status='ok', local=str(local.relative_to(LIB)), sha256=digest,
                       size=local.stat().st_size, downloaded_at=now(), remote_checked_at=now(),
                       etag=headers.get('etag'), last_modified=headers.get('last-modified'))
            doc.pop('error', None)
        except StopAccess as e:
            doc.update(status='failed',error=str(e),attempted_at=now());save(s)
            raise
        except (ValueError, RuntimeError, FileNotFoundError, subprocess.TimeoutExpired) as e:
            doc['status'] = 'failed';doc['error'] = str(e);doc['attempted_at'] = now()
        save(s)
        if count % 10 == 0:
            ok = sum(d.get('status') == 'ok' for d in active)
            fail = sum(d.get('status') == 'failed' for d in active)
            print(f"PDF: {ok}/{len(active)} ověřených, {fail} neúspěšných; poslední {destination(s, doc)}", flush=True)
            catalog(s)


def md(s):
    return str(s).replace('|', r'\|').replace('\n', ' ')


def counts(s, docs):
    return len(docs), sum(d.get('status') == 'ok' for d in docs)


def catalog(s):
    active = [d for d in s['documents'].values() if d.get('active')]
    total, ok = counts(s, active)
    fail = [d for d in active if d.get('status') == 'failed']
    pending = [d for d in active if d.get('status') not in ('ok', 'failed')]
    files = {d['local'] for d in active if d.get('status') == 'ok'}
    errors = s.get('errors', {})
    complete = total > 0 and ok == total and not errors and s.get('discovery_finished_at', '') >= s.get('started_at', '~')
    nparts=sum(p.get('active',True) for p in s['parts'].values())
    nchaps=sum(p.get('active',True) for p in s['chapters'].values())
    nlessons=sum(p.get('active',True) for p in s['lessons'].values())
    robotstatus=s.get('policies',{}).get('robots',{}).get('status','neověřeno')
    lines = ['# Realisticky.cz – lokální knihovna Matematika SŠ', '',
             f"Aktualizace katalogu: {now()}. **{'KOMPLETNÍ vzhledem k prověřeným veřejným odkazům' if complete else 'NEKOMPLETNÍ / probíhá zpracování'}**.", '',
             '[Původní učebnice](https://www.realisticky.cz/ucebnice.php?id=2). '
             f'[Použité veřejné rozhraní]({INDEX}). Web používá HTTP v odkazu base; HTTPS certifikát při úvodním ověření neodpovídal doméně. Ověřování certifikátů se nevypíná.', '',
             f'Zjištěno **{total} jedinečných odkazů na PDF**; integritou ověřeno **{ok}**; neúspěšných **{len(fail)}**; čekajících **{len(pending)}**. '
             f'Po sloučení totožného obsahu jde o **{len(files)} fyzických PDF**. '
             'Počet odkazů není důkazem dostupnosti: za dostupné se zde považují pouze úspěšně načtené a ověřené dokumenty. '
             'Nezpracovaný odkaz zůstává čekající; chyba detailu stránky vylučuje tvrzení o úplnosti.', '',
             f"Díly: {nparts}; kapitoly: {nchaps}; lekce: {nlessons}. "
             f"Dokončení průzkumu: {s.get('discovery_finished_at', 'zatím nedokončen')}. Chyby průzkumu: {len(errors)}.", '',
             '## Používání a aktualizace', '',
             'Autor materiálů: **Martin Krynický**. [Podmínky na webu]('+LICENSE+'): '
             '[Creative Commons Uveďte autora – Neužívejte dílo komerčně – Nezasahujte do díla 3.0 Česko](https://creativecommons.org/licenses/by-nc-nd/3.0/cz/). '
             'Jde o studijní kopie původních PDF; obsah dokumentů se neupravuje. Knihovna sama neuděluje další práva k přebírání či šíření.', '',
             'Z kořene projektu spusťte:', '',
             '```bash', 'python3 scripts/aktualizuj_realisticky.py',
             '# Kontrola uložených souborů a přegenerování katalogu bez sítě:',
             'python3 scripts/aktualizuj_realisticky.py --offline',
             '# Vynucený nový průzkum a podmíněná kontrola změn PDF:',
             'python3 scripts/aktualizuj_realisticky.py --refresh-index --refresh-pdfs', '```', '',
             'Vyžaduje Python 3, curl, pdfinfo a pdftotext. Stahuje sekvenčně, nejvýše jeden požadavek za sekundu; '
             'případné pomalejší tempo robots.txt má přednost. HTTP 401, 403 nebo 429 stahování zastaví. '
             f'Poslední HTTP stav robots.txt: {robotstatus}; podrobnosti jsou ve stavu aktualizátoru. '
             'Dokončené PDF se při běžném pokračování znovu nestahují. Index se kontroluje při každém spuštění, '
             'detaily se při běžné aktualizaci načtou znovu po 24 hodinách. '
             'Po přerušení stačí zopakovat příkaz; rozpracovaná data a stav jsou v `.knihovna/stav.json` a `*.pdf.part` přímo v cílové struktuře. '
             'Při změně obsahu existujícího PDF se odlišná starší kopie zachová. Totožné soubory mají jedinou lokální cestu; '
             'více URL proto může odkazovat na jeden soubor. Nezařazené původní kopie jsou uvedeny samostatně.', '',
             'Číselné identifikátory pocházejí z webu. V některých starších PDF je odlišné vnitřní číslování: například webová lekce 010120 má v původním PDF záhlaví 1.1.17. Původní PDF se kvůli tomu nemění.', '',
             'Integrita: hlavička a konec PDF, počet stran přes pdfinfo, úplný průchod pdftotext a SHA-256. '
             'Upozornění parseru jsou evidována v manifestu; nejde o matematické ani vizuální ověření obsahu každého dokumentu.', '',
             '## Díly a kapitoly', '', '| Díl / kapitola | Odkazů PDF | Ověřeno |', '|---|---:|---:|']
    intro = [d for d in active if not d['placement'].get('part') and d['placement'].get('section')!='appendix']
    duplicates={}
    for ck,c in s['chapters'].items():
        if c.get('active',True):duplicates.setdefault((c.get('part'),c['number']),[]).append(c)
    conflicts=[cs for cs in duplicates.values() if len(cs)>1]
    if conflicts:
        note=['Číslování webu má tyto rozpory; zachovány oba názvy a původní prefixy, kapitoly nebyly svévolně přečíslovány:','']
        for cs in conflicts:
            note.append('- '+', '.join(f"[{md(c['number']+' '+c['title'])}]({c['url']})" for c in cs)+'.')
        pos=lines.index('## Díly a kapitoly')
        lines[pos:pos]=note+['']
    lines.append(f'| [00 Úvod](00_Uvod/) | {len(intro)} | {counts(s,intro)[1]} |')
    for key, p in sorted(s['parts'].items(), key=lambda kv:int(kv[1]['number'])):
        if not p.get('active',True):continue
        ds = [d for d in active if d['placement'].get('part') == key]
        folder = f"{int(p['number']):02d}_{slug(p['title'])}"
        lines.append(f"| **[{int(p['number']):02d} {md(p['title'])}]({folder}/)** | **{len(ds)}** | **{counts(s,ds)[1]}** |")
        for ck, c in sorted(s['chapters'].items(), key=lambda kv:int(kv[1]['number'])):
            if not c.get('active',True) or c.get('part') != key:continue
            ds = [d for d in active if d['placement'].get('chapter') == ck]
            sub = f"{folder}/{int(c['number']):02d}_{slug(c['title'])}"
            lines.append(f"| [{int(p['number']):02d}.{int(c['number']):02d} {md(c['title'])}]({sub}/) | {len(ds)} | {counts(s,ds)[1]} |")
    appendices=[d for d in active if d['placement'].get('section')=='appendix']
    if appendices:
        lines.append(f'| **[99 Přílohy](99_Prilohy/)** | **{len(appendices)}** | **{counts(s,appendices)[1]}** |')
        for group in dict.fromkeys(d['placement']['group'] for d in appendices):
            ds=[d for d in appendices if d['placement']['group']==group]
            order=ds[0]['placement'].get('group_order',1)
            lines.append(f'| [{md(group)}](99_Prilohy/{order:02d}_{slug(group)}/) | {len(ds)} | {counts(s,ds)[1]} |')
    lines += ['', '## Dokumenty', '', '| Lekce / dokument | Původní URL | Lokální PDF | Stav |', '|---|---|---|---|']
    def order(d):
        c=d['placement'];p=s['parts'].get(c.get('part'),{});ch=s['chapters'].get(c.get('chapter'),{});l=s['lessons'].get(c.get('lesson'),{})
        if c.get('section')=='appendix':return 99,c.get('group_order',1),'',str(destination(s,d))
        return int(p.get('number',0)),int(ch.get('number',0)),l.get('number',''),str(destination(s,d))
    for d in sorted(active,key=order):
        c=d['placement'];l=s['lessons'].get(c.get('lesson'),{})
        title=(l.get('number','')+' '+l.get('title','')+' – '+c['label']).strip(' –')
        local = f"[PDF]({quote(d['local'], safe='/_-.')})" if d.get('status')=='ok' else f"`{destination(s,d)}`"
        label = {'ok':'OK','failed':'NEDOSTUPNÉ / CHYBA','pending':'ČEKÁ'}.get(d.get('status'),'ČEKÁ')
        if d.get('status')=='ok' and any(w.startswith('Syntax Error:') for w in d.get('warnings',[])):
            label='OK; upozornění k fontům'
        lines.append(f"| {md(title)} | [zdroj]({d['url']}) | {local} | {label} |")
    lines += ['', '## Neúspěšné či nedostupné soubory a stránky', '']
    if s.get('interruption') and not complete:
        lines += ['Přerušení: '+md(s['interruption']['reason'])+'.', '']
    if not fail and not pending and not errors:lines += ['Žádné.']
    for d in fail+pending:lines.append(f"- [{md(d['placement']['label'])}]({d['url']}): {md(d.get('error','čeká na stažení'))}.")
    for u,e in errors.items():lines.append(f'- [Stránka průzkumu]({u}): {md(e)}.')
    warnings = [d for d in active if d.get('status')=='ok' and d.get('warnings')]
    lines += ['', '## Upozornění PDF parseru', '',
              f'U {len(warnings)} PDF parser vypsal upozornění; přesná hlášení jsou u dokumentů v `.knihovna/stav.json`.', '']
    problems=[d for d in warnings if any(w.startswith('Syntax Error:') for w in d['warnings'])]
    if problems:
        lines += ['U následujících souborů parser hlásí také problém s mapováním znaků. Stažení, pdfinfo i průchod pdftotext uspěly; původní soubory nejsou opravovány. Kopírovaný text je vhodné kontrolovat proti zobrazení PDF.','']
        for d in problems:
            v=d.get('visual_check',{})
            note=(f"Vizuálně prověřeno všech {v['pages']} stran: {v.get('result','')}" if v.get('sha256')==d['sha256'] else 'Vizuální kontrola není evidována')
            lines.append(f"- [{md(Path(d['local']).name)}]({quote(d['local'],safe='/_-.')}): {md('; '.join(d['warnings']))}. {note}.")
        lines.append('')
    lines += ['', '## Přesunuté a nezařazené původní soubory', '',
              'Přesuny byly provedeny pouze po shodě SHA-256 s načteným dokumentem. Obsah se nezměnil. '
              'Starší komentáře v přípravách mohou obsahovat původní cestu; převod je zde dohledatelný.', '']
    for m in s['moves']:
        if m.get('reason')=='aktualizace_zarazeni':continue
        lines.append(f"- `{m['from']}` → [{m['to']}]({quote(m['to'],safe='/_-.')}).")
    known={d.get('local') for d in s['documents'].values()}
    unassigned=[str(p.relative_to(LIB)) for p in LIB.rglob('*.pdf') if str(p.relative_to(LIB)) not in known]
    if unassigned:
        lines += ['', 'Ponechané soubory bez přiřazeného aktuálního odkazu (nepovažují se za splnění stažení):']
        lines += [f'- [{md(p)}]({quote(p,safe="/_-.")})' for p in sorted(unassigned)]
    historical=[d for d in s['documents'].values() if not d.get('active')]
    if historical:
        lines += ['', f'Ve stavu je navíc {len(historical)} historických URL mimo aktuálně ověřený seznam; uložené soubory se nemažou.']
    tmp=LIB/'KATALOG.md.tmp';tmp.write_text('\n'.join(lines)+'\n');tmp.replace(LIB/'KATALOG.md')
    return complete


def offline(s):
    for d in s['documents'].values():
        if not d.get('local'):continue
        p=LIB/d['local']
        try:
            if sha(p)!=d.get('sha256'):raise ValueError('Neshoda SHA-256')
            d.update(validate_pdf(p),status='ok');d.pop('error',None)
        except (OSError,ValueError,subprocess.TimeoutExpired) as e:
            d.update(status='failed',error=str(e))
    save(s)


def main():
    ap=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--offline',action='store_true',help='Bez sítě ověřit PDF a přegenerovat katalog')
    ap.add_argument('--refresh-index',action='store_true',help='Ignorovat 24hodinovou mezipaměť detailů')
    ap.add_argument('--refresh-pdfs',action='store_true',help='Podmíněně ověřit i dokončené PDF')
    ap.add_argument('--delay',type=float,default=1.0,help='Nejméně 1 s mezi začátky požadavků')
    ap.add_argument('--limit',type=int,help='Omezit počet přenesených PDF při tomto běhu')
    args=ap.parse_args()
    for binary in ['curl','pdfinfo','pdftotext']:
        import shutil
        if not shutil.which(binary):ap.error('Chybí '+binary+'; nástroje automaticky neinstaluji')
    META.mkdir(parents=True,exist_ok=True)
    # Advisory lock prevents simultaneous migrations and manifest overwrites.
    import fcntl
    lock=(META/'aktualizace.lock').open('w')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:ap.error('Jiná aktualizace knihovny právě běží')
    s=json.loads(STATE.read_text()) if STATE.exists() else empty_state()
    failed=False
    signal.signal(signal.SIGTERM,lambda *_: (_ for _ in ()).throw(KeyboardInterrupt()))
    try:
        if args.offline:
            ensure_directories(s)
            offline(s)
        else:
            s['started_at']=now();s.pop('discovery_finished_at',None)
            fetcher=Fetcher(args.delay)
            policies(s,fetcher)
            # Preserve robots restrictions when using one fetcher for the whole run.
            robot_record=s['policies'].get('robots',{})
            if robot_record.get('status')==200:
                rp=RobotFileParser();rp.parse(robot_record['text'].splitlines());fetcher.robot=rp
                fetcher.delay=max(fetcher.delay,rp.crawl_delay(UA) or rp.crawl_delay('*') or 0)
            discover(s,fetcher,args.refresh_index)
            catalog(s)
            download(s,fetcher,args.refresh_pdfs,args.limit)
    except (StopAccess,RuntimeError,OSError,ValueError,KeyboardInterrupt) as e:
        failed=True;s['interruption']={'at':now(),'reason':str(e) or 'Přerušeno uživatelem'}
        print('Přerušeno:',s['interruption']['reason'],file=sys.stderr,flush=True)
    finally:
        save(s);complete=catalog(s)
    ds=[d for d in s['documents'].values() if d.get('active')]
    print(f"Výsledek: {counts(s,ds)[1]}/{len(ds)} PDF; katalog {LIB/'KATALOG.md'}",flush=True)
    return 0 if complete and not failed else 1


if __name__=='__main__':
    sys.exit(main())
