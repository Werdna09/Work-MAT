# Společná projektová pravidla – Work/MAT

## Účel projektu

Repozitář slouží středoškolskému učiteli matematiky k tvorbě učebnice, příprav na vyučování, testů a pracovních listů. Výsledné výukové materiály vytvářej v českém jazyce a v LaTeXu, pokud uživatel výslovně nepožaduje jinak. Vždy respektuj požadovaný ročník, úroveň žáků, rozsah učiva a účel dokumentu. Neznámé důležité parametry si vyjasni; u drobností zvol přiměřený předpoklad a uveď jej.

## Závaznost a rozdělení pravidel

Tato pravidla platí pro **OpenAI Codex i Claude Code**. Před prací pročti celý soubor, nejen automaticky vložený výňatek. Výslovné zadání učitele má přednost před výchozími konvencemi, nemění však technická oprávnění nástroje. Již udělené schválení nevyžaduj znovu; rozpory konkrétně oznam.

| Hlavní místo | Obsah |
|---|---|
| `AGENTS.md` | Společná pravidla a obecný postup spolupráce. |
| [CLAUDE.md](CLAUDE.md), `.claude/` | Implementace Claude Code, recenzní režim a omezení nástrojů. |
| `.agents/skills/` | Postupy [vytvor-pripravu](.agents/skills/vytvor-pripravu/SKILL.md), [vytvor-test](.agents/skills/vytvor-test/SKILL.md), [over-matematiku](.agents/skills/over-matematiku/SKILL.md). |
| `sablony/`, [katalog vzorů](sablony/KATALOG_VZORU.md) | Sazební vzory, makra a rozcestník ukázek. |
| [Recenzní protokol](planovani/recenze/README.md) | Identifikátory, stavy a struktura předání. |

Použij odpovídající Skill; názvy a primární účel bez zadání neměň. Společná pravidla neduplikuj v dalších dokumentech, odkazuj na jejich hlavní místo. Funkční styl rozhoduje o příkazové syntaxi, nikoli o obsahových pravidlech či schvalování.

## Výchozí spolupráce Codexu, Claude Code a učitele

1. **Codex vytvoří materiál**, provede vlastní matematickou a technickou kontrolu a předá soubory, výsledky kontrol a omezení.
2. **Claude Code provede nezávislou recenzi** a uloží nálezy do `planovani/recenze/`. Lze recenzovat i pracovní kopii s doloženým stavem a otisky souborů.
3. **Učitel schválí nebo zamítne připomínky.** Schválení opravy neznamená schválení celého materiálu ani commitu.
4. **Codex provede schválené opravy**, ověří dopady a u LaTeXu znovu sestaví dotčená PDF.
5. **Claude podle potřeby a na pokyn učitele ověří opravené části** a jejich dopady; rozliší opravené, přetrvávající a nové vady.
6. **Učitel rozhodne o finálním uložení do Gitu.** Předchozí kroky neopravňují ke commitu ani pushi.

Role jsou výchozí: na výslovný pokyn může kterýkoliv nástroj tvořit, opravovat či recenzovat. Platí stejná pravidla včetně schvalování testových úloh. Vlastní kontrola autora nenahrazuje nezávislou recenzi druhého nástroje.

Při recenzi se materiály ani PDF nemění, zapisují se protokoly. Nástroje současně neupravují stejné soubory; předávají práci přes učitele a protokol, druhý nástroj automaticky nespouštějí. Neprovedenou nebo nedostupnou nezávislou recenzi výslovně přiznej; vlastní kontrolu za ni nevydávej.

## Organizace projektu a tematické plány

Rozlišuj **centrální učebnici podle matematických oblastí** a **výukové materiály podle ročníků**:

- `ucebnice/`: společná učebnice pro SPŠ i gymnázium; kapitoly nekopíruj do ročníků, zachovej členění a názvy.
- `1_rocnik/` až `4_rocnik/`: vždy `tematicke_plany/`, `testy/`, `pracovni_listy/`, `pripravy/`. Testy a listy lze členit podle témat. Přípravy patří přímo do ročníkové složky `pripravy/`, tematické podsložky jen na přání učitele.
- `sablony/`: společné šablony testů, listů a příprav; nejprve ověř skutečný obsah a použití.
- `pravidla/`: pravidla výuky a hodnocení.
- `import_testu/`: pracovní kopie starších testů, opravných zkoušek a listů; **neověřený archiv**, nikoli schválená banka nebo šablony.
- `externi_zdroje/`: externí podklady pro inspiraci a porovnání, bez automatického oprávnění k převzetí či šíření. Pro `realisticky/` platí pravidla níže.
- `planovani/`: rozpracovanost, přehledy kontrol a `recenze/`. Kontrolní zpráva není zdrojem zadání ani schválením učitele.
- `scripts/`: technické kontroly a samostatný aktualizátor knihovny; kontrola materiálu nepovoluje aktualizaci zdrojů.
- `.agents/skills/`, `CLAUDE.md`, `.claude/`: pracovní postupy a integrace nástrojů; při tvorbě materiálu konfiguraci neměň.

Obsah a pořadí hodin určuje zadání učitele a schválený `N_rocnik/tematicke_plany/Rozpis_vyuky_MAT_N_rocnik.tex`. Ověř konkrétní řádek a okolí. Souhrnný rozpis v `sablony/pripravy/` ročníkový rozpis nenahrazuje.

V ročníkových `tematicke_plany/` jsou také `SPS.pdf` (společný pro strojírenské a informatické obory) a `GYM.pdf`. Relevantní dostupný plán prostuduj, zohledni návaznost a časovou dotaci. Názvy a pořadí témat neodvozuj z obecného kurikula. Rozdíly plánů nejsou nepřekročitelnou hranicí, zadá-li učitel jinak.

Učebnice, přípravy a listy mohou sloužit oběma školám; automaticky je nerozděluj podle SPŠ/GYM. O použití ve třídě rozhoduje učitel. Původní `~/ucebnice/` je archiv: bez výslovného pokynu jej neupravuj, nemaž ani nic neimportuj.

## Společná pravidla názvů a umístění

Cesty jsou relativní ke kořeni projektu, není-li uvedeno jinak. `N_rocnik`, `[NN]`, `<Tema>` apod. jsou vzory k dosazení, nikoli tvrzení o existenci souboru.

| Typ | Konvence |
|---|---|
| Učebnice | Zachovat tematickou strukturu, názvy a vazby v `ucebnice/`. |
| Příprava | `N_rocnik/pripravy/[NN]_[TTT]_[PopisnyNazev].tex`; číslo hodiny v ročníku. |
| Test | `N_rocnik/testy/<Tematicky_celek>/[cislo]_test_[nazev]_[varianty].tex`; viz pravidla testů. |
| Řešení testu | Vedle zadání, zpravidla stejný základ s `_reseni.tex`. |
| Pracovní list | `N_rocnik/pracovni_listy/`, podle tématu a místní konvence; univerzální název není zaveden. |
| PDF | Stejný základ jako hlavní `.tex`; u samostatného materiálu vedle něj. |
| Recenze | `planovani/recenze/`, název a ID podle tamního `README.md`. |

Nové názvy piš bez mezer, konzistentně s okolím. Testy bez diakritiky; u příprav respektuj zavedené zkratky a diakritiku. Kvůli sjednocení existující soubory nepřejmenovávej ani nepřesouvej. Číslo hodiny, pořadí testu v tématu a kód externí lekce nezaměňuj.

## Lokální knihovna Realisticky.cz

`externi_zdroje/realisticky/` je **lokální knihovna vyřazená ze sledování Gitem**. Codex i Claude Code ji mohou studovat a porovnávat s učivem; běžně je pouze ke čtení.

- Lekce vyhledávej v místním [KATALOG.md](externi_zdroje/realisticky/KATALOG.md), je-li dostupný. Není to projektový katalog vzorů; cesty ověř, nevymýšlej je ze starých komentářů.
- Čti skutečný obsah PDF, shodný název nestačí. Eviduj cestu, kód lekce a použité části či příklady; rozliš výklad, sbírku a nezkontrolovaný obsah. Externí číslování nemění náš rozpis.
- Extrakce textu může ztratit zlomky, odmocniny či absolutní hodnoty. Sporný zápis ověř obrazově; artefakt převodu není chyba zdroje.
- Bez příslušného oprávnění obsah **neredistribuuj**, nepřikládej k výstupům a nepřebírej rozsáhlé doslovné či téměř doslovné výklady nebo sady úloh. Existence PDF ani katalogový záznam nedokládají licenci k úpravám a šíření; podmínky nevymýšlej.
- **Úpravy, stahování a aktualizace vyžadují samostatné zadání.** Ani `scripts/aktualizuj_realisticky.py --offline` není pouhé čtení: přepisuje katalog a stav knihovny. Chybějící zdroj zaznamenej jako omezení, automaticky jej nestahuj.
- Zachovej vzor `/externi_zdroje/realisticky/` v `.gitignore`; neobcházej jej přes `git add -f`. Před přidáváním do Gitu ověř `git check-ignore -v externi_zdroje/realisticky/KATALOG.md` a prázdný výstup `git ls-files -- externi_zdroje/realisticky/`. Ignorování již sledované soubory neodstraní; rozpor oznam, index ani soubory automaticky hromadně neměň.
- V jiném klonu nemusí knihovna existovat. Nepřítomnost neřeš přidáním do Gitu; uveď dopad na kontrolu.

## Existující podklady a šablony

Před tvorbou či úpravou prohlédni související soubory, šablony, makra a vhodné vzory z `sablony/KATALOG_VZORU.md`. Ověřené skutečné soubory určují makra, rozvržení a návaznosti; ukázkový obsah nepřebíjí obsahová pravidla ani schvalování. Chybějící vzor přiznej, nevydávej domněnku za vlastnost projektu.

Zachovej členění, názvy a funkční kompilaci. Nevytvářej duplicitní šablony, adresáře či makra, stačí-li existující řešení; rozdíly šablon bez souhlasu plošně nesjednocuj. Nové testy vycházejí z aktuálního `sablony/testy/`; nedostupnost oznam. `sablony/pracovni_listy/` obsahující jen `.gitkeep` není funkční šablona.

## Autorský styl a matematické značení

Zachovej především autorův styl formátování LaTeXu: strukturu dokumentu, členění na odstavce, způsob zápisu rovnic, prostředí, odsazování a prostorové uspořádání. Druhotně zachovej styl vyjadřování. Upřednostňuj souvislý, plynulý a srozumitelný matematický výklad před zbytečným množstvím nadpisů, seznamů a vizuálních bloků. Při revizi měň jen to, co je nutné pro věcnou, jazykovou či didaktickou správnost.

Používej konzistentní českou matematickou terminologii, správnou symboliku a návaznost na dříve zavedené pojmy. Definice, tvrzení, důkazy a příklady rozlišuj podle vzorů projektu. Není-li doložena autorova volba, nevynucuj své oblíbené značení ani vlastní úpravu vzhledu.

## Učebnice

Centrální `ucebnice/` má oblasti od `01_Zakladni_poznatky/` po `11_Diferencialni_a_integralni_pocet/`. Respektuj samostatné kapitoly i propojené projekty. `ucebnice/07_Analyticka_geometrie/projekt/` je funkční projekt s `main.tex`, `preamble.tex` a soubory přes `\input`; bez zadání jej nerozděluj ani neměň vazby.

Přečti navazující části, zavedené pojmy a značení. Pokud dokument používá `ucebnice.sty`, prostředí `definition`, `example`, `solution` či `\historybox`, používej jejich skutečné definice a vzory. Ne každý dokument styl používá: respektuj vlastní preambuli, bez důvodu ji nepřepisuj a nepřidávej stylové balíčky. Nová kapitola nesmí být stylisticky izolovaná.

Výklad má být odborně přesný a přístupný středoškolákům: vysvětluj motivaci, podmínky a význam kroků, nepřeskakuj podstatné úvahy. Historické poznámky a citace musí mít doložitelný zdroj, nevymýšlej je.

### Zápis matematických výsledků v učebnici

V učebnici nepoužívej `\boxed{}` ani jiné rámečky pro konečné matematické výsledky. Rovnice, výrazy, výpočty a řešené příklady zapisuj běžně v `$...$`, `\[...\]`, `align` apod. podle okolí; výsledek lze uvést větou „Dostáváme …“, „Řešením je …“ či „Odtud vyplývá …“.

Zákaz se netýká autorských prostředí `definitionbox`, `examplebox`, `solutionbox`, `notebox` aj. pro strukturu učebnice. Staré `\boxed{}` nahraď standardním zápisem v právě upravované části, nikoli v nesouvisejících kapitolách.

## Testy: umístění, pojmenování a šablony

Nové testy ukládej do `N_rocnik/testy/<Tematicky_celek>/` podle skutečného učiva a struktury. **Nezakládej automaticky složku pro každý test**: varianty patří vedle sebe do tematické složky. Další podadresář musí mít konkrétní důvod.

Pro každý nový test je závazná konvence:

`[cislo]_test_[nazev]_[varianty].tex`

Například `01_test_ExponencialniRovnice_AB.tex`, `01_test_ExponencialniRovnice_CD.tex` nebo `02_test_ExponencialniRovnice_GH.tex`. Číslo je dvojciferné, začíná obvykle `01` a vyjadřuje pořadí testu **v rámci konkrétního tématu**, nikoliv celého školního roku. Hodnotu `00` použij jen záměrně (např. vstupní diagnostika). V nových názvech souborů používej názvy témat bez diakritiky a mezer; zachovávej konzistentní zápis. Soubor je pojmenován podle skutečných variant uvnitř, nikoliv podle předpokladu.

**Každá dvojice variant má vlastní samostatný `.tex` soubor:** `AB`, `CD`, `EF`, `GH`, `IJ`, `KL`. Soubor s příponou `_AB.tex` obsahuje variantu A i B, `_CD.tex` obsahuje C i D atd. Neslučuj více dvojic do jednoho souboru; nevytvářej nepožadované dvojice. Pokud se zadává pouze jedna varianta, postup pojmenování domluv s učitelem, místo abys druhou automaticky vytvářel.

V `sablony/testy/` se používají dva výchozí typy šablon, **pokud jsou skutečně přítomné a funkční**:

- `A5x2.tex`: A4 na šířku se dvěma testy velikosti přibližně A5 vedle sebe, obvykle jedna varianta v každé polovině. Vhodné pro kratší testy a desetiminutovky.
- `A4.tex`: A4 na výšku, vhodná pro rozsáhlejší písemky; dvojice variant může zabírat samostatné stránky.

Po schválení konkrétní skladby úloh **vytvoř nový samostatný soubor z vhodné existující šablony**. Zachovej rozvržení, makra a hlavičku, nezadá-li učitel změnu; originální šablonu neupravuj. Hlavička obsahuje jméno a příjmení, třídu, datum a prázdná pole „Počet bodů“ a „Známka“ (nejde o bodování zadání). Ukázkové úlohy nejsou matematicky ověřené: nahraď je schválenými a ověřenými. Staré testy z `import_testu/` mechanicky neopisuj.

**V žákovském zadání nikdy automaticky neuváděj bodové hodnoty úloh ani podúloh, celkový maximální počet bodů, klasifikační stupnici ani procentní hranice známek. Jedinou výjimkou je výslovný pokyn učitele.** Zákaz platí pro všechny varianty A–L, všechny formáty A4/A5 a všechny typy běžných písemných testů, včetně textů a údajů převzatých ze šablony.

Řešení a výsledky ulož odděleně vedle testu nebo podle dohody, s jednoznačným přiřazením k variantám. Bez pokynu nepatří do tiskové žákovské verze. Samostatné řešení obsahuje postupy a výsledky; orientační bodovací schéma **jen na výslovnou žádost**. Vyžádané bodování je nezávazný návrh, učitel jej i kritéria uznávání postupů může při opravování odborně upravit.

## Testy: obtížnost a zadávání

Výchozí stupnice obtížnosti je následující:

- **A/B:** SPŠ, základní úroveň, zpravidla řádný termín.
- **C/D:** SPŠ, zvýšená obtížnost, často dopisování nebo oprava.
- **E/F:** SPŠ, vysoká obtížnost, často další dopisování nebo oprava; zpravidla těžší než C/D.
- **G/H:** gymnázium, základní gymnaziální úroveň, zpravidla řádný termín.
- **I/J:** gymnázium, velmi vysoká obtížnost, často dopisování nebo oprava.
- **K/L:** gymnázium, mimořádně náročná úroveň, často další dopisování nebo oprava; zpravidla těžší než I/J.

Platí dvě samostatné posloupnosti obtížnosti: **A/B < C/D < E/F** a **G/H < I/J < K/L**. Gymnaziální úlohy obvykle vyžadují větší míru abstrakce, propojování poznatků nebo důkazu. Nesrovnávej mechanicky každou dvojici napříč školami a nepovažuj přiřazení k typu školy za zákaz použití jiné varianty v konkrétní třídě. Konkrétní požadavek učitele má přednost před výchozí konvencí.

Obtížnost musí primárně odpovídat konkrétním úlohám a rozsahu učiva schváleným učitelem. Samotné označení varianty neopravňuje k použití extrémně náročných, olympiádních či mezioborových úloh. Nevybírej automaticky nejtěžší příklady z učebnice jen proto, že jde o variantu E/F nebo K/L.

Vyšší obtížnost vybírej v rámci schválených úloh zejména podle náročnosti matematické úvahy, souvislostí a vícefázového řešení, nikoli jen podle větších čísel, zbytečně dlouhých výpočtů či nepřiměřeného množství úloh. I opravné a náhradní termíny musí ověřovat stanovené učivo, být řešitelné v přiměřeném čase a odpovídat požadovanému hodnocení. **Varianty uvnitř jedné dvojice** musí mít srovnatelnou obtížnost, časovou náročnost a rozsah; pokud učitel požaduje bodování, také srovnatelné bodovací schéma. Různé úlohy mohou testovat stejné dovednosti; označení varianty neopravňuje ke změnám zadání.

**Opravná zkouška za pololetí či celý školní rok není automaticky další variantou běžného testu.** Zacházej s ní jako se samostatným typem dokumentu, který může mít odlišnou strukturu a rozsah. Starší zkoušky v `import_testu/opravne_zkousky/` jsou pouze neověřeným podkladem.

Nepřidávej kalkulačku, tabulky ani jiné pomůcky, pokud jejich použití nebylo povoleno. Jestliže chybí informace zásadní pro zadání testu (například rozsah látky, délka testu nebo povolené pomůcky), vyžádej si je před tvorbou.

### Výběr úloh pro testy

Pokud učitel určí konkrétní úlohy, vyhledej je a prostuduj jejich zadání, řešení a používané matematické postupy. Jeho výběr má přednost; nepředkládej jej znovu ke schválení a pokračuj podle jeho pokynů.

Při vyhledávání úloh povinně čerpej přednostně z existujících konkrétních příkladů v tomto pořadí:

1. Příslušné kapitoly v `ucebnice/`.
2. Pracovní listy v `N_rocnik/pracovni_listy/`.
3. Další konkrétní materiály určené učitelem.
4. Starší testy v `import_testu/` pouze jako pomocné a neověřené podklady.

Pokud existuje vhodný příklad v učebnici nebo pracovním listu, použij jej jako výchozí zdroj. Nevymýšlej automaticky nové typy příkladů ani vlastní zadání pouze podle názvu tematického celku. Tvorba nových úloh vyžaduje výslovné povolení učitele; pokud vhodné podklady nenajdeš, sděl to a vyžádej si další podklady nebo pokyn k tvorbě.

U každé vybrané úlohy zaznamenej původ: přesnou cestu k souboru a číslo úlohy nebo jinou jednoznačnou identifikaci původního zadání. Zdrojové informace ukládej do interního přehledu nebo dokumentu pro učitele, nikoliv automaticky do žákovského zadání. U výslovně povolených nových úloh zaznamenej, že jde o vlastní tvorbu; u obdobných úloh eviduj také zdrojový vzor a povolené úpravy.

Pokud učitel zadá pouze téma testu nebo jinak neurčí konkrétní úlohy, nesmíš sám rozhodnout o konečné skladbě. Nejdříve prostuduj dostupné zdroje a předlož návrh obsahující:

- konkrétní vybrané úlohy;
- přesné odkazy na jejich zdroje;
- stručný popis požadovaného matematického postupu;
- orientační obtížnost;
- předpokládanou časovou náročnost;
- návrh přiřazení k jednotlivým variantám.

**Finální `.tex` a PDF sestav až po schválení konkrétního výběru učitelem.** Samotné zadání tématu, označení variant nebo povolení vlastní tvorby nenahrazuje schválení konkrétní skladby; učitelem přímo určené úlohy se znovu neschvalují.

Při převzetí existujícího příkladu zachovej jeho matematický obsah. Bez výslovného pokynu učitele neměň číselné hodnoty, matematické výrazy, parametry, podmínky, požadované postupy ani obtížnost. Požaduje-li učitel obdobnou úlohu, můžeš upravit konkrétní hodnoty při zachování požadovaného matematického postupu a srovnatelné náročnosti. Nezaváděj jiné, dosud neprobrané znalosti, pokud je učitel výslovně nepožaduje.

Každou převzatou, nově vytvořenou i upravenou úlohu matematicky ověř podle části „Matematická kontrola“. Existence úlohy v učebnici, pracovním listu či starším testu není zárukou správnosti. Zjistíš-li chybu ve schváleném zadání, upozorni učitele a vyžádej si pokyn k opravě nebo náhradě; neměň matematický obsah svévolně.

## Pracovní listy

Pracovní listy ukládej do `N_rocnik/pracovni_listy/` a dále podle tématu; používej společné šablony ze `sablony/pracovni_listy/`, pokud existují. Vycházej z probíraného tématu a úrovně žáků. Pokud uživatel neurčí jinak, řaď úlohy od základního porozumění přes běžné procvičení po náročnější aplikace. U listů určených k vyplňování ponechávej přiměřené místo na výpočty, zápis nebo náčrtek; u vzorových listů respektuj jejich dosavadní úspornou sazbu. Pro grafy a geometrické obrázky používej přednostně zavedené nástroje projektu (například TikZ či pgfplots), pokud jsou vhodné. Výsledky a řešení udržuj oddělené od žákovské verze, není-li zadáno jinak. Staré pracovní listy v `import_testu/` nejsou automaticky obsahově ověřené.

## Přípravy na hodiny

Závazný standard pro `1_rocnik/pripravy/` až `4_rocnik/pripravy/`; technické ukázky jsou v `sablony/pripravy/TUTORIAL_pripravy.md`.

1. **Přečti podklady:** `AGENTS.md`, tutorial, `sablony/pripravy/TEMPLATE_Priprava.tex`, `sablony/pripravy/priprava.sty` a související okolní přípravy. Chybějící soubor bez důvodu nenahrazuj.
2. **Pořadí výuky:** vycházej ze zadání učitele, schváleného rozpisu, ročníkového plánu a okolních hodin. Cizí učebnice neurčuje naše číslování. Rozpor oznam, jiné hodiny sám nepřečíslovávej.
3. **Název:** přímo `N_rocnik/pripravy/[NN]_[TTT]_[PopisnyNazev].tex`, např. `02_VRL_CoJeVyrok.tex`, `01_ÚVD_ÚvodníHodina.tex`. `NN` je hodina v ročníku (1–9 s nulou, od 100 tři číslice), `TTT` trojpísmenná zkratka tématu. Existující názvy zachovej.
4. **Styl:** `\input{../../sablony/pripravy/priprava.sty}` a `\nastavPripravu{ročník}{globální téma}{číslo}{název}`. Cesta platí z adresáře `.tex` při kompilaci přímo v ročníkovém `pripravy/` (např. `latexmk -cd`); při jiné hloubce ji přepočítej. Makra a rámečky neduplikuj lokálně.
5. **Záhlaví a struktura:** vlevo „ročník | globální téma“, vpravo „číslo: název hodiny“. Nepřidávej úvodní metadatovou hlavičku, zápatí, povinné cíle ani minutový rozpis. Použij jen potřebné oddíly: motivaci, definice, výklad, příklady, procvičení, poznámky.
6. **Boxy:** každý samostatný pojem definuj v odděleném `definiceBox`. Zadání bez řešení patří do `prikladBox` či `zadaniBox`; s řešením do `prikladReseniBox` či `zadaniReseniBox` s právě jedním `\tcblower`. Nahoře zadání, ve světle šedé spodní části řešení; víceřádkový výpočet v `align*` apod. uvnitř řešení. Nepřipojuj druhý rámeček a v nových dokumentech nepoužívej zastaralé `\reseni{}`.
7. **Poznámky:** `\poznamka{...}` šedě mimo boxy; volitelné mezititulky `\blok{...}`. Příkazy ověř ve stylu. Při rozporu technických ukázek rozhoduje funkční `priprava.sty`; rozpor oznam, sdílené soubory svévolně nepřepisuj.
8. **Obsah:** čeština, přesnost, návaznost, gradace a odlišený základ od rozšíření. Příprava není žákovský pracovní list. Ověř každé zadání i řešení; přeplněnou hodinu oznam.
9. **Zdroje:** učebnice, vlastní listy a dostupné externí podklady podle části „Lokální knihovna Realisticky.cz“. Skutečně použité zdroje eviduj v komentářích `.tex` nebo interním přehledu, ne automaticky v zápatí. Nevymýšlej odkazy a nepřečtené lekce neoznačuj za ověřené.
10. **Sestavení a rozsah:** použij postup v části „Kompilace a kontrola výstupu“, např. `./scripts/build_latex.sh 1_rocnik/pripravy/02_VRL_CoJeVyrok.tex`. Zadání jedné hodiny neopravňuje měnit jiné přípravy, osnovy, sdílený styl ani `AGENTS.md`.

### Didaktická kvalita a čas přípravy

Běžná příprava má při svižnějším tempu nabízet **40–50 minut základního výkladu a procvičování**, označenou volitelnou rezervu a **10–20 minut domácího procvičování s výsledky či řešením**, není-li zadáno jinak. Pro obvykle 45minutovou hodinu při přesahu označ příklady k výběru či dokončení doma. Rezerva není povinnou součástí součtu; mírný přesah nabídky není automatická vada. Nezvládnutelný povinný obsah oznam.

Odhadni zvlášť výklad, pokus žáků, společnou kontrolu, rezervu a domácí práci. Počet stran, řádků či rychlost učitele nestačí; jde o odhad, nikoli měření. Minutový harmonogram nemusí být vytištěn. U testovacích a organizačních hodin zachovej odlišný účel.

Dobré části nepřepisuj. Doplň konkrétní chybějící pojmy, podmínky, zdůvodnění, souvislosti a názorné modely; nepřidávej téměř stejné úlohy jen kvůli rozsahu. Graduj od porozumění po aplikaci, obtížné důkazy a zajímavosti odděl od základu. Vysvětli platnost úprav. U diagramů používej zavedené nástroje a rozliš konkrétní obrázek od obecného tvrzení.

### Evidence dokončených příprav

Respektuj `planovani/STAV_PRIPRAV.md` a rozpis výuky. Po dokončení tematického celku ověř jeho úplnost a aktualizuj stav. `HOTOVO` vyžaduje všechny přípravy celku včetně `.tex` a `.pdf`. Nevytvářej záznamy pro celky neuvedené v tematických plánech.

## Matematická kontrola

Ověř každé zadání i řešení: definiční obor, předpoklady, ekvivalenci úprav, výpočty, jednotky, grafy a jednoznačnost otázky. Kde je praktické, použij nezávislou metodu (dosazení, symbolický či numerický výpočet, krajní případy, jiný postup). Opakované přečtení stejného řešení není nezávislé ověření. Neprovedenou kontrolu výslovně přiznej.

Zahrň i rezervní a domácí úlohy a výsledkové položky. Vytištěný výsledek porovnej přímo s doslovným zadáním a vlastním výpočtem, ne jen s navazující kontrolou. Konečně mnoho souhlasných dosazení nedokazuje identitu; protipříklad musí patřit do původního oboru. „Bez zjištěné chyby v uvedeném rozsahu“ není záruka ani schválení učitelem.

U testů **ověř každou variantu samostatně**, včetně existence a úplnosti řešení, času a vyžádaného bodování. Nezávislá kontrola platí pro převzaté, nové i upravené úlohy a řešení; předchozí výuka není důkaz správnosti.

Před označením testu za hotový ověř:

1. Zdroje jsou schválené, případná vlastní tvorba výslovně povolená.
2. Úlohy lze dohledat podle evidence; vlastní tvorba je označena, obdobné úlohy mají zdrojový vzor.
3. Zadání i rozdělení variant odpovídají schválenému či přímo určenému výběru.
4. Žádná úloha nebyla změněna mimo výslovné zadání.
5. Žákovský test včetně výsledného PDF a textů šablony neobsahuje nevyžádané body úloh/podúloh, maximum bodů, stupnici ani procentní hranice známek. Jejich nepřítomnost výslovně zkontroluj; výjimkou je učitelův výslovný požadavek.
6. Hlavička zachovává prázdná pole „Počet bodů“ a „Známka“.
7. Dvojice má přibližně srovnatelnou obtížnost, čas, rozsah a případné vyžádané bodování.
8. Každé zadání a řešení včetně všech úprav bylo nezávisle ověřeno.
9. PDF bylo zkompilováno a vizuálně zkontrolováno podle části „Kompilace a kontrola výstupu“.

Pokud některou kontrolu nelze dokončit, uveď konkrétní omezení a test neoznačuj za hotový.

## Nezávislá recenze a předávání nálezů

Recenzent nejprve posoudí materiál sám; lze-li zadání bezpečně oddělit, řeší je bez autorských výsledků. Zprávy autora a jiných recenzentů čte až ke srovnání po vlastním závěru. Cílené ověření oprav smí vycházet z dřívějších nálezů, musí však být takto označeno.

Každá recenze zaznamená:

- soubory, varianty, úlohy, datum, větev, HEAD, Git stav a obsahové otisky kontrolovaných zdrojů, PDF a řešení;
- skutečně provedené matematické, didaktické, časové, zdrojové a vizuální kontroly včetně nezávislé metody;
- u nálezu ID, místo (soubor, úloha, řádek či strana), popis, důkaz nebo zdůvodnění, závažnost, minimální návrh opravy a stav;
- odděleně prokázané chyby, nejednoznačnosti, doporučení a neověřené podněty; neshodu hlášení s aktuálním souborem ověří před zápisem;
- omezení: nedostupné podklady, neprovedené kontroly, neprohlédnuté strany, nejistý čas. Čistý Git ani čas změny nejsou důkazem shody PDF se zdrojem.

O nálezech rozhoduje učitel, recenzent je automaticky neopravuje. Výslovně zadaná konkrétní oprava již schvaluje její rozsah: nevyžaduj totéž podruhé. Opravu předej s ID, změněnými cestami a výsledky kontrol; změny nad schválený rozsah odděl k rozhodnutí.

Zachovej historii nálezů a opravovanou verzi identifikuj otiskem pracovní kopie nebo existujícím commitem. Commit není podmínkou recenze, opravy ani ověření. ID, názvy a stavy určuje pouze [recenzní protokol](planovani/recenze/README.md), techniku Claude Code jeho vlastní dokumentace.

## Kompilace a kontrola výstupu

Po autorizované tvorbě či změně samostatné přípravy, testu nebo listu používej dostupný funkční skript z kořene projektu:

```bash
./scripts/build_latex.sh cesta/k/dokumentu.tex
```

Provádí základní kontrolu struktury, kompilaci a technické ověření PDF; **PDF musí být vedle zdrojového `.tex`**, pomocné soubory mimo materiály. Selhání vyšetři a oznam, nezakrývej je neohlášeným jiným postupem. Pokud skript chybí, použij zavedený překladač a nastavení, např. `latexmk -cd -pdf -interaction=nonstopmode -halt-on-error <cesta.tex>`.

Skript nepoužívej automaticky na dílčí kapitoly přes `\input` ani projekty se zvláštním sestavením. Respektuj VS Code/LaTeX Workshop a případnou cestu k `ucebnice.sty`; nepřepisuj kvůli ní jednotlivé preambule.

Zkontroluj log, chyby a významná varování. Vizuálně prověř všechny relevantní strany: diakritiku, matematickou sazbu, přetékání, grafy, rozvržení a tiskovou čitelnost. U `A5x2` ověř obě varianty na jedné A4 bez vzájemného zásahu. Neprovedenou vizuální kontrolu přiznej. Uveď vzniklé soubory a výsledek kompilace.

Při recenzi pouze pro čtení sestavení nespouštěj: přepisuje PDF. Lze samostatně použít `scripts/check_structure.py`, `scripts/verify_pdf.py` a zobrazit existující PDF; pochybnosti o aktuálnosti zaznamenej. Vykreslení a diagnostiku ukládej mimo materiály, např. do dočasného adresáře. Automatické kontroly jsou heuristické: neprokazují matematiku, sazbu, srovnatelnost variant ani shodu PDF se zdrojem; nenahrazují jejich kontrolu.

## Bezpečnost, Git a rozsah změn

Pracuj v určeném projektu a podle oprávnění. Bez výslovného souhlasu nemaž či hromadně nepřesouvej soubory, nepřepisuj sdílené šablony a nepřidávej systémové nástroje či závislosti. Osobní údaje žáků, přístupové údaje a klíče neotevírej ani nezveřejňuj mimo nezbytnou výslovně zadanou bezpečnou operaci.

Před prací zkontroluj `git status` a relevantní diff. Zachovej existující i nesledované uživatelské změny. K čištění stromu automaticky nepoužívej `git reset`, `git restore`, `git clean`, přepis historie, mazání ani hromadné přesuny. Změny drž malé, nepřeformátovávej okolí; před rozsáhlou úpravou předlož krátký plán.

**Commit ani push bez výslovného zadání neprováděj.** Před commitem ukaž změny, vyber jen dohodnuté soubory, ověř připravený diff a ignorování knihovny; nepřidávej neuváženě celý projekt. Souhlas s materiálem či opravou není souhlasem s Gitem; commit a push jsou samostatná rozhodnutí.

Zachovej konfiguraci nástrojů, oprávnění a import `@AGENTS.md`, není-li jejich úprava výslovně zadána. Po práci shrň změny, matematické ověření, kompilaci, vizuální kontrolu a omezení; neprovedené kontroly označ.

## Referenční materiály

Při tvorbě příprav, testů a listů použij podle potřeby `sablony/KATALOG_VZORU.md`: doporučuje vzory, nenahrazuje závazné šablony ani pravidla. Rozliš schválené reference od neověřených ukázek; ukázka není zárukou správnosti.
