---
name: vytvor-test
description: Navrhni nebo po schválení sestav matematický test v repozitáři Work/MAT (varianty A–L, LaTeX, oddělená řešení). Použij při práci na testech a písemných pracích, nikoli při tvorbě příprav, pracovních listů či učebnice.
---

# Testy matematiky v projektu Work/MAT

Pracuj z kořene repozitáře `Work/MAT`. Tento skill určuje **pracovní postup**, nikoli nové požadavky na sazbu nebo obtížnost. Závazné podrobnosti najdeš v kořenovém `AGENTS.md`, zvláště v oddílech **Testy: umístění, pojmenování a šablony**, **Testy: obtížnost a zadávání**, **Výběr úloh pro testy**, **Matematická kontrola** a **Kompilace a kontrola výstupu**. Při rozporu se řiď aktuálním `AGENTS.md` a upozorni na něj. Sám tento soubor ani šablony neměň.

## Nejdřív rozhodni, ve které fázi jsi

1. **Návrh** – učitel zadal jen téma, typ, ročník, délku nebo požadované varianty, ale **neschválil konkrétní skladbu úloh**. Prozkoumej zdroje a předlož výběr přímo v konverzaci; **nevytvářej finální žákovské `.tex` ani PDF**. Vyčkej výběru či schválení učitelem. Povolení „můžeš vymýšlet vlastní úlohy“ samo o sobě není schválením konkrétní skladby.
2. **Realizace** – učitel již **určil konkrétní úlohy** nebo **schválil jejich výběr a přiřazení**. Pokračuj přímo k sazbě a ověření; nevyžaduj opakované schválení totožného výběru.
3. **Revize** – učitel chce opravit existující test. Měň pouze požadovanou část; není-li změněn obsah či skladba úloh, nepodmiňuj drobnou revizi novým schvalováním. Obsahové náhrady podléhají pravidlům pro schvalování a povoleným změnám.

## Společný postup

1. **Zjisti skutečný stav.** Přečti `AGENTS.md`, relevantní `N_rocnik/tematicke_plany/SPS.pdf` nebo `GYM.pdf`, odpovídající část `ucebnice/`, existující pracovní listy, související testy a skutečný obsah `sablony/testy/A4.tex` a `sablony/testy/A5x2.tex` (pokud existují). Chybějící podklady nepředstírej. Respektuj zadání a dosud probrané učivo; podstatné chybějící údaje (např. čas, pomůcky, rozsah) si vyjasni, nejsou-li patrné z podkladů.
2. **Dohledávej konkrétní úlohy v pořadí dle `AGENTS.md`.** Přednostně autorova `ucebnice/`, potom `N_rocnik/pracovni_listy/`, další materiály určené učitelem a až pomocně neověřený archiv `import_testu/`. Nové úlohy nevymýšlej bez výslovného svolení. U každé úlohy si eviduj přesnou cestu a identifikaci úlohy; v žákovském zadání zdroje automaticky neuváděj. Autorská práva k externím podkladům respektuj.
3. **Nepozměňuj zadanou úlohu bez povolení.** Čísla, parametry, podmínky, požadovaný postup a obtížnost převzaté úlohy neměň svévolně. Pokud učitel žádá úlohy obdobné, zachovej požadovaný matematický princip a eviduj původní vzor. Zjistíš-li chybu ve schválené úloze, oznam ji a vyžádej si rozhodnutí o opravě či náhradě.

### Ve fázi návrhu (bez finálního souboru)

4. Předlož **konkrétní kandidáty** včetně jejich zadání či jednoznačné identifikace, zdroje (cesta + číslo úlohy), potřebného postupu, obtížnosti, odhadu času a návrhu rozdělení do požadovaných variant. Rozliš, co je ověřené a co je pouze návrh. Nenahrazuj zadání neurčitými popisky typu „příklad na rovnice“.
5. Upozorni, pokud úloh pro požadované varianty není dost, případně jsou příliš obtížné nebo se nehodí na stanovený čas. Požádej o konkrétní schválení nebo změnu výběru. **Zastav se zde**: negeneruj finální test, soubor s řešením ani PDF jen na základě tématu.

### Ve fázi realizace (schválená skladba)

6. **Varianty a názvy:** testy ukládej do `N_rocnik/testy/<Tematicky_celek>/`. Použij vzor `[NN]_test_[NazevBezDiakritiky]_[AB|CD|EF|GH|IJ|KL].tex`. `NN` značí pořadí testu **v tématu**, ne v roce. Každá dvojice variant má vlastní `.tex`; `AB` obsahuje A i B, `CD` obsahuje C i D atd. Nevytvářej další dvojice bez zadání. U požadavku pouze na jednu variantu ověř konvenci pojmenování u učitele. Respektuj stupně obtížnosti podle `AGENTS.md`; uvnitř dvojice mají být varianty srovnatelné.
7. **Šablona:** zvol skutečně dostupnou a funkční `sablony/testy/A5x2.tex` (krátký test, dvě přibližně A5 na jedné A4 na šířku) nebo `A4.tex` (delší práce), podle délky, rozsahu a učitelova pokynu. Vytvoř nový soubor z kopie šablony; **neupravuj originální šablonu**. Zachovej hlavičku (jméno, třída, datum, prázdná pole „Počet bodů“ a „Známka“). Zkontroluj skutečně vytištěné varianty proti názvu souboru.
8. **Žákovské zadání bez nevyžádaného bodování:** nepřidávej bodové hodnoty úloh, maximální body, procenta ani klasifikační stupnici, pokud si je učitel výslovně nevyžádal; platí to i pro text převzatý ze šablony. Prázdné pole „Počet bodů“ v hlavičce ponech.
9. **Oddělená řešení:** vytvoř samostatné, jednoznačně pojmenované řešení ke každé požadované dvojici variant, pokud učitel neurčil jinak. Žákovská verze nikdy nesmí prozradit výsledky. Řešení musí obsahovat dostatečný matematický postup, nejen konečná čísla. Bodovací schéma do řešení přidej **jen na výslovnou žádost**.
10. **Matematicky ověř každou variantu zvlášť.** Prověř správnost i jednoznačnost každého zadání, podmínky, definiční obory, ekvivalentnost úprav, výsledky, časovou náročnost a srovnatelnost A/B, C/D apod. Kde to jde, použij nezávislou kontrolu (dosazení, jiný postup, výpočetní nástroj). Neoznačuj neprovedenou kontrolu za hotovou.
11. **Kompilace a kontrola PDF:** je-li dostupný `scripts/build_latex.sh`, spusť ho z kořene projektu samostatně pro **každý schválený `.tex`** (zadání i řešení), například `./scripts/build_latex.sh N_rocnik/testy/Tema/01_test_Tema_AB.tex`. Skript ověřuje základní strukturu, kompilaci a uložení PDF vedle `.tex`. Pokud skript chybí, použij existující funkční postup s `latexmk`; pokud existující skript selže, zjisti a oznam příčinu, nepovažuj kontrolu za splněnou. Zkontroluj log a vizuálně **všechny vytvořené varianty**. U `A5x2` ověř, že jsou skutečně dvě varianty na jedné A4 bez přesahů; u A4 správné oddělení stran. Zkontroluj čitelnost, diakritiku a nepřítomnost řešení nebo bodování v žákovských PDF. Ověř, že finální PDF existují vedle příslušných `.tex`, nikoliv pouze v `/tmp`. Samotný skript neumí ověřit srovnatelnost variant ani matematickou správnost.
12. **Dohlédni na rozsah změn:** neupravuj bez pokynu jiné testy, učebnici, pracovní listy, přípravy, osnovy ani šablony. Neprováděj `git commit` ani `git push` bez požadavku. Při dokončení uveď vytvořené soubory, použité a schválené zdroje, výsledek matematické i vizuální kontroly a případné nedořešené body.

## Hranice

- Tento skill je pouze pro běžné matematické testy, čtvrtletní a pololetní písemné práce. Opravné zkoušky mají samostatná pravidla; nevydávej je automaticky za další varianty běžného testu.
- Samotné téma není souhlas s novými úlohami ani se skladbou testu. U konkrétně určených a správně dostupných úloh naopak nebrzdi realizaci zbytečným opakovaným schvalováním.
- Má-li učitel výslovné jiné zadání, respektuj je v mezích platných projektových pravidel a výsledek změn popiš.
