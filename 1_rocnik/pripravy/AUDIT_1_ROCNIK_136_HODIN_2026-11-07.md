# Audit příprav matematiky – 1. ročník SPŠ (1–136)

**Datum kontroly:** 7. 11. 2026  
**Repozitář:** [Werdna09/Work-MAT](https://github.com/Werdna09/Work-MAT)  
**Kontrolovaná větev:** `main`  
**Výchozí commit:** `da2544eae794c64c2d264bf4b31cba007db083a7` („Hotový první ročník“, 7. 11. 2026)  
**Rozsah:** aktuální `.tex` soubory v `1_rocnik/pripravy/`, soupis PDF a pracovních listů, společná šablona a aktuální textový rozpis hodin.  
**Charakter:** **nálezový a implementační report; zdrojové soubory nebyly změněny**.

> **Jak číst hodnocení:** Kontroloval jsem skutečné zdrojové texty všech hodin a jejich strukturu (boxy, označení, domácí části, pedagogické poznámky), podrobněji vybrané rizikové výklady a ukázkové matematické výpočty. **Nejde o úplný přepočet všech příkladů ani vizuální kontrolu každé stránky všech 136 PDF.** „Bez obsahového nálezu“ znamená pouze, že rychlý audit neodhalil konkrétní problém, nikoli stoprocentní matematickou certifikaci.

## 1. Výkonný souhrn

**Učivo je sestavené pro všech 136 hodin; repozitář ale ještě není finálně unifikovaný.** Doporučuji jednu závěrečnou revizi. Neznamená to předělat všechna zadání – naprostá většina práce je sazba, pojmenování, organizační úklid a několik konkrétních metodických doplnění.

| Oblast | Výsledek |
|---|---|
| Hodiny **1–136** | **136/136 čísel hodin má svůj zdrojový `.tex`** v `1_rocnik/pripravy/`. |
| Obsah adresáře `pripravy/` | **142 `.tex`, 142 `.pdf`, 1 `.gitkeep`** – šest čísel hodin se objevuje u více zdrojových souborů (část jsou záměrné bonusy nebo pracovní listy). |
| Párování názvů `.tex`/`.pdf` | **Dvě `.tex` bez stejně pojmenovaného PDF a dvě PDF bez stejně pojmenovaného `.tex`**; podrobnosti níže. |
| Šablona | Existuje jedna společná `sablony/pripravy/priprava.sty`; boxy `definiceBox`, `prikladReseniBox`, `zadaniReseniBox` jsou zavedené. |
| Označení boxů | **Nesjednocené.** Vyskytují se `P1`, `S1`, `R1`, `D1`, `V1`, `Příklad 1: název`, `Úloha 1`, výchozí `Zadání` i box bez čísla. |
| Domácí úkoly | Většina novějších příprav už má jeden společný seznam, ale používá jiné nadpisy (`Domácí procvičení`, `Domácí příprava`, `Domácí úkol`) a starší části mají `D1` či samostatně titulované bloky. |
| Vysvětlení učiva | Návaznost hlavních celků je dobrá; zdrojové texty obsahují výklad, vzory, samostatnou práci a typicky i rezervu. Jsou však konkrétní místa k doplnění. |
| Poznámky pro učitele | Jsou přítomné ve většině vlastních příprav. **Kvalita a hloubka kolísá**: ve starších hodinách bývají bohatší; v některých novějších je jediná poznámka převážně časovým rozvrhem. |
| Tematický rozpis | **Nesouhlasí s aktuálními hodinami** především od 71/72 a zásadně od 93/96 do konce roku. |
| Matematická / sazební chyba | **Potvrzená chyba ve vysázení odmocňování v hodině 103** (níže). |

### Rozhodnutí před opravami

- **Nezměnit původní zadání ani jejich výsledky** jen kvůli typografii. Zachovat řešení, postupy, grafy, zdroje a počet příkladů.
- **Nevytvářet zadání testů.** Testové přípravy slouží organizačně; testy jsou u učitele mimo repozitář.
- **Zachovat bonusovou 85A**, ale nepovažovat ji za povinnou 137. hodinu; v rozpisu musí být zřejmé, že může nahradit jinou hodinu.
- Hodiny **130–136 jsou podle posledního zadání opakovací**, nikoli testy. Se starším rozpisem je to vědomý nesoulad, který je nutné vyřešit v rozpisu a v systému hodnocení, nikoli zpětným přepsáním těchto příprav.
- Soubory na GitHub **nebude asistent pushovat**. Opravené `.tex` a `.pdf` předat po etapách; vlastník provede kontrolu a nahrání.

---

## 2. Konkrétní problémy v repozitáři – odstranit před plošnou revizí

### R01 · P0 – Tematický rozpis není synchronizovaný

**Soubor:** `1_rocnik/tematicke_plany/Rozpis_vyuky_MAT_1_rocnik.tex`.

| Hodina | Aktuální `.tex` příprava | Starý rozpis uvádí |
|---|---|---|
| 71 | Grafy se dvěma absolutními hodnotami | Samostatné procvičování lineárních funkcí |
| 85 | Obecná eliminace soustav (+ volitelná 85A) | Smíšené lineární rovnice s parametrem |
| 86 | Průběžný test I | Lineární nerovnice |
| 93 | Aplikační slovní úlohy napříč obory | Kombinované procvičení lineárních rovnic a nerovnic |
| 96 | Úvod do kvadratické funkce | Vyjádření neznámé z technického vzorce |
| 103 | Neúplné kvadratické rovnice | Úvod do kvadratické funkce |
| 124 | Grafy kvadratických funkcí s absolutními hodnotami | Kvadratická nerovnice řešená graficky |
| 125 | Rovnice v podílovém tvaru | Kvadratická nerovnice znaménkovou metodou |
| 130 | Opakování logiky a množin | Test T8 |
| 135 | Matematika v praxi | Pololetní práce P4 |

**Doporučení:** Ze skutečných 136 příprav sestavit *nový* tabulkový rozpis 1–136 a pak jej porovnat s oficiální dotací a plánovaným počtem písemných prací. **Nesnažit se vracet přípravy k zastaralému rozpisu.** Do vyřešení nesouladu neoznačovat počet testů za administrativně finální. Případné písemné práce domlouvat samostatně.

### R02 · P0 – Nevyužité či duplicitní soubory mezi učitelskými přípravami

Adresář `pripravy/` by měl obsahovat **jednu hlavní přípravu na číslo hodiny**; pomocné materiály patří do `pracovni_listy/` (výjimkou je jednoznačně označená dobrovolná 85A).

| Číslo | Soubory v `pripravy/` | Zjištění / doporučený postup |
|---|---|---|
| 27 | `27_MOC_KISS_ProcvicovaniMocnin.tex`; `27_MOC_TabulkaReckychPismen.tex` | Druhý soubor je pomocná tabulka, nikoli druhá příprava. Přesunout/vést jako pracovní materiál, nepočítat jako další hodinu. |
| 39 | `39_MOC_PripravaNaTestATypickeChyby.tex`; `39_MOC_PracovniList_Procvicovani_120.tex` | Druhý je pracovní list a existuje i v `pracovni_listy/` se **stejným Git SHA**. V `pripravy/` ponechat jen učitelskou přípravu. |
| 71 | `71_FNC_GrafySeDvemaAbsolutnimiHodnotami.tex`; `71_FCE_DveAbsolutniHodnoty.tex` | Druhý je žákovský pracovní list, zároveň v `pracovni_listy/` (stejný SHA). V `pripravy/` jej zrušit jako duplicitu; navíc odkazuje na `../../../sablony/…`, což odpovídá jiné hloubce adresáře. |
| 85 | `85_SOU_EliminaceNN.tex`; `85A_MAT_MaticeAUvodDoGaussovyEliminace.tex` | **Nejde o chybnou duplicitu:** 85A je výslovně volitelný bonus. Zachovat a dokumentovat. |
| 93 | `93_APL_AplikacniSlovniUlohy.tex`; `93_APL_VyjadreniNeznameZeVzorce.tex` | **Skutečná stará varianta** vedle schválené aplikace; starý soubor nemá párové PDF. Archivovat/mimo `pripravy/` odstranit po kontrole, že nejde o cíleně uchovanou historickou verzi. |
| 95 | `95_OPA_SouhrnneProcvicovani.tex`; `95_SB_RovniceNerovniceSoustavy.tex` | Druhý je žákovská sbírka, totožná se souborem v `pracovni_listy/` (stejný SHA). V `pripravy/` ponechat jen učitelskou přípravu. |

**Nepárové soubory v `pripravy/`:** `.tex` bez identicky pojmenovaného PDF: `27_MOC_TabulkaReckychPismen`, `93_APL_VyjadreniNeznameZeVzorce`; PDF bez identicky pojmenovaného `.tex`: `39_MOC_PracovniList_ZadaniProZaky`, `71_FNC_ProcviceGrafuAVlastnosti`. U pracovních materiálů se může jednat o legitimní různá jména exportů; smyslem auditu je jejich **přemístění a dohledatelnost**, ne nutně mazání PDF.

### R03 · P0 – Konkrétní chyba sazby v hodině 103

V `103_KVR_NeuplneRovniceI.tex` jsou v úvodní ukázce

```latex
\begin{aligned}
x^2&=9\
|x|&=3\
x&=-3\quad\text{nebo}\quad x=3,\qquad K=\{-3;3\}.
\end{aligned}
```

**za prvními dvěma řádky jen jednotlivá zpětná lomítka `\`, nikoli LaTeXové `\\`.** Skutečně jsem ověřil také odpovídající výstupní PDF: výrazy `x² = 9`, `|x| = 3` a kořeny se v PDF **slily do jednoho řádku**. Nejde o didaktické zkrácení, ale o chybně vysázený postup.

Opravit na jednotlivé řádky `aligned` a znovu zkompilovat. Zachovat důležité sdělení `\sqrt{x^2}=|x|` a zápis `K=\{-3;3\}`.

### R04 · P1 – Historické názvy a mezníky v testových hodinách

Testy **10, 21, 40, 57, 69, 86, 94, 110, 121** mají různě podrobnou organizační přípravu. To samo o sobě není chyba. Hodiny **110 a 121** mají záměrně jen organizaci a učitelskou poznámku; podle dohody **nezadávat jejich varianty A/B**. Revize má pouze sjednotit hlavičky a popis rozsahu podle skutečně probraného učiva.

---

## 3. Cílový závazný standard boxů

Po finální revizi musí být **viditelná záhlaví výukových boxů přesně tato**:

| Typ | Požadovaný titulek | Číslování |
|---|---|---|
| Definice | **`Definice`** | Bez čísla. Každý samostatný matematický pojem má svůj box. Název pojmu může být tučně v obsahu boxu. |
| Společně řešený příklad | **`Příklad 1`**, `Příklad 2`, … | Průběžně od 1 v rámci hodiny; **bez vysvětlujícího podtitulu v záhlaví**. |
| Samostatné řešení | **`Samostatná práce 1`**, `Samostatná práce 2`, … | Průběžně od 1 v rámci hodiny; u jednoho boxu s více podúlohami použít `a)`, `b)`, … |
| Výběrová rezerva | **`Rozšíření 1`**, `Rozšíření 2`, … | Číslovat zvlášť. V metodické poznámce uvést, že je dobrovolná. |
| Domácí příklady | **`Domácí úkol`** | **Jediný box bez čísla.** Zadání uvnitř `a)`, `b)`, …; po `\tcblower` stejný počet odpovídajících řešení. |

**Pozor na dvojitý nadpis:** Současná šablona nastavuje `zadaniReseniBox` na výchozí `Zadání` a `prikladReseniBox` na `Příklad`. Při změně titulků lze použít `title={...}` v konkrétních přípravách; **neměnit globální vzhled** šablony, pokud to není nutné. Je-li už nadpis `\blok{Domácí úkol}`, nevyrob další opticky stejný nadpis přímo nad boxem – vybrat jeden jednotný způsob a použít jej všude. Pro požadavek „Domácí úkol je jeden box“ doporučuji ponechat právě box s titulkem `Domácí úkol` a samostatný duplicitní `\blok` odstranit.

### Co musí zmizet ze záhlaví boxů

- `P1`, `P2`, `S1`, `R1`, `D1`, `V1`, `D0`, `P3b` a jejich rozvedené varianty.
- `Příklad 1: kladný jednočlen`, `Příklad 2 – sbírka č. 31d`, `Úloha 1 – …`, `Foto 1 – 4j` apod.
- `Zadání` tam, kde jde o samostatnou práci; samotná matematická formulace zadání uvnitř boxu samozřejmě zůstává.
- `Domácí příprava`, `Domácí procvičení`, `D1` jako různé konkurenční názvy stejné kategorie.

**Popisný titulek nepřijít o obsah:** například informaci „pozor na záporný koeficient“ přesunout do krátké `\poznamka{...}` nebo úvodu před příkladem; text `Příklad 2 – název` není vhodné jen bez rozmyslu zahodit, pokud pomáhal výuce.

**Řešení:** středově vysazené pomocí `\[\begin{aligned}…\end{aligned}\]` nebo `align*`, s rovnítky pod sebou; vždy věcně správné množiny `K`, české intervaly, uspořádané dvojice `[x;y]`; žádné `\boxed`. U geometrických konstrukcí a úloh bez množiny kořenů se `K` samozřejmě nevynucuje.

### Jediný domácí box – ukázka (jen šablona)

```latex
\begin{zadaniReseniBox}[title={Domácí úkol}]
\begin{enumerate}[label=\alph*)]
  \item $2x-3=7$.
  \item $3(x-1)=12$.
\end{enumerate}
\tcblower
\begin{enumerate}[label=\alph*)]
  \item \[\begin{aligned}2x-3&=7\\x&=5\\K&=\{5\}\end{aligned}\]
  \item \[\begin{aligned}3(x-1)&=12\\x-1&=4\\x&=5\\K&=\{5\}\end{aligned}\]
\end{enumerate}
\end{zadaniReseniBox}
```

Ukázková zadání **nesmí nahrazovat** existující úlohy při automatickém sjednocování.

---

## 4. Audit stylů podle skutečných souborů

### 4.1 Starší generace (`P1`, `S1`, `R1`, `D1`)

Výrazně se vyskytuje zejména v **05–26** a v části **28–46**, včetně příprav:

- `05_CIS_PrirozenaACelaCisla.tex` – `P1`, `V1–V3`, `P2–P3`, `S1–S2`, `R1–R2`, `D1`.
- `06_CIS_RacionalniCislaAZlomky.tex` – obdobné kombinace.
- `07_CIS_RealnaCislaAZaokrouhlovani.tex`, `08_CIS_Intervaly.tex`, `09_CIS_AbsolutniHodnota.tex` – `P1` a další zkratky.
- `12_MNZ_MnozinaAJejiPrvky.tex` – `Příklad 1: …` i `D1`.
- `13_MNZ_PodmnozinaARovnostMnozin.tex` až `20_MNZ_OpakovaniMnozinAIntervalu.tex` – `P1`, `S1`, `R1`, `D1`; místy i `D0` a `P3b`.
- `22_GON_PravouhlyTrojuhelnikAPomery.tex` až `26_MOC_SoucinAPodilMocnin.tex` – staré zkratky.
- `28_MOC_CelociselnyExponent.tex` až `31_MOC_RacionalniExponent.tex` – `Příklad 1: název`.
- `37_MOC_SlovniATechnickeUlohy.tex` až `46_ALG_AlgebraickeVzorce.tex` – nesourodé titulky (zejména 42–46).

**Oprava:** Jednotný parser/průchod přes boxy, potom vizuální kontrola skutečného pořadí čísel. Zvlášť hlídat, že označení `V1` může patřit *vysvětlujícímu/výkladovému* boxu, který nemá být mechanicky přejmenován na příklad bez didaktického rozhodnutí.

### 4.2 Prostřední generace (`Příklad 1 – název`, `Úloha 1`)

Nachází se výrazně v **59–65**, **72–85**, **103–129**.

Konkrétní ukázky:

- `59_FNC_CoJeFunkce.tex`: `Příklad 1: jedna funkce, několik argumentů`.
- `63_FNC_LinearniFunkceAParametry.tex`: `Příklad 2: od dvou bodů k předpisu`.
- `72_ROV_RovniceAEkvivalentniUpravy.tex`: několik `Úloha 1`, `Úloha 2`, `Úloha 3`.
- `79_SOU_DosazovaciMetoda.tex`: `Příklad 3 – sbírka č. 30a, vhodný samostatný pokus`.
- `84_SOU_SoustavyTriNeznamych.tex`: `Příklad 1 – sbírka č. 31b`.
- `103_KVR_NeuplneRovniceI.tex`: `Příklad 4 – nejprve uprav na nulový tvar`, `Úloha 1`.
- `106_KVR_UplnaRovniceII.tex`: `Příklad 5 – složená rovnice se čtverci (dobrovolně)`.
- `124_KAH_GrafySAbsolutnimiHodnotami.tex`: `Příklad 1 -- modul celého výrazu`.
- `125_LRO_RovniceVPodilovemTvaru.tex`: `Příklad 2 -- zakázaný kořen`.

**Oprava:** Přepsat na přesný titulek a potřebné pedagogické popisy ponechat jako poznámku nebo běžný text před boxem. U samostatných úloh nepoužívat titulek `Úloha`, ale `Samostatná práce n`.

### 4.3 Novější generace (defaultní `Příklad` a `Zadání` bez čísla)

Hojná od **47** do konce, zejména **86–102**, **130–136**, ale také jinde. Tato verze je graficky konzistentní se šablonou, **nesplňuje však požadavek na číslo příkladu ani rozlišení kategorie**.

**Oprava:** Explicitní `title={Příklad n}`, `title={Samostatná práce n}` nebo `title={Rozšíření n}` podle pedagogické role. **Nesnažit se vše číslovat jedním automatickým čítačem** – každá kategorie má vlastní posloupnost; domácí úkol zůstává nečíslovaný.

### 4.4 Definice

- Standard `definiceBox` už většina příprav dodržuje; není důvod jej přestavovat.
- V některých souborech se liší `title`, např. `69_ALG_PololetniPisemnaPrace.tex` má `title={Připomenutí definice}` – titulkem má být jen `Definice`.
- **Nevyrábět nové definiční boxy** pro postupy typu „odmocníme rovnici“ nebo pro libovolné metodické upozornění. V 103 správně zůstává pravidlo `\sqrt{x^2}=|x|` vysvětlením, nikoli další definicí.
- Samostatná definice je důležitá pro *nový pojem* (např. definiční obor, omezenost, diskriminant); rozbité či rozdílné definice při hromadné typografické revizi nepřepisovat bez samostatné matematické kontroly.

---

## 5. Rychlé obsahové hodnocení (co zachovat, co dovysvětlit)

Tato část **není instrukce přepsat vše**. Uvádí místa, kde má smysl přidat jednu až dvě cílené poznámky pro učitele; u ostatních ponechat kvalitní existující výklad.

| Rozsah | Stav / silné stránky | Doporučené zpřesnění učitelských poznámek |
|---|---|---|
| **01–04** | Organizační úvod, výroková logika, kvantifikátory; dobře rozvržené výklady, příklady a názorné negace. | U implikace a kvantifikátorů držet explicitní protipříklad a obor, z něhož se kvantifikuje. Nepřidávat duplicitní definice. |
| **05–11** | Číselné obory, operace, intervaly, absolutní hodnota; mnoho užitečných vysvětlení. | Oddělovat rozšíření (Peanovy axiomy) od povinného jádra. Připomínat rozdíl mezi přesným číslem a zaokrouhlením; rozdíl opačné/převrácené číslo. **Zde je hlavní problém styl**, nikoli chybějící výklad. |
| **12–20** | Množiny, operace, Vennovy diagramy a slovní úlohy; velmi bohaté poznámky a rezervy. | Výslovně vždy uvést univerzum u doplňku množiny a rozdíl „právě v jedné“ vs. „alespoň v jedné“. Při unifikaci nevyhazovat učitelské komentáře z nadpisů. |
| **21–24** | Test a základy goniometrie v pravoúhlém trojúhelníku; aplikační úlohy. | Kalkulačka: režim stupňů a význam vstupních hodnot; před dosazováním pojmenovat přeponu/odvěsny. Testovou přípravu neplnit zadáními. |
| **25–40** | Mocniny, exponenty, odmocniny, zlomky a vědecký zápis. Dobrá návaznost a rozšíření. | Zřetelně oddělit pravidla pro kladná/záporná čísla a podmínky u odmocnin. U `\sqrt{x^2}` psát `|x|`. Pomocné materiály 27/39 přesunout z učitelských příprav. |
| **41–58** | Souvislý a procvičený algebraický blok. Výrazný výskyt společných úloh, rezerv a domácí práce. | U lomených výrazů explicitně upozornit, že **krácení nemění původní definiční podmínky**; u součinových vzorců ukázat typické znaménkové chyby. Značení boxů sjednotit. |
| **59–62** | Obecný úvod do funkcí, definiční obor a obor hodnot, monotónnost, prostá/sudá/lichá/periodická, omezenost. | Důležité pedagogické riziko: u sudosti/lichosti předpoklad souměrného definičního oboru; u maxima/minima rozdíl mezi mezí a dosaženou hodnotou. |
| **63–71** | Lineární/konstantní funkce, slovní aplikace a funkce s absolutní hodnotou; dobré pracovní listy. | Nedopustit, aby lineární funkce s omezeným definičním oborem byla vykládána jako celá přímka. Zkontrolovat archivní list pro 71 (není další učitelská příprava). |
| **72–78** | Rovnice a nerovnice, včetně geometrického obracení znaménka a intervalových průniků. | U násobení nerovnosti výrazem obsahujícím `x` vyžadovat rozbor znaménka; zjednodušené podílové nerovnice v 77 ponechat volitelné. |
| **79–85A** | Dosazovací, sčítací, odečítací a porovnávací metody, počet řešení, `3×3`, dobrovolná matice/Gauss. Metodicky silná část. | U 81 výslovně nechat žáky srovnat **stejnou** soustavu čtyřmi metodami. U 83 kontrolovat všechny tři rovnice. U 85A označit návaznost jako výběrovou; 4×4 není povinným standardem. |
| **86–90** | Test, rovnice/nerovnice s absolutní hodnotou, parametr. Tabulková metoda se v přípravách používá. | Při otevřených intervalech vždy zkoušet kritické body; u parametru pečlivě hlídat případ nulového koeficientu. Hodinám 87/88/90 prospívá druhá poznámka na nejčastější žákovskou chybu, nejen časový rozpis. |
| **91–95** | Pestré slovní a aplikační úlohy, domácí procvičení a souhrnná sbírka. | U 93 trvat na rozdílu **modelová vs. skutečná data** a kontrole jednotek. Vyřadit starý zdroj 93 ze složky příprav. Test 94 bez žákovských variant je záměr. |
| **96–102** | Návazný celek kvadratických funkcí, grafů, vrcholu a nulových bodů. | Více konkrétních varování: omezený definiční obor může změnit obor hodnot; parabola se nemusí protínat s osou x; kontrolovat znaménko `a` a vrchol. Nyní má řada hodin hlavně **jednu časovou poznámku**. |
| **103–109** | Neúplné/úplné kvadratické rovnice, vzorec, Viètovy vztahy, rozklad. Pořadí 107→108 je správné. | **Přednostně opravit chybnou sazbu 103.** V 105 zdůraznit důvod dělení `a ≠ 0`, `\sqrt{4a^2}=2|a|` a význam znaménka diskriminantu. U 106–109 připomenout volbu postupu podle tvaru rovnice. |
| **110–121** | Organizační testy, bikvadratické rovnice, soustavy, dvě odlišné absolutní hodnoty, odmocninové rovnice, parametr a aplikace. | Hlídat podmínku `t = x² ≥ 0` u substituce; další kořeny po umocnění vždy zkontrolovat; rozlišovat `|f(x)|` vs. `f(|x|)` a práci s grafem. Testy 110/121 bez žákovských zadání ponechat. |
| **122–129** | Kvadratické nerovnice graficky a znaménkově, modulové grafy, podílové rovnice, soustavy nerovnic, procvičení. | V 125 zdůraznit **nulový čitatel a nenulový jmenovatel** a zvláštní případy po krácení. U soustav kvadratických nerovnic řešit vždy průnik. U 124 grafy označit jako výběr, ne všechny povinně. |
| **130–136** | Sedm různorodých opakovacích hodin včetně aplikací a únikovky. Struktura obsahuje společné příklady, samostatnou práci a domácí úkoly. | Ponechat diferenciaci podle výkonu třídy; u 136 jasně říci pravidla, kontrolu kódu a že nejde o další test. V rozpisu opravit 130/135. |

### Poznámky pro učitele – cílová kvalita

U **každé nové výkladové přípravy** (mimo organizační test a čistě samostatnou práci) mají učitelské poznámky pokud možno odpovědět na tyto čtyři praktické otázky:

1. **Co doslova zdůraznit nebo ukázat na tabuli?** Jedna zásadní souvislost, ne pouhá parafráze zadání.
2. **Kde student typicky udělá chybu a proč?** Uvést konkrétní nesprávný krok nebo protipříklad.
3. **Co je povinné minimum a co volitelná rezerva?** Uvést odkaz na konkrétní příklad či blok.
4. **Co udělat, když hodina nestíhá?** Časový rozpis není sám o sobě metodickou poznámkou.

Nemusí to znamenat čtyři dlouhé poznámky v každé přípravě. Jestli jsou informace kvalitně uvedeny přímo v metodickém textu, neduplikovat je. **Priorita na doplnění:** 87–90, 91–92, 95, 96–102, 124–125, případně 130–136 podle reálného průběhu ve třídě. V hodinách 02–18 bývají poznámky už dostatečně konkrétní: především je **zachovat**.

---

## 6. Index všech 136 hodin – co při opravách kontrolovat

**Legenda:** **S** = sjednotit titulky boxů (neobsahuje pokyn měnit výpočty); **M** = doplnit/zvážit metodické vysvětlení; **O** = organizační soubor/test nebo list, neplést s výukovou přípravou; **K** = konkrétní nalezená chyba/konflikt. Pro téměř všechny netestové hodiny platí S, protože aktuální výchozí `Příklad`/`Zadání` bez čísla nesplňuje cílový standard.

| Hod. | Téma z aktuálních souborů | Audit / hlavní akce |
|---:|---|---|
| 01 | Úvodní hodina | O: organizační hodina, bez povinného boxového schématu. |
| 02 | Co je výrok | S; zachovat oddělené definice a dobré poznámky. |
| 03 | Pravdivost složených výroků | S; nepřijít o poznámky k implikaci. |
| 04 | Kvantifikátory | S; zachovat upozornění na obory. |
| 05 | Přirozená a celá čísla | S: `P1/V1/R1/D1`; Peanovy axiomy ponechat volitelné. |
| 06 | Racionální čísla a zlomky | S: staré zkratky, jinak dobrá metodika. |
| 07 | Reálná čísla a zaokrouhlování | S: staré zkratky; poznámka o zaokrouhlování. |
| 08 | Intervaly | S: `P1/R1/D1`; kontrola krajních bodů. |
| 09 | Absolutní hodnota | S: staré zkratky; vzdálenost na ose. |
| 10 | Průběžný test a rozbor | O/S: ponechat organizaci, titulky rozborových úloh sjednotit. |
| 11 | Číselné obory a výroky | S: staré zkratky; zdůvodnění oboru. |
| 12 | Množina a její prvky | S: popisné titulky; definice zachovat oddělené. |
| 13 | Podmnožina a rovnost množin | S: `P1/S1/R1/D1`; hlídat správný význam rovnosti. |
| 14 | Vennovy diagramy | S: `P1/S1/R1/D1`; domácí obrázky zachovat. |
| 15 | Vlastnosti množin, mohutnost | S: staré zkratky; definovat univerzum. |
| 16 | Operace s intervaly | S: navíc `P3b`; sjednotit číslování. |
| 17 | Slovní úlohy se dvěma množinami | S: popisné názvy; zachovat vysvětlení průniku. |
| 18 | Slovní úlohy se třemi množinami | S; pevně rozlišovat „právě“ / „alespoň“. |
| 19 | Kombinované slovní úlohy | S: `D0/P1/S1`; podle role boxu. |
| 20 | Opakování množin a intervalů | S: `D0`, `S3a/S3b`, `R1/D1`; bez změny úloh. |
| 21 | Test a úvodní diskuse | O: správně kombinovaná organizační hodina. |
| 22 | Pravoúhlý trojúhelník a poměry | S; výklad sin/cos/tg podle stran. |
| 23 | Přesné hodnoty a kalkulačka | S: staré zkratky; M: režim DEG. |
| 24 | Goniometrické procvičování a aplikace | S: staré zkratky; zachovat úlohy s výškovým úhlem. |
| 25 | Mocniny s přirozeným exponentem | S: `P1/S1/R1/D1`; zachovat typické chyby se závorkami. |
| 26 | Součin a podíl mocnin | S: `P1/P2/S1/R1/D1`, číslování není jednotné. |
| 27 | KISS – procvičování mocnin | S/K: v `pripravy/` je i separátní řecká tabulka, přemístit. |
| 28 | Celočíselný exponent | S: `Příklad 1: …`; výklad záporného exponentu zachovat. |
| 29 | Druhá a třetí odmocnina | S; poznámky k zápornému odmocněnci. |
| 30 | Pravidla pro odmocniny | S: titulky příkladů s popisy. |
| 31 | Racionální exponent | S; podmínky u odmocnin. |
| 32 | Částečné odmocňování | S; typické rozdíly v přípustných proměnných. |
| 33 | Usměrňování zlomků | S; nepřijít o podmínky. |
| 34 | Sdružené výrazy | S; zdůraznit výběr správného znaménka. |
| 35 | Složené výrazy s mocninami | S; ponechat dostatek místa na úpravy. |
| 36 | Vědecký a technický zápis | S; jednotky/předpony. |
| 37 | Slovní a technické úlohy | S: popisné titulky; aplikace zachovat. |
| 38 | KISS II – opakování | S: popisné titulky; nepřepisovat výsledky. |
| 39 | Příprava na test a chyby | S/K: duplicitní žákovský list v `pripravy/`. |
| 40 | Test a úvod do algebraických výrazů | O/S: bez testu navíc; úvodní příklad sjednotit. |
| 41 | Pojmy a mnohočleny | S; dostatečný soubor samostatných definic. |
| 42 | Sčítání a odčítání mnohočlenů | S: příklady s podtituly. |
| 43 | Násobení jednočlenu mnohočlenem | S: příklady s podtituly. |
| 44 | Násobení mnohočlenů | S: `S1/R1/D1`, doplnit souvislé číslo příkladů. |
| 45 | Mocnění mnohočlenů | S: `Příklad 1: …`, `S1/R1/D1`. |
| 46 | Algebraické vzorce | S: `S1/R1/D1`; vzorce zachovat jako přehled. |
| 47 | Dělení mnohočlenu jednočlenem | S; základní a rozšiřující příklady. |
| 48 | Dělení mnohočlenu mnohočlenem | S; hlídat zbytek. |
| 49 | Vytýkání a seskupování | S; přehled metod. |
| 50 | Rozklad kvadratických trojčlenů | S; netahat předčasně diskriminant. |
| 51 | Rozklady rozdělením a seskupením | S; zachovat alternativní postupy. |
| 52 | Lomené výrazy – podmínky a krácení | S; M: původní podmínky. |
| 53 | Sčítání a odčítání lomených výrazů | S; M: společný jmenovatel. |
| 54 | Násobení a dělení lomených výrazů | S; M: podmínky. |
| 55 | Složené lomené výrazy | S; M: nepřípustné hodnoty. |
| 56 | Smíšené úpravy výrazů | S; samostatný výběr metody. |
| 57 | Průběžný test z algebry | O/S: organizační rozbor, bez testového zadání. |
| 58 | Opakování úprav výrazů | S; zachovat kontrolní úlohy. |
| 59 | Co je funkce | S: `Příklad 1: …`; definice přiměřené. |
| 60 | Definiční obor a obor hodnot | S; M: omezení oboru. |
| 61 | Monotónnost, prostá, lichá a sudá | S; M: symetrie D(f), periodičnost. |
| 62 | Omezenost a extrémy | S; M: maxima vs. mez. |
| 63 | Lineární funkce a parametry | S: příklady s názvy. |
| 64 | Samostatné procvičování lineárních funkcí | S; dobré určení povinného minima. |
| 65 | Grafy lineárních a konstantních funkcí | S; M: omezený definiční obor. |
| 66 | Slovní úlohy lineárních funkcí | S; zachovat rozdílné aplikace. |
| 67 | Souhrnné procvičování lineárních funkcí | S; pracovní list ponechat oddělený. |
| 68 | Grafické porovnávání lineárních funkcí | S; souvislost průsečíku a řešení. |
| 69 | Pololetní písemná práce | O/S: upravit titulek `Připomenutí definice`; zadání testu není v repo. |
| 70 | Funkce s absolutní hodnotou | S; grafické transformace. |
| 71 | Grafy se dvěma absolutními hodnotami | S/K: duplicitní žákovský list v `pripravy/`. |
| 72 | Rovnice a ekvivalentní úpravy | S: `Úloha 1`; M: kdy je úprava ekvivalentní. |
| 73 | Lineární rovnice I | S: `Příklad 1 – název`; zachovat progresi. |
| 74 | Složené závorky a výrazy | S; samostatná práce dle tempa. |
| 75 | Lineární rovnice II | S; M: proměnná ve jmenovateli jen volitelně. |
| 76 | Nerovnice a úpravy | S; M: změna znaménka. |
| 77 | Nerovnice se zlomky | S; podílová nerovnice je volitelná. |
| 78 | Soustavy lineárních nerovnic | S; M: průnik na ose. |
| 79 | Dosazovací metoda | S: popisné titulky a `Úloha 1`. |
| 80 | Sčítací metoda | S: popisné titulky a `Úloha 1`. |
| 81 | Volba metody a procvičování | S; zachovat různé metody téže soustavy. |
| 82 | Počet řešení a geometrie | S; soustavy s 0/1/∞ řešeními. |
| 83 | Tři rovnice, dvě neznámé | S; M: potvrzení třetí rovnice. |
| 84 | Soustavy tří neznámých | S: názvy z fotografií/sbírky přesunout z titulku. |
| 85 | Eliminace `n×n` | S; 4×4 nechat výběrové. |
| 86 | Průběžný test I | O/S: pouze organizační test a rozbor. |
| 87 | Rovnice s absolutní hodnotou | S/M: kritické body a odmítnutí kandidátů. |
| 88 | Dvě absolutní hodnoty | S/M: tabulky a případ celého intervalu. |
| 89 | Nerovnice s absolutní hodnotou | S; kontrola otevřených/uzavřených mezí. |
| 90 | Rovnice s parametrem | S/M: nulový koeficient. |
| 91 | Slovní úlohy na lineární rovnice | S; jednotky a věcná zkouška. |
| 92 | Slovní úlohy na soustavy | S; pojmenovat neznámé. |
| 93 | Aplikační slovní úlohy | S/K: vyřadit starou verzi 93; zachovat nabídku oborů. |
| 94 | Průběžný test II | O/S: nevyžadovat varianty A/B v repozitáři. |
| 95 | Souhrnné procvičování | S/K: žákovská sbírka patří jen do `pracovni_listy/`. |
| 96 | Úvod do kvadratické funkce | S/M: odlišit funkci a její graf. |
| 97 | Vliv koeficientu `a` | S/M: orientace a šířka paraboly. |
| 98 | Posuny a vrcholový tvar | S/M: souřadnice vrcholu. |
| 99 | Doplnění na čtverec | S/M: pozor na `a<0`. |
| 100 | Průsečíky s osami | S/M: mohou neexistovat. |
| 101 | Graf z obecného tvaru | S/M: sestavení vrcholu a oboru hodnot. |
| 102 | Souhrnné procvičení funkcí | S; list zadání a řešení zůstává oddělený. |
| 103 | Neúplné kvadratické rovnice I | **K/P0: opravit chybné `\\` v řetězci odmocňování**; poté S. |
| 104 | Neúplné kvadratické rovnice II | S; přechod k vytýkání. |
| 105 | Diskriminant a vzorec | S; zachovat správné odvození `2|a|`. |
| 106 | Úplná kvadratická rovnice II | S; náročný závěrečný příklad ponechat jako volitelný. |
| 107 | Viètovy vztahy | S; správná pozice před rozkladem. |
| 108 | Rozklad kvadratického trojčlenu | S; navázat na 107. |
| 109 | Opakování kvadratických rovnic | S; volba metody. |
| 110 | Čtvrtletní práce P3 | O: bez zadání podle dohody. |
| 111 | Bikvadratické rovnice | S/M: `t=x²≥0`. |
| 112 | Soustava přímky a paraboly | S; zkouška dvojic. |
| 113 | Průsečíky dvou parabol | S; ponechat. |
| 114 | Kvadratická rovnice s modulem I | S/M: `|q(x)|` a intervaly. |
| 115 | Kvadratická rovnice s modulem II | S/M: `q(|x|)` a symetrie. |
| 116 | Odmocninové rovnice I | S/M: podmínky a zkouška. |
| 117 | Odmocninové rovnice II | S/M: falešné kořeny po umocnění. |
| 118 | Rovnice s parametrem | S/M: výjimečné hodnoty. |
| 119 | Slovní úlohy geometrie | S; zlatý řez ponechat jako aplikaci. |
| 120 | Technické aplikace rovnic | S; jednotky a model. |
| 121 | Průběžný test T7 | O: pouze organizační zadání. |
| 122 | Kvadratické nerovnice graficky | S; ostré/neostré vztahy. |
| 123 | Kvadratické nerovnice – znaménka | S; opakované nulové body. |
| 124 | Grafy s absolutními hodnotami | S/M: ne všechny varianty jsou povinné. |
| 125 | Rovnice v podílovém tvaru | S/M: jmenovatel nesmí být nula. |
| 126 | Soustavy kvadratických nerovnic | S; průnik. |
| 127 | Smíšené procvičování | S; rezerva a výzva oddělit. |
| 128 | Aplikační úlohy | S; interpretace výsledku. |
| 129 | Souhrnné procvičování | S; samostatná sbírka jako zdroj. |
| 130 | Logické stopy a množiny | S/K: rozpis mylně uvádí test T8. |
| 131 | Algebraický servis | S; opravy chyb a rozklady. |
| 132 | Funkce jako příběh | S; spojit graf s kontextem. |
| 133 | Rovnice a volba metody | S; více správných postupů. |
| 134 | Nerovnice a absolutní hodnota | S; průnik a krajní body. |
| 135 | Matematika v praxi | S/K: rozpis mylně uvádí písemnou práci P4. |
| 136 | Matematická únikovka | S; zachovat pracovní list a učitelský klíč. |

**85A (bonus):** `85A_MAT_MaticeAUvodDoGaussovyEliminace.tex` – není součástí povinné řady 1–136, ale je přítomen. Při sjednocování boxů použít stejný standard; v časovém rozpisu jej držet jako náhradu, nikoli dodatečnou povinnou hodinu.

---

## 7. Pořadí budoucích oprav – doporučené dávky

| Dávka | Priority a soubory | Jak ověřit |
|---|---|---|
| **0. Úklid a blokující chyby** | Opravit 103; vyjasnit starou 93, archivní listy 27/39/71/95; sjednotit seznam platných hodin. | `git diff` jen zamýšlené soubory; 103 znovu vysázet a zkontrolovat vizuálně. |
| **1. Základní styly 01–40** | Přejmenovat `P1/S1/R1/D1/V1` a tematické titulky na požadované standardy. | Souvislé číslování P, S, R; domácí právě jeden box; výpočty ani zadání beze změn. |
| **2. Algebra a funkce 41–71** | Odstranit podtituly z boxů, očíslovat defaultní boxy; zachovat grafické listy. | Každé PDF zkompilovat; porovnat počet úloh před a po změně. |
| **3. Lineární učivo 72–95** | `Úloha 1` → `Samostatná práce 1` / `Rozšíření 1` dle skutečné funkce; jeden domácí box. | Zachovat tabulky absolutní hodnoty, množiny `K` a 85A jako volitelnou. |
| **4. Kvadratické učivo 96–129** | Jednotné titulky příkladů a samostatné práce; doplnit klíčové metodické poznámky. | Zvlášť 103, 105, 114–117, 122–126, 124 grafy; reálná kontrola výstupních PDF. |
| **5. Opakování 130–136** | Očíslovat boxy, zachovat kreativní a výběrový charakter. | Zkontrolovat 136 pracovní list a klíč; nerozšiřovat o testy. |
| **6. Rozpis a závěrečný audit** | Aktualizovat `Rozpis_vyuky_MAT_1_rocnik.tex` na skutečné přípravy a sladit testy s organizačními požadavky. | 136 základních hodin bez duplicit, zkompilované PDF, ručně zkontrolované vzorky každého celku. |

### Akceptační kritéria – kdy uznat první ročník za unifikovaný

- [ ] Přesně **136 hlavních** učitelských příprav; bonus 85A veden zvlášť; pracovní listy nepočítat jako další vyučovací hodiny.
- [ ] Žádná současně aktivní stará verze stejné přípravy, zejména **93**.
- [ ] Každý box má jen požadovaný titulek: `Definice`, `Příklad n`, `Samostatná práce n`, `Rozšíření n`, `Domácí úkol`.
- [ ] Číslování P/S/R je souvislé **v rámci jedné hodiny**; žádné `P1`, `S1`, `R1`, `D1`, `V1`, `Foto …` jako titulek.
- [ ] Každá výuková hodina s domácím cvičením má **právě jeden** domácí box, se všemi zadáními a řešeními v odpovídajícím pořadí `a)`, `b)`, …
- [ ] Řešení odpovídají původním zadáním, jsou čitelná a rovnítka jsou zarovnaná; rovnice/nerovnice mají korektní `K`.
- [ ] U skutečně **nových matematických pojmů** zůstávají samostatné definice; běžné algoritmy se nepředefinují jako definice.
- [ ] U výkladových hodin existují užitečné učitelské poznámky o **typických chybách, hlavní myšlence, povinném minimu a případné rezervě**; ne jen minuta po minutě.
- [ ] Všechna změněná `.tex` mají správná a aktuální PDF. U 103 musí být vizuálně správná třířádková posloupnost odmocňování.
- [ ] Aktualizovaný rozpis odpovídá skutečným přípravám a rozhodnutí o testech/volitelné 85A.
- [ ] Po úpravách zkontrolován `git diff`; bez náhodných úprav šablony a ostatních ročníků; **bez asistentského pushování**.

---

## 8. Výslovně mimo rozsah této rychlé kontroly

Aby report nevzbuzoval falešnou jistotu:

- Nezávislý symbolický přepočet **všech** učitelských a domácích příkladů (tuto kontrolu doporučuji jako samostatnou poslední etapu po sjednocení).
- Obrazová kontrola **každé** stránky všech 136 PDF a všech pomocných sbírek. Z konkrétních kontrol jsem ověřil problematické místo 103 v existujícím PDF.
- Kontrola oficiálního `SPS.pdf` po jednotlivých očekávaných výstupech; zde byl přímo čten textový rozpis `.tex`, který je zjevně starší.
- Vytváření testových variant a změny školního klasifikačního plánu.

**Doporučený další krok:** Použít tento report jako kontrolní seznam, nejprve opravit P0 nálezy a potom postupovat po dávkách, ideálně vždy s diffem a PDF k nahlédnutí. **Obsah příprav máme; zbývá ho důsledně sjednotit, ne začínat znovu.**
