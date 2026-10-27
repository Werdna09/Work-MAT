# Pokyny pro AI agenta – matematické výukové materiály

## Účel projektu

Repozitář slouží středoškolskému učiteli matematiky k tvorbě učebnice, příprav na vyučování, testů a pracovních listů. Výsledné výukové materiály vytvářej v českém jazyce a v LaTeXu, pokud uživatel výslovně nepožaduje jinak. Vždy respektuj požadovaný ročník, úroveň žáků, rozsah učiva a účel dokumentu. Neznámé důležité parametry si vyjasni; u drobností zvol přiměřený předpoklad a uveď jej.

## Organizace projektu a tematické plány

Projekt má dvě odlišné organizační osy: **centrální učebnici podle matematických oblastí** a **výukové materiály podle ročníků**. Nemíchej je.

- `ucebnice/` obsahuje společnou učebnici pro SPŠ i gymnázium, členěnou podle matematických oblastí, nikoli podle ročníků. Kapitoly zbytečně nekopíruj do adresářů ročníků. Respektuj existující podadresáře a názvy souborů.
- `1_rocnik/` až `4_rocnik/` obsahují vždy `tematicke_plany/`, `testy/`, `pracovni_listy/` a `pripravy/`. Nové materiály ukládej do odpovídajícího ročníku. Testy a pracovní listy lze dále členit podle témat; přípravy se standardně ukládají přímo do `N_rocnik/pripravy/` a řadí se podle čísla hodiny. Tematické podsložky vytvářej jen tehdy, pokud si je učitel výslovně přeje.
- `sablony/` obsahuje společné šablony pro `testy/`, `pracovni_listy/` a `pripravy/`. Vždy nejprve zkontroluj skutečný obsah šablon a jejich způsob použití.
- `pravidla/` je vyhrazen pro pravidla související s výukou a hodnocením.
- `import_testu/` může obsahovat pracovní kopie starších testů, opravných zkoušek a pracovních listů. Jde o **neověřený archiv**, nikoliv o schválenou banku správných úloh nebo závazné šablony.
- `externi_zdroje/` obsahuje externí podklady (např. materiály Realisticky.cz). Jsou zdrojem inspirace a kontroly návaznosti, nikoli automatickým svolením k doslovnému přebírání nebo šíření.

V `tematicke_plany/` každého ročníku jsou plány `SPS.pdf` (společný pro strojírenské a informatické obory SPŠ) a `GYM.pdf` (gymnázium). Při práci s konkrétním ročníkem prostuduj relevantní plán, pokud je dostupný, a zohledni návaznost učiva a časovou dotaci. Názvy a pořadí témat neodvozuj automaticky z obecného kurikula; opírej se o skutečné plány. Rozdíly mezi plány nejsou nepřekročitelnou hranicí obtížnosti či obsahu, pokud učitel zadá něco jiného.

Učebnice, přípravy a pracovní listy mohou sloužit oběma typům školy; nerozděluj je automaticky podle SPŠ a GYM. Učitel rozhoduje o použití v konkrétní třídě. Původní repozitář `~/ucebnice/` je archiv a zdroj podkladů: bez výslovného pokynu jej neupravuj, nemaž ani z něj nic automaticky neimportuj.

## Existující podklady a šablony

Než začneš tvořit nebo upravovat dokument, prohlédni související soubory, šablony, makra a vzorové materiály dostupné v repozitáři. Přednost mají skutečné soubory projektu před obecnými pravidly uvedenými zde. Nevydávej popsané zvyklosti za ověřené vlastnosti projektu, dokud nenajdeš odpovídající soubory. Pokud podklady chybějí, stručně upozorni, že pracuješ bez vzoru.

Zachovávej existující členění projektu, názvy souborů a funkční kompilovací postup. Nevytvářej duplicitní šablony, nadbytečné adresáře ani nová makra, jestliže stávající řešení stačí. Případné rozdíly mezi šablonami nepřepisuj plošně bez souhlasu. Pro nové testy používej aktuální šablony v `sablony/testy/`; pokud nejsou na disku dostupné, upozorni na to a nevydávej jejich předpokládanou podobu za skutečnost.


## Autorský styl a matematické značení

Zachovej především autorův styl formátování LaTeXu: strukturu dokumentu, členění na odstavce, způsob zápisu rovnic, prostředí, odsazování a prostorové uspořádání. Druhotně zachovej styl vyjadřování. Upřednostňuj souvislý, plynulý a srozumitelný matematický výklad před zbytečným množstvím nadpisů, seznamů a vizuálních bloků. Při revizi měň jen to, co je nutné pro věcnou, jazykovou či didaktickou správnost.

Používej konzistentní českou matematickou terminologii, správnou symboliku a návaznost na dříve zavedené pojmy. Definice, tvrzení, důkazy a příklady rozlišuj podle vzorů projektu. Není-li doložena autorova volba, nevynucuj své oblíbené značení ani vlastní úpravu vzhledu.

## Učebnice

Centrální `ucebnice/` je rozdělená na tematické oblasti od `01_Zakladni_poznatky/` po `11_Diferencialni_a_integralni_pocet/`. Některé kapitoly tvoří samostatné `.tex` soubory, jiné mohou být propojené projekty. Konkrétně `ucebnice/07_Analyticka_geometrie/projekt/` obsahuje samostatný funkční LaTeXový projekt s `main.tex`, `preamble.tex` a navazujícími soubory načítanými přes `\input`. Bez zadání je nerozděluj a neměň vazby mezi nimi.

Při pokračování učebnice si přečti navazující části a ověř, jak jsou zavedeny pojmy a značení. Je-li v projektu soubor `ucebnice.sty` a prostředí jako `definition`, `example`, `solution` nebo příkaz `\historybox`, používej je v souladu se skutečnou definicí a existujícími příklady. Ne každý dokument však musí `ucebnice.sty` používat; respektuj vlastní preambuli existujících projektů. Nevkládej nové stylové balíčky ani nepřepisuj preambuli bez důvodu. Nevytvářej izolovanou kapitolu odlišnou stylem od zbytku učebnice.

Výklad má být odborně přesný, ale přístupný středoškolákům. Vysvětluj motivaci, podmínky platnosti a význam prováděných kroků; nepřeskakuj podstatné úvahy. Historické poznámky a citace používej jen s doložitelným zdrojem, nikdy je nevymýšlej.

### Zápis matematických výsledků v učebnici

V souborech učebnice nikdy nepoužívej příkaz `\boxed{}` ani jeho
obdoby k orámování matematických výsledků.

Výsledky rovnic, výrazů, výpočtů a řešených příkladů zapisuj
standardním matematickým zápisem v prostředích `$...$`, `\[...\]`,
`align` apod., v souladu s okolním textem.

Výsledek může být uveden běžnou větou, například „Dostáváme ...“,
„Řešením je ...“ nebo „Odtud vyplývá ...“.

Nezaváděj vlastní rámečky pro zvýrazňování konečných výsledků.

Toto omezení se netýká existujících prostředí `definitionbox`,
`examplebox`, `solutionbox`, `notebox` a dalších autorských
prostředí používaných pro strukturování učebnice.

Při úpravách starších kapitol nahrazuj `\boxed{}` běžným
matematickým zápisem, pokud se nachází v právě upravované části.
Neměň kvůli tomu nesouvisející kapitoly.

## Testy: umístění, pojmenování a šablony

Nové testy ukládej do `N_rocnik/testy/<Tematicky_celek>/`, kde `N` je příslušný ročník. Název tematického celku odvoď podle skutečného učiva a existující struktury. **Nevytvářej automaticky samostatnou složku pro každý test**; varianty stejného testu ukládej vedle sebe do tematické složky. Další podadresář vytvoř jen tehdy, má-li konkrétní opodstatnění.

Pro každý nový test je závazná konvence:

`[cislo]_test_[nazev]_[varianty].tex`

Například `01_test_ExponencialniRovnice_AB.tex`, `01_test_ExponencialniRovnice_CD.tex` nebo `02_test_ExponencialniRovnice_GH.tex`. Číslo je dvojciferné, začíná obvykle `01` a vyjadřuje pořadí testu **v rámci konkrétního tématu**, nikoliv celého školního roku. Hodnotu `00` použij jen záměrně (např. vstupní diagnostika). V nových názvech souborů používej názvy témat bez diakritiky a mezer; zachovávej konzistentní zápis. Soubor je pojmenován podle skutečných variant uvnitř, nikoliv podle předpokladu.

**Každá dvojice variant má vlastní samostatný `.tex` soubor:** `AB`, `CD`, `EF`, `GH`, `IJ`, `KL`. Soubor s příponou `_AB.tex` obsahuje variantu A i B, `_CD.tex` obsahuje C i D atd. Neslučuj více dvojic do jednoho souboru; nevytvářej nepožadované dvojice. Pokud se zadává pouze jedna varianta, postup pojmenování domluv s učitelem, místo abys druhou automaticky vytvářel.

V `sablony/testy/` se používají dva výchozí typy šablon, **pokud jsou skutečně přítomné a funkční**:

- `A5x2.tex`: A4 na šířku se dvěma testy velikosti přibližně A5 vedle sebe, obvykle jedna varianta v každé polovině. Vhodné pro kratší testy a desetiminutovky.
- `A4.tex`: A4 na výšku, vhodná pro rozsáhlejší písemky; dvojice variant může zabírat samostatné stránky.

Po schválení konkrétního výběru úloh podle části „Výběr úloh pro testy“ vyber vhodnou existující šablonu, **vytvoř z ní nový samostatný soubor** a zachovej její rozvržení, makra a hlavičku, pokud učitel nepožaduje změnu. Samotné šablony neupravuj při běžné tvorbě testu. Hlavička má obsahovat jméno a příjmení, třídu, datum a prázdná pole „Počet bodů“ a „Známka“. Tato prázdná pole nejsou bodováním zadání. Šablonu nikdy nepovažuj za matematicky ověřené zadání; výchozí ukázkové úlohy nahraď schválenými, matematicky ověřenými úlohami. Neopisuj mechanicky staré testy z `import_testu/`.

**V žákovském zadání nikdy automaticky neuváděj bodové hodnoty úloh ani podúloh, celkový maximální počet bodů, klasifikační stupnici ani procentní hranice známek. Jedinou výjimkou je výslovný pokyn učitele.** Zákaz platí pro všechny varianty A–L, všechny formáty A4/A5 a všechny typy běžných písemných testů, včetně textů a údajů převzatých ze šablony.

Řešení a výsledky drž odděleně od zadání pro žáky. Ulož je jednoznačně vedle příslušného testu nebo podle dohodnuté struktury; nepřidávej je do tiskové žákovské verze bez pokynu. Pokud existují různé varianty, musí být zřejmé, ke které řešení patří. V samostatném dokumentu s řešením uveď orientační bodovací schéma **pouze na výslovný požadavek učitele**; jinak připrav jen matematické postupy a výsledky. Vyžádané bodování je nezávazným návrhem, který může učitel při opravování spolu s kritérii uznávání postupů upravit podle svého odborného posouzení.

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

Toto je závazný standard pro soubory v `1_rocnik/pripravy/` až `4_rocnik/pripravy/`. Podrobná pravidla a ukázky jsou v **`sablony/pripravy/TUTORIAL_pripravy.md`**. Při tvorbě nebo úpravě přípravy:

1. **Nejprve pročti** tento `AGENTS.md`, `sablony/pripravy/TUTORIAL_pripravy.md`, `sablony/pripravy/TEMPLATE_Priprava.tex`, `sablony/pripravy/priprava.sty` a nejbližší související přípravy. Jestliže některý soubor chybí, nezakládej jeho náhradu bez důvodu.
2. **Dodrž pořadí výuky:** vycházej ze schváleného rozpisu hodin, zadání učitele, tematického plánu v `N_rocnik/tematicke_plany/` a návaznosti okolních lekcí. Cizí učebnice sama o sobě neurčuje číslování hodin. Rozpor podkladů oznam; samostatně nepřečíslovávej jiné hodiny.
3. **Umístění a název:** jednotlivé přípravy standardně ukládej přímo do `N_rocnik/pripravy/` jako `[NN]_[TTT]_[PopisnyNazev].tex`, např. `02_VRL_CoJeVyrok.tex` nebo `01_ÚVD_ÚvodníHodina.tex`. `NN` je pořadí vyučovací hodiny v ročníku, `TTT` trojpísmenná zkratka tématu. U již existujících souborů zachovej jejich názvy.
4. **Jednotný vzhled:** do nového `.tex` načti společný styl **`../../sablony/pripravy/priprava.sty`**, pokud je příprava přímo v `N_rocnik/pripravy/`, typicky `\input{../../sablony/pripravy/priprava.sty}`. Používej `\nastavPripravu{ročník}{globální téma}{číslo}{název}`. Cesta se počítá při kompilaci z adresáře `.tex` (např. pomocí `latexmk -cd`); při jiné hloubce podsložek ji přepočítej. Neduplikuj lokálně makra ani definice rámečků.
5. **Záhlaví a struktura:** v záhlaví vlevo „ročník | globální téma“, vpravo „číslo: název hodiny“. Nepřidávej úvodní metadatovou hlavičku, zápatí, povinný seznam cílů ani minutový rozpis. Didaktický výklad může přirozeně obsahovat motivaci, definice, vysvětlení, příklady, samostatné procvičení a vhodné metodické poznámky; používej jen potřebné oddíly.
6. **Definice a příklady:** každý samostatný matematický pojem definuj v **odděleném `definiceBox`**. Pro úlohu bez řešení použij `prikladBox` či `zadaniBox`. Pro zadání s řešením použij **`prikladReseniBox` nebo `zadaniReseniBox`** s právě jedním `\tcblower`: nahoře zadání, ve světle šedé spodní části řešení. Víceřádkové matematické výpočty saz do `align*` či obdobného prostředí **uvnitř spodní části**. Nepřipojuj samostatný druhý rámeček a pro nové dokumenty nepoužívej zastaralý příkaz `\reseni{}`.
7. **Učitelské poznámky:** piš pomocí `\poznamka{...}` šedým písmem mimo rámečky. Volitelné mezititulky lze vložit přes `\blok{...}`. Přesná znění a podporovaná prostředí ověřuj přímo v `priprava.sty`.
8. **Obsah:** zachovávej češtinu, matematickou přesnost, návaznost učiva a přiměřenou gradaci úloh. Rozlišuj povinný výklad a volitelné rozšíření; učitelskou přípravu nezaměňuj s pracovním listem pro žáky. Každé zadání i řešení matematicky ověř. Pokud je hodina obsahově přeplněná, upozorni na to.
9. **Zdroje a Realisticky.cz:** používej související materiály z `ucebnice/`, vlastních pracovních listů a dostupných `externi_zdroje/` jako podklady; Realisticky.cz zejména jako metodickou inspiraci. Dodržuj autorská práva, neodvozuj přístup nebo licenci z pouhé existence PDF, nevymýšlej odkazy ani neprohlašuj nepřečtené lekce za ověřené. Použité zdroje eviduj v komentářích `.tex` či v interním přehledu, ne automaticky v zápatí PDF.
10. **Kompilace a rozsah změn:** z kořene projektu použij např. `latexmk -cd -pdf -interaction=nonstopmode -halt-on-error 1_rocnik/pripravy/02_VRL_CoJeVyrok.tex` a zkontroluj log i výslednou sazbu. Při zadání jedné hodiny neupravuj jiné přípravy, osnovy, sdílený styl ani tento `AGENTS.md` bez výslovného pokynu.

Pokud se praktické ukázky v tutorialu a ve stylu liší, řiď se pro konkrétní LaTeXové příkazy aktuálním funkčním `priprava.sty`; rozpor však oznam a nepřepisuj sdílené soubory svévolně.

### Evidence dokončených příprav

Aktuální stav zpracování učitelských příprav je evidován v `planovani/STAV_PRIPRAV.md`.

Při tvorbě nebo úpravě učitelských příprav respektuj tento přehled a odpovídající rozpis výuky.

Po dokončení tematického celku zkontroluj úplnost všech jeho příprav a aktualizuj příslušný stav v `planovani/STAV_PRIPRAV.md`.

Stav `HOTOVO` použij pouze tehdy, pokud jsou vytvořeny všechny přípravy příslušného celku včetně `.tex` a `.pdf`.

Nevytvářej nové záznamy mimo tematické celky skutečně uvedené v tematických plánech.

## Matematická kontrola

Každé nově vytvořené zadání i řešení zkontroluj. Ověř definiční obory, předpoklady, ekvivalenci úprav, správnost výpočtů, jednotky, grafy a jednoznačnost otázky. Kde je to praktické, použij nezávislou metodu: zpětné dosazení, symbolický či numerický výpočet, kontrolu krajních případů nebo jiný postup. Pouhé opakované přečtení stejného řešení nepovažuj za nezávislé ověření. Pokud kontrolu nelze provést, výslovně to sděl; netvrď, že bylo ověřeno něco, co ověřeno nebylo.

U testů navíc **zkontroluj každou variantu samostatně**: jednoznačnost zadání, existenci a podobu řešení, časovou náročnost a případné učitelem vyžádané bodování. Každou převzatou, novou i upravenou úlohu včetně jejího řešení nezávisle ověř; předchozí použití ve výuce není důkazem správnosti.

Před označením testu za hotový ověř:

1. Všechny úlohy pocházejí ze schválených zdrojů nebo jejich tvorba byla výslovně povolena učitelem.
2. Každou převzatou úlohu lze podle evidence zdrojů dohledat k původnímu zadání; u povolené vlastní tvorby je zaznamenán její původ a u obdobné úlohy také zdrojový vzor.
3. Matematická zadání i přiřazení k variantám odpovídají výběru schválenému nebo přímo určenému učitelem.
4. Žádná úloha nebyla svévolně pozměněna; případné změny odpovídají výslovnému pokynu učitele.
5. Žákovský test neobsahuje bodové hodnoty úloh ani podúloh, maximální počet bodů, klasifikační stupnici ani procentní hranice známek, pokud je učitel výslovně nepožadoval. Jejich nepřítomnost výslovně zkontroluj také ve výsledném PDF, včetně textů převzatých ze šablony.
6. Hlavička zachovává prázdná pole „Počet bodů“ a „Známka“.
7. Varianty uvnitř každé dvojice jsou přibližně srovnatelné obtížností, časovou náročností a rozsahem, případně i vyžádaným bodovacím schématem.
8. Všechna matematická zadání a řešení, včetně každé upravené varianty úlohy, byla nezávisle ověřena.
9. PDF bylo úspěšně zkompilováno a vizuálně zkontrolováno podle části „Kompilace a kontrola výstupu“.

Pokud některou kontrolu nelze dokončit, uveď konkrétní omezení a test neoznačuj za hotový.

## Kompilace a kontrola výstupu

Po vytvoření či změně LaTeXového dokumentu použij existující překladač a nastavení projektu (např. `latexmk`), pokud jsou dostupné. Respektuj nastavení VS Code/LaTeX Workshop a případnou potřebu vyhledávací cesty k `ucebnice.sty`; neměň kvůli tomu automaticky každý jednotlivý `.tex` soubor. Zkontroluj protokol, chyby a významná varování. Je-li možné prohlédnout výsledné PDF, zkontroluj též diakritiku, matematickou sazbu, přetékání obsahu, velikosti grafů, rozvržení stránek a čitelnost při tisku. U šablony `A5x2.tex` zvlášť ověř, že se obě varianty skutečně vejdou na jednu A4 a nezasahují do sebe. Pokud PDF vizuálně nezkontroluješ, nepředstírej opak. Sděl, které soubory vznikly a zda kompilace proběhla úspěšně.

### Společné kontrolní skripty

Pro samostatné LaTeXové dokumenty používej, pokud je v repozitáři dostupný a funkční, skript `scripts/build_latex.sh`:

```bash
./scripts/build_latex.sh cesta/k/dokumentu.tex
```

Skript provádí základní kontrolu struktury, kompilaci a ověření PDF. Výsledné PDF musí být uloženo vedle zdrojového `.tex`; pomocné soubory ponechávej mimo adresář materiálů. V případě neúspěchu zjisti příčinu. Nepovažuj chybnou nebo neprovedenou kompilaci za úspěch.

Tento postup je určen primárně pro samostatné přípravy, testy a pracovní listy. Nepoužívej jej automaticky na dílčí kapitoly učebnice načítané přes `\input` ani na projekty se zvláštním systémem sestavení. Pokud skript chybí, použij stávající funkční kompilaci projektu. Pokud skript existuje, ale selže, chybu nezakrývej neohlášeným přepnutím na jiný postup.

Po automatické kontrole vždy proveď matematickou kontrolu a podle dostupných možností i vizuální kontrolu všech relevantních stránek PDF. Úspěch skriptu sám o sobě neprokazuje správnost matematiky, sazby ani rozložení testových variant.

## Bezpečnost, Git a rozsah změn

Pracuj pouze v určeném projektu a podle nastavených oprávnění. Bez výslovného souhlasu nemaž ani hromadně nepřesouvej soubory, nepřepisuj sdílené šablony a nepřidávej závislosti nebo nástroje do systému. Neotevírej ani nezveřejňuj osobní údaje žáků, přístupové údaje či tajné klíče, pokud to není nezbytné pro výslovně zadanou bezpečnou operaci. Změny udržuj malé a přehledné; nepřeformátovávej nesouvisející části. Před rozsáhlými změnami předlož krátký plán. Po práci stručně shrň provedené úpravy, matematické ověření, výsledek kompilace a případná omezení. Git commity neprováděj bez zadání; před commitem ukaž, co se změnilo.


## Referenční materiály

Při tvorbě učitelských příprav, testů a pracovních listů prostuduj podle potřeby soubor `sablony/KATALOG_VZORU.md`.

Katalog určuje doporučené vzory a jejich využití. Nenahrazuje závazné projektové šablony ani pravidla v tomto souboru.

Rozlišuj schválené referenční materiály od dosud neověřených ukázek. Nepovažuj ukázkové soubory automaticky za bezchybné.
