# Recenzní protokol – Work/MAT

Tato složka obsahuje nezávislé recenze výukových materiálů. Společné role, schvalování a pořadí spolupráce určuje [AGENTS.md](../../AGENTS.md#výchozí-spolupráce-codexu-claude-code-a-učitele); implementaci příkazu `/recenze` popisuje [Claude Skill](../../.claude/skills/recenze/SKILL.md). Zde je závazná technická podoba protokolu a evidence nálezů.

## Evidence při předávání

1. Recenzent zaznamená větev, HEAD, Git stav a otisky recenzovaných souborů. **Commit před recenzí ani před ověřením oprav není podmínkou.** Změněné či nesledované soubory označí jako pracovní kopii.
2. Nový protokol uloží sem; do recenzovaného materiálu nezasahuje. Podklady rozliší na skutečně přečtené, obrazově prohlédnuté a nedostupné.
3. Učitel u každého nálezu rozhodne: `SCHVÁLENO` (opravit), nebo `ZAMÍTNUTO` (s krátkým důvodem). Rozhodnutí zapíše do sloupce *Stav*, případně je nástroj zaznamená podle výslovného pokynu s odkazem na toto rozhodnutí. Nástroj je nesmí sám odvodit z recenzního verdiktu.
4. Autor opravy uvede ID schválených nálezů, změněné cesty, provedené kontroly a otisky opravené verze. Stav doplní jako `OPRAVENO (pracovní kopie; SHA-256 …)`; je-li příslušný commit již výslovně povolen a proveden, lze místo toho uvést jeho ID. Samotný stav `OPRAVENO` ke commitu neopravňuje.
5. Ověření opravy dostane nový protokol s odkazem na původní ID a novou identifikací verze. Ověřující doplní k původnímu nálezu stav `OVĚŘENO` s odkazem na nový protokol; přetrvávající problém vysvětlí a nové problémy eviduje novým ID.

Při aktualizaci stavů zachovej původní popis, důkaz, rozhodnutí učitele a historii změn (kdo, kdy, kterou verzi ověřil). Nová recenze původní protokol nenahrazuje. Rozdíl proti původnímu HEAD může zahrnovat i změny před recenzí; při opravách pracovní kopie porovnej také původní otisky a zaznamenaná místa nálezů.

### Oprava chyby v protokolu

Chybu v již uloženém protokolu (početní, věcnou, chybné místo či citaci) opraví recenzent v témže protokolu a učiteli ji oznámí. Oprava musí zachovat auditní historii původního nálezu i jeho opravy:

- **ID nálezu se nemění.** Nové ID dostane jen skutečně nový problém.
- **U opraveného místa** se vyznačí, že bylo opraveno, s datem a odkazem na oddíl *Historie protokolu*. Změna závažnosti nebo zrušení nálezu se uvede výslovně, například „DOPORUČENÍ (původně DŮLEŽITÁ)“.
- **Do oddílu *Historie protokolu*** na konci protokolu se zapíše datum, kdo opravu provedl, původní znění, nové znění nebo výpočet, důvod a způsob nezávislého ověření. Původní text se nemaže beze stopy.
- **Oprava protokolu nemění stav nálezu** ani rozhodnutí učitele a nenahrazuje ověření opravy materiálu. Recenzovaný materiál se kvůli ní neupravuje.

## Pojmenování a identifikátory

- Soubor: `R-RRRR-MM-DD-NN_<KratkyPopis>.md`, například `R-2026-10-28-01_1roc_28_MOC.md`.
- ID recenze: `R-RRRR-MM-DD-NN` (pořadí recenze v daném dni).
- ID nálezu: `<ID recenze>.<oblast><pořadí>`, například `R-2026-10-28-01.M02`.
  Oblasti: **M** matematika, **D** didaktika a výklad, **C** čas a obtížnost, **Z** zdroje a autorská práva, **S** sazba a PDF, **T** pravidla testů (bodování, hlavička, varianty).

## Závažnost

| Stupeň | Význam |
|---|---|
| **KRITICKÁ** | Chybný výsledek nebo tvrzení, neřešitelné či nejednoznačné zadání měnící odpověď, prozrazené řešení nebo nevyžádané bodování v žákovském PDF. Před použitím ve výuce opravit. |
| **DŮLEŽITÁ** | Chybějící podmínka či krok, didakticky zavádějící výklad, nezvládnutelný povinný obsah hodiny, nesrovnatelné varianty, nedohledatelný zdroj či nedoložené rozsáhlé převzetí. Návaznost, čas a výjimky posuzuj podle zadání a `AGENTS.md`, nikoli podle samotné délky dokumentu nebo přítomnosti volitelného rozšíření. |
| **DROBNÁ** | Formulace, terminologie, sazba, evidence zdrojů bez vlivu na správnost. |
| **DOPORUČENÍ** | Nepovinné zlepšení. |

## Stavy nálezů

- Přijatý nález: `OTEVŘENO` → `SCHVÁLENO` → `OPRAVENO (<verze>)` → `OVĚŘENO (<protokol>)`.
- Zamítnutý nález: `OTEVŘENO` → `ZAMÍTNUTO (<důvod>)`; bez opravy.
- Neúspěšné ověření: doplň `NEOVĚŘENO (<důvod a protokol>)`. Další oprava zůstává v původně schváleném rozsahu; rozšíření vyžaduje rozhodnutí učitele.

`<verze>` může být pracovní kopie s otisky dotčených souborů nebo skutečně existující commit. Při zkráceném otisku vždy uveď jeho délku; pomocný nástroj níže vypisuje prvních 12 hexadecimálních znaků SHA-256. V případě nejednoznačnosti použij úplný otisk. `OVĚŘENO` označuje výsledek kontroly nálezu v konkrétní verzi, nikoli schválení celého materiálu.

## Struktura protokolu

1. **Hlavička:** ID, datum, režim, recenzované soubory, použití subagenti.
2. **Stav Gitu:** výstup `python3 -I .claude/skills/recenze/nastroje.py stav <cesty>` spuštěný z kořene projektu (větev, HEAD, stav souborů, zkrácený SHA-256). Zahrň `.tex`, existující PDF a oddělené řešení; pomocník k zadanému `.tex` hledá sourozenecké soubory automaticky. Další skutečně použité vstupy uveď výslovně. Chybějící soubor zaznamenej.
3. **Verdikt po oblastech:** *bez zjištěné chyby / chyba / nejednoznačnost / nelze ověřit*, vždy s rozsahem toho, co bylo skutečně zkontrolováno.
4. **Přehled nálezů:** tabulka `ID | Závažnost | Místo | Stručně | Stav`.
5. **Nálezy podrobně:** u každého místo (soubor:řádek, úloha), popis, **důkaz či zdůvodnění** (výpočet, protipříklad, citace pravidla), **návrh minimální opravy** a jistota.
6. **Zkontrolované položky:** tabulka `úloha | nezávislý výsledek | výsledek v souboru | shoda | metoda`, u přípravy také časový odhad.
7. **Omezení:** co nebylo zkontrolováno a proč.
8. **Historie protokolu** (jen pokud byl protokol po uložení změněn): tabulka `datum | změna | původní znění | důvod a ověření`.
