# Katalog referenčních materiálů – Work/MAT

> Tento katalog je **rozcestník na existující soubory**, nikoli další šablona ani banka automaticky schválených příkladů. Všechny cesty jsou relativní ke kořeni `~/Work/MAT`. Poslední aktualizace popisů a cest: 28. 10. 2026; nejde o nové matematické schválení vzorů.

## 1. Jak katalog používat

1. Před tvorbou si přečti kořenový `AGENTS.md` a pravidla příslušného Skillu v `.agents/skills/`. Při přípravách přečti také `sablony/pripravy/TUTORIAL_pripravy.md` a skutečný zdroj společného stylu.
2. Vyber **jeden nebo dva nejbližší vzory podle typu úlohy**; není nutné procházet každou přípravu. Vždy ověř, že soubory v projektu opravdu existují a že jejich aktuální obsah odpovídá tomuto popisu.
3. **Přebírej strukturu a didaktické postupy, ne automaticky matematická zadání.** Závazná je aktuální šablona a projektová pravidla. Ukázkové dokumenty mohou obsahovat rozpracovaná místa.
4. U testů výběr konkrétních zadání a jejich schvalování řídí `AGENTS.md` a Skill `vytvor-test`. Žádný dokument uvedený jako vzor sám o sobě nedává souhlas s použitím nebo úpravou úloh.
5. Pokud je vzor nedostupný, zastaralý nebo odporuje zadání, **neodvozuj z něj pravidlo**. Neopravuj vzor, společný styl ani jiné soubory bez výslovného zadání.
6. Vytvořený dokument kontroluj matematicky i technicky; tam, kde to pro samostatný dokument dává smysl, spusť `./scripts/build_latex.sh cesta/k/souboru.tex` a vizuálně ověř PDF.

### Stavy materiálů

- **Projektová šablona:** aktuální technický nebo typografický základ. Obsah a skutečná makra je nutné před použitím přečíst; katalog ji nenahrazuje.
- **Kandidát na vzor:** užitečná existující ukázka. Zde uvedené didaktické a typografické vlastnosti nejsou schválením učitele ani potvrzením bezchybnosti celé ukázky.
- **Technicky ověřený kandidát:** u dané verze proběhla kompilace a kontrola PDF; automaticky to neznamená schválený výklad či zadání.
- **Neprověřený materiál:** lze jej po otevření využít pro orientaci, nikoli automaticky pro přebírání úloh.

## 2. Závazná technická východiska

| ID | Typ | Relativní cesta | Kdy ji použít |
|---|---|---|---|
| S-P1 | Projektová šablona | `sablony/pripravy/priprava.sty` | Společná makra, záhlaví, definice boxů a grafická podoba příprav. **Nekopírovat** do jednotlivých hodin. |
| S-P2 | Projektová šablona | `sablony/pripravy/TEMPLATE_Priprava.tex` | Základ nově vytvářené učitelské přípravy. |
| S-P3 | Projektový návod | `sablony/pripravy/TUTORIAL_pripravy.md` | Pojmenování hodin, práce s `definiceBox`, `prikladReseniBox`, `zadaniReseniBox`, `\tcblower` a metodickými poznámkami. |
| S-T1 | Projektová šablona | `sablony/testy/A5x2.tex` | Krátký test: dvě varianty na jedné A4; ověřit skutečné rozměry a přetečení. |
| S-T2 | Projektová šablona | `sablony/testy/A4.tex` | Delší test: jedna varianta na A4 podle stávající konvence. |

> Šablony testů určují především **rozvržení**. Nejsou schválenou sadou matematických úloh. Pokud se katalog a šablona liší, otevři skutečný soubor a postupuj podle `AGENTS.md`.

## 3. Přípravy – příklady použití

| ID | Soubor | Proč se do něj podívat | Stav a omezení |
|---|---|---|---|
| P-01 | `1_rocnik/pripravy/01_ÚVD_ÚvodníHodina.tex` | Organizační hodina: praktické učitelské pokyny místo matematického výkladu. | Kandidát. Nevyvozuj z něj povinnou strukturu matematických hodin. |
| P-02 | `1_rocnik/pripravy/02_VRL_CoJeVyrok.tex` | Motivace, krátké definice v oddělených boxech, klasifikace výroků, jednoduché úlohy s řešením. | Kandidát. V aktuálním zdroji není označení rozpracovanosti; jeho nepřítomnost sama nedokládá schválení. |
| P-03 | `1_rocnik/pripravy/03_VRL_PravdivostSlozenychVyroku.tex` | Přehledná pravdivostní tabulka, postupné výpočty logických formulí, práce s implikací a metodické poznámky. | Kandidát. Vždy ověř konkrétní matematický obsah a aktuální verzi. |
| P-04 | `1_rocnik/pripravy/04_VRL_Kvantifikatory.tex` | Souvislý výklad na více stranách, kvantifikátory, kombinace řešených příkladů, samostatného procvičení a volitelného rozšíření. | Kandidát. Dřívější záznam technické kontroly se týkal staršího třístránkového PDF; aktuální PDF má čtyři strany. Kontrolu starší verze nepřenášej automaticky na současnou. Učitelské schválení zde není doloženo. |

**Poznámka k P-04:** Dřívější připomínka k části *Samostatné procvičení*, úloze **a)**, je v aktuálním zdroji již zapracována zněním „Doplň **obecný kvantifikátor**“. Původní kritérium „aby vznikl pravdivý výrok“ samo neurčovalo jedinou možnost: nad reálnými čísly jsou pro vlastnost `x² + 1 > 0` pravdivé **obě** kvantifikace (`∀` i `∃`). Při použití vzoru rozlišuj tento konkrétní ověřený stav formulace od neprovedené nové kontroly celého dokumentu.

## 4. Testy, pracovní listy a zdroje úloh

- **Testy:** Pro sazbu používej `S-T1` nebo `S-T2`. V projektu může existovat například `2_rocnik/testy/ExponencialniRovnice/01_test_ExponencialniRovnice_AB.tex`; jde nanejvýš o **neprověřený kandidát** pro porovnání konvencí, nikoli o schválený obsahový vzor. Nejprve ho otevři, zkontroluj a ověř jeho aktuální podobu.
- **Pracovní listy:** Zatím zde není označen žádný konkrétní schválený referenční pracovní list. Při tvorbě se řiď `AGENTS.md` a skutečně dostupnou šablonou v `sablony/pracovni_listy/`, pokud existuje. Nové vzory do katalogu přidávej až po kontrole.
- **Zdroj matematických zadání:** Preferuj odpovídající kapitoly v `ucebnice/`, pak příslušné `N_rocnik/pracovni_listy/` a další učitelem určené materiály podle `AGENTS.md`. Zdroj zadání není automaticky typografický vzor a každou použitou úlohu je třeba ověřit.
- **Nevěřené archivy a externí podklady:** `import_testu/` a `externi_zdroje/` nejsou schválené šablony ani automaticky ověřené banky úloh. Respektuj jejich určení, omezení a autorská práva.

## 5. Jak přidat nový schválený vzor

Učitel nejprve výslovně vybere konkrétní soubor. Poté zkontroluj (a zaznamenej, co skutečně proběhlo):

1. matematickou správnost včetně řešení a jednoznačnosti zadání;
2. soulad se šablonou, čitelnost a vhodnost didaktické struktury;
3. úspěšnou kompilaci a vzhled **všech** stran PDF, pokud jde o LaTeX;
4. učitelovo **výslovné schválení** právě této verze.

Teprve potom změň status na **Schválený referenční vzor** a doplň datum a rozsah ověření. Změní-li se výrazně obsah nebo společná šablona, status znovu prověř. Nevytvářej kopii vzorového dokumentu v `sablony/`; katalog má odkazovat na jeho původní umístění.
