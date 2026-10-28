@AGENTS.md

# Claude Code v projektu Work/MAT

Importovaný `AGENTS.md` je společný a závazný pro Codex i Claude Code. Tento soubor doplňuje jen pravidla specifická pro Claude Code. Při rozporu platí `AGENTS.md`; rozpor oznam učiteli.

## Použití společných postupů

- Role, schvalování a předávání určuje [společný pracovní postup](AGENTS.md#výchozí-spolupráce-codexu-claude-code-a-učitele). Při výslovném zadání tvorby nebo oprav použij příslušný postup z `.agents/skills/` a technické kontroly v `AGENTS.md`.
- Příkaz `/recenze` je definován v [.claude/skills/recenze/SKILL.md](.claude/skills/recenze/SKILL.md); specializované recenzenty obsahuje `.claude/agents/`. Podobu protokolu určuje [planovani/recenze/README.md](planovani/recenze/README.md).
- Oprávnění nástrojů spravuje `.claude/settings.json`. Změna role není pokynem k přepsání této konfigurace ani k obcházení jejích omezení.

## Recenzní režim (výchozí)

- V režimu `/recenze` pouze čti materiály. Zapisovat smíš jen protokol, záznam ověření nálezů a opravu chyby v protokolu (s auditní historií) v `planovani/recenze/`, podle tamního `README.md`; neměň rozhodnutí učitele. Nalezenou chybu neopravuj, zapiš ji jako nález s návrhem opravy.
- Recenzi spouští učitel příkazem `/recenze`. Subagenty vybírej podle režimu a charakteru materiálu, ne automaticky všechny.
- Při recenzi nespouštěj `scripts/build_latex.sh` ani `latexmk`, protože přepisují PDF a vytvářejí pomocné soubory. K vizuální kontrole prohlédni existující PDF nástrojem Read. Pokud to nestačí, vykresli ho přes `pdftoppm` do dočasného adresáře podle povolení v `.claude/settings.json`. Prokázaný nesoulad PDF se zdrojem je nález; nejistotu o jeho aktuálnosti uveď jako omezení.
- Python (`python3 -I`, jen standardní knihovna) používej ke čtení a výpočtům. Nikdy jím nezapisuj soubory v projektu. Balíčky neinstaluj; chybějící `sympy` není chyba projektu.
- U externích podkladů dodržuj [pravidla lokální knihovny](AGENTS.md#lokální-knihovna-realistickycz). V recenzním režimu nespouštěj aktualizátor ani nic nestahuj.
- **Nezávislost:** kontrolní zprávy Codexu (`planovani/KONTROLA_*.md`, `planovani/REVIZE_*.md`, `*_Kontrola.md`) čti až po vlastním závěru. Výjimkou je cílené ověření oprav: vyjdi z určených nálezů, ale opravu sám přepočítej a vymez rozsah ověření.
- Recenze není schválení. Nikdy nepiš, že materiál je „schválený“ nebo „bezchybný“. Piš „bez zjištěné chyby v uvedeném rozsahu“.

## Omezení oprávnění (nejde o sandbox)

`.claude/settings.json` chrání před omylem, **není to bezpečnostní sandbox**. Testem v režimu `dontAsk` (2026-10-28) bylo ověřeno zamítnutí zápisu nástroji Edit/Write a přesměrováním `>` do materiálů, `AGENTS.md`, `ucebnice/` a `externi_zdroje/`. Zamítnuty byly také aktualizátor knihovny, `curl`, `build_latex.sh` a `git commit`. Zbývající mezery:

- Pravidla pro úpravy platí pro nástroje Edit/Write a pro zápisy, které Claude Code v příkazu Bash rozpozná (přesměrování, `tee`, `sed` apod.). **Neplatí pro procesy, které zapisují samy.** Povolený `python3 -I -c` tak technicky může zapsat kamkoli. Zákaz zápisu z Pythonu je jen pokyn a kompenzuje ho kontrola `git status` po recenzi.
- Pravidla Bash porovnávají text příkazu. Spuštění přes jinou cestu, `sh -c` nebo skript nemusí zachytit.
- **Slepá fáze matematické recenze není technicky vynucená.** Subagent smí číst celý soubor. `nastroje.py zadani` skrývá jen části za `\tcblower` a `\reseni{}`, ne výsledky ve volném textu, komentářích nebo PDF. Pořadí čtení lze doložit jen ze záznamu relace.
- V režimu auto o příkazech bez pravidla rozhoduje klasifikátor. Pravidla `ask` vyvolají dotaz vždy.
- V této instalaci nejsou samostatné nástroje Grep a Glob. Vyhledávání probíhá vestavěným `grep` a `find` v Bash.
- Povolení `pdftoppm` počítá s dočasným adresářem `/tmp/claude-1000/` (UID 1000). Na jiném počítači si vyžádá potvrzení.

Tvrdou izolaci by zajistil jen sandbox Claude Code na úrovni operačního systému. Zapnutý není.

## Evidence recenzované verze

Pro načtení stavu a otisků použij `python3 -I .claude/skills/recenze/nastroje.py stav <cesta>`. Pracovní kopie se může lišit od HEAD; závěr se pak vztahuje k zaznamenaným otiskům, ne automaticky ke commitu. Gitové operace se řídí `AGENTS.md` a oprávněními nástroje.
