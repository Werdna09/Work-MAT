---
name: recenze
description: Nezávislá recenze výukového materiálu ve Work/MAT (matematika, didaktika, čas a obtížnost, zdroje) s protokolem v planovani/recenze/. Spouští ji učitel.
argument-hint: "matematika|didaktika|kompletni|test <cesta>"
arguments: [rezim, cesta]
disable-model-invocation: true
---

# /recenze $rezim $cesta

Proveď nezávislou recenzi podle `CLAUDE.md`, `AGENTS.md` a protokolu `planovani/recenze/README.md`. **Výukové materiály neupravuj.** Vytvoř pouze protokol recenze; při zadaném ověření oprav lze navíc doplnit stav původních nálezů podle `README.md`, se zachováním historie a rozhodnutí učitele.

## 1. Kontrola zadání

- Režim musí být `matematika`, `didaktika`, `kompletni` nebo `test` a `$cesta` musí existovat. Jinak vypiš použití `/recenze <režim> <cesta>` a skonči.
- Recenzuje se vždy **jeden** materiál, u testu jedna dvojice variant (např. `..._AB.tex`). Pokud je zadána složka nebo více souborů, zeptej se, který materiál recenzovat. Hromadné recenze nespouštěj.
- Režim `test` použij jen na soubor v `N_rocnik/testy/`; ostatní režimy na přípravy, pracovní listy a učebnici. Při nesouladu se zeptej.
- Pokud učitel odkazuje na předchozí recenzi (ověření oprav), přečti ji a kontroluj hlavně dotčené nálezy. `git diff <původní HEAD> -- <cesta>` je pomocný: u původní recenze pracovní kopie nezachycuje jen následné opravy. Porovnej také zaznamenané otisky a místa nálezů. Režim ověření oprav označ v protokolu.

## 2. Stav Gitu

Spusť `python3 -I .claude/skills/recenze/nastroje.py stav $cesta`. Výstup vlož do protokolu beze změny. Pokud jsou recenzované soubory změněné proti HEAD, recenze se týká pracovní kopie s uvedeným SHA-256; uveď to v hlavičce.

Pomocník vypisuje zkrácené otisky (12 hexadecimálních znaků); zahrň též případné další použité vstupy, které automaticky nedohledá. Nevyžaduj commit před recenzí.

## 3. Výběr subagentů (postupně, ne paralelně)

| Režim | Subagenti | Hlavní relace sama |
|---|---|---|
| `matematika` | `matematicky-recenzent` | – |
| `didaktika` | `didakticky-recenzent` | – |
| `kompletni` | `matematicky-recenzent` → `didakticky-recenzent` → `recenzent-casu-a-obtiznosti`; `recenzent-zdroju` jen tehdy, když soubor cituje externí zdroje nebo převzaté úlohy | Kontrola PDF (S) |
| `test` | `matematicky-recenzent` (obě varianty, zadání i řešení) → `recenzent-casu-a-obtiznosti`; `recenzent-zdroju` jen tehdy, když existuje evidence původu úloh | Pravidla testů (T) a PDF (S) |

Zásady:
- Pokud materiál neobsahuje matematické úlohy (např. organizační hodina), matematického recenzenta vynech a uveď to v protokolu.
- Každému subagentovi předej cestu, režim, HEAD a související soubory (PDF, `_reseni.tex`, rozpis). **Nepředávej mu nálezy jiných subagentů ani kontrolní zprávy Codexu**, aby zůstal nezávislý. Při cíleném ověření oprav předej určená původní ID a jejich rozsah; tento postup nevydávej za slepou recenzi.
- Při nové recenzi matematickému recenzentovi připomeň slepou fázi A (`nastroje.py zadani`) a její omezení pro neoddělitelná zadání; cílené ověření známých nálezů označ odlišně.

## 4. Kontroly hlavní relace

- **S – PDF:** existuje PDF vedle `.tex`? Porovnej jeho obsah se zdrojem; Git stav a čas změny jsou jen pomocné údaje, ne důkaz shody. Prohlédni všechny strany nástrojem Read (parametr `pages`). Pokud to nestačí, vykresli je jednoduchým příkazem `pdftoppm -r 60 -png <pdf> <scratchpad>/strana`, bez `mkdir` a bez spojování s dalšími příkazy, do dočasného adresáře povoleného v `.claude/settings.json`. Malé vzorce a sporná místa vykresli ve vyšším rozlišení. Kontroluj: diakritika, přetékání, prázdné strany, čitelnost; u `A5x2` dvě varianty na jedné A4 bez zásahu do sebe. Při recenzi nekompiluj; neověřenou shodu označ jako omezení.
- **T – test:** text žákovského PDF z `pdftotext -layout <pdf> -` prohledej na bodování, maximum bodů, stupnici a procenta (`bod`, `b.`, `%`, `známk`, `stupnice`, `výborn`). Každý výskyt posuď v kontextu podle `AGENTS.md`, včetně výjimky pro výslovně vyžádané bodování; procenta v matematickém zadání nejsou sama o sobě vada. Hlavička musí mít jméno, třídu, datum a prázdná pole „Počet bodů“ a „Známka“. Řešení nesmí být v žákovské verzi. Varianty v souboru musí odpovídat názvu souboru.

## 5. Sloučení a ověření nálezů

- Přidělené ID: `<ID recenze>.<oblast><pořadí>` podle `planovani/recenze/README.md`. Duplicitní nálezy slouč.
- Každý nález před zápisem ověř: existuje uvedený řádek? Platí důkaz? **Součty a jiné výpočty přepočítej** (`python3 -I -c`), zvláště součty minut v časovém odhadu. Neověřitelný nebo vyvrácený nález nezapisuj jako nález; uveď ho v *Omezeních* jako zamítnutý podnět.
- Každý zapsaný nález musí mít závažnost, místo, důkaz či zdůvodnění, návrh minimální opravy a stav `OTEVŘENO`.

## 6. Protokol

Ulož `planovani/recenze/<ID>_<KratkyPopis>.md` ve struktuře z `planovani/recenze/README.md`: hlavička, stav Gitu, verdikt po oblastech, přehled nálezů, nálezy podrobně, zkontrolované položky, omezení. Piš česky a věcně. Existující protokol nenahrazuj novým obsahem. Povolené doplnění stavů a odkazů při ověření oprav i oprava chyby v protokolu musí zachovat auditní historii podle oddílu „Oprava chyby v protokolu“ v `README.md`.

## 7. Závěrečná odpověď

Nejprve spusť `git status --short` a ověř, že od začátku recenze přibyly nebo se změnily jen soubory v `planovani/recenze/`. Jakoukoli jinou změnu výslovně oznam, nic nevracej. Potom uveď cestu k protokolu, verdikt po oblastech, počet nálezů podle závažnosti, nejzávažnější nálezy jednou větou a omezení. Nic neopravuj. Další předání se řídí společným postupem v `AGENTS.md`.
