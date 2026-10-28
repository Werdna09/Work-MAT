#!/usr/bin/env python3
"""Pomocné nástroje recenze Claude Code (Work/MAT). Pouze čtení; Python stdlib.

Použití z kořene projektu:
  python3 -I .claude/skills/recenze/nastroje.py stav CESTA [CESTA ...]
  python3 -I .claude/skills/recenze/nastroje.py zadani SOUBOR.tex
  python3 -I .claude/skills/recenze/nastroje.py prekryv SOUBOR.tex ZDROJ.pdf [ZDROJ.pdf ...]

stav     vypíše stav Gitu a otisky souborů pro hlavičku recenze a navrhne ID recenze
zadani   vypíše .tex se skrytými řešeními (část za \\tcblower a \\reseni{...})
prekryv  hledá shodné úseky textu mezi .tex a PDF (orientační kontrola převzetí)

Skript nic nezapisuje.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RECENZE = ROOT / "planovani" / "recenze"
BOXY = r"(?:prikladReseniBox|zadaniReseniBox)"


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def souvisejici(p: Path) -> list[Path]:
    """K .tex přidá PDF a u testu také soubor s řešením."""
    out = [p]
    if p.suffix == ".tex":
        out.append(p.with_suffix(".pdf"))
        if "/testy/" in p.as_posix() and not p.stem.endswith("_reseni"):
            r = p.with_name(p.stem + "_reseni.tex")
            out += [r, r.with_suffix(".pdf")]
    return out


def dalsi_id() -> str:
    dnes = dt.date.today().isoformat()
    cisla = [int(m.group(1)) for f in RECENZE.glob(f"R-{dnes}-*")
             if (m := re.match(rf"R-{dnes}-(\d\d)", f.name))]
    return f"R-{dnes}-{max(cisla, default=0) + 1:02d}"


def stav(cesty: list[str]) -> int:
    soubory: list[Path] = []
    for c in cesty:
        p = (ROOT / c) if not Path(c).is_absolute() else Path(c)
        for s in souvisejici(p):
            if s not in soubory:
                soubory.append(s)
    head = git("rev-parse", "HEAD")
    print(f"- Návrh ID recenze: `{dalsi_id()}`")
    print(f"- Datum a čas: {dt.datetime.now().isoformat(timespec='minutes')}")
    print(f"- Větev: `{git('branch', '--show-current') or '(odpojený HEAD)'}`")
    print(f"- HEAD: `{head}` – {git('log', '-1', '--format=%s (%ci)')}")
    zmeny = [l for l in git("status", "--porcelain").splitlines() if l]
    print(f"- Pracovní strom: {'čistý' if not zmeny else f'{len(zmeny)} změněných/nesledovaných položek'}")
    print()
    print("| Soubor | Git | SHA-256 (12) | Upraveno |")
    print("|---|---|---|---|")
    for s in soubory:
        r = rel(s)
        if not s.exists():
            if s.suffix == ".pdf" or s.stem.endswith("_reseni"):
                print(f"| `{r}` | chybí | – | – |")
            continue
        st = git("status", "--porcelain", "--", r)
        if st:
            gs = "změněn" if st[:2].strip() in ("M", "MM", "AM") else f"`{st[:2]}`"
        elif git("ls-files", "--", r):
            gs = "shodný s HEAD"
        else:
            gs = "nesledován/ignorován"
        h = hashlib.sha256(s.read_bytes()).hexdigest()[:12]
        m = dt.datetime.fromtimestamp(s.stat().st_mtime).isoformat(timespec="minutes")
        print(f"| `{r}` | {gs} | `{h}` | {m} |")
    for s in soubory:
        pdf = s.with_suffix(".pdf")
        if s.suffix == ".tex" and s.exists() and pdf.exists() and pdf.stat().st_mtime < s.stat().st_mtime:
            print(f"\nUPOZORNĚNÍ: `{rel(pdf)}` je starší než `{rel(s)}`; PDF nemusí odpovídat zdroji.")
    return 0


def zadani(cesta: str) -> int:
    p = Path(cesta)
    if p.stem.endswith("_reseni"):
        print("CHYBA: Toto je soubor s řešením; ve slepé fázi ho nečti.", file=sys.stderr)
        return 1
    src = p.read_text(encoding="utf-8-sig")
    n = 0

    def skryj(m: re.Match) -> str:
        nonlocal n
        n += 1
        return m.group(1) + f"\\tcblower\n[ŘEŠENÍ {n} SKRYTO]\n" + m.group(3)

    src = re.sub(rf"(\\begin\{{{BOXY}\}}.*?)\\tcblower(.*?)(\\end\{{{BOXY}\}})", skryj, src, flags=re.S)
    # Zastaralé \reseni{...}: skryj obsah s vyvážením závorek.
    out, i = [], 0
    while (j := src.find("\\reseni{", i)) != -1:
        k, hloubka = j + len("\\reseni{"), 1
        while k < len(src) and hloubka:
            hloubka += {"{": 1, "}": -1}.get(src[k], 0) if src[k - 1] != "\\" else 0
            k += 1
        n += 1
        out += [src[i:j], f"\\reseni{{[ŘEŠENÍ {n} SKRYTO]}}"]
        i = k
    out.append(src[i:])
    print("".join(out))
    print(f"% --- nastroje.py: skryto {n} řešení ---", file=sys.stderr)
    return 0


def slova(text: str) -> list[str]:
    return re.findall(r"[0-9a-záčďéěíňóřšťúůýž]+", text.lower())


def tex_text(src: str) -> str:
    src = "\n".join(re.split(r"(?<!\\)%", l, maxsplit=1)[0] for l in src.splitlines())
    return re.sub(r"\\[A-Za-z@]+\*?", " ", src)


def prekryv(tex: str, pdfs: list[str], n: int = 8) -> int:
    t = slova(tex_text(Path(tex).read_text(encoding="utf-8-sig")))
    zdroj: set[tuple[str, ...]] = set()
    for pdf in pdfs:
        r = subprocess.run(["pdftotext", "-q", pdf, "-"], capture_output=True, text=True)
        if r.returncode:
            print(f"CHYBA: pdftotext selhal pro {pdf}", file=sys.stderr)
            return 1
        s = slova(r.stdout)
        zdroj |= {tuple(s[i:i + n]) for i in range(len(s) - n + 1)}
    hit = [i for i in range(len(t) - n + 1) if tuple(t[i:i + n]) in zdroj]
    useky, start, konec = [], None, None
    for i in hit:
        if start is not None and i <= konec:
            konec = i + n
        else:
            if start is not None:
                useky.append((start, konec))
            start, konec = i, i + n
    if start is not None:
        useky.append((start, konec))
    pokryto = sum(b - a for a, b in useky)
    print(f"Slov v .tex (bez příkazů a komentářů): {len(t)}; shodných úseků (≥{n} slov): {len(useky)}; "
          f"pokryto slov: {pokryto} ({100 * pokryto / max(len(t), 1):.1f} %)")
    for a, b in sorted(useky, key=lambda u: u[0] - u[1])[:25]:
        print(f"- [{b - a} slov] {' '.join(t[a:b])}")
    print("Pozn.: matematické zápisy se rozpadají na krátké tokeny; shoda je podnět k ručnímu porovnání, ne důkaz.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] not in ("stav", "zadani", "prekryv"):
        print(__doc__, file=sys.stderr)
        return 2
    if argv[0] == "stav":
        return stav(argv[1:])
    if argv[0] == "zadani":
        return zadani(argv[1])
    if len(argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    return prekryv(argv[1], argv[2:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
