# Pokyny pro AI agenta – matematické výukové materiály

## Účel projektu

Repozitář slouží středoškolskému učiteli matematiky k tvorbě učebnice, příprav na vyučování, testů a pracovních listů. Výsledné výukové materiály vytvářej v českém jazyce a v LaTeXu, pokud uživatel výslovně nepožaduje jinak. Vždy respektuj požadovaný ročník, úroveň žáků, rozsah učiva a účel dokumentu. Neznámé důležité parametry si vyjasni; u drobností zvol přiměřený předpoklad a uveď jej.

## Organizace projektu a tematické plány

Projekt má dvě odlišné organizační osy: **centrální učebnici podle matematických oblastí** a **výukové materiály podle ročníků**. Nemíchej je.

- `ucebnice/` obsahuje společnou učebnici pro SPŠ i gymnázium, členěnou podle matematických oblastí, nikoli podle ročníků. Kapitoly zbytečně nekopíruj do adresářů ročníků. Respektuj existující podadresáře a názvy souborů.
- `1_rocnik/` až `4_rocnik/` obsahují vždy `tematicke_plany/`, `testy/`, `pracovni_listy/` a `pripravy/`. Nové testy, pracovní listy a přípravy ukládej do příslušného ročníku a dále podle tematického celku. Tematické složky vytvářej podle skutečné potřeby, ne plošně dopředu.
- `sablony/` obsahuje společné šablony pro `testy/`, `pracovni_listy/` a `pripravy/`. Vždy nejprve zkontroluj skutečný obsah šablon a jejich způsob použití.
- `pravidla/` je vyhrazen pro pravidla související s výukou a hodnocením.
- `import_testu/` může obsahovat pracovní kopie starších testů, opravných zkoušek a pracovních listů. Jde o **neověřený archiv**, nikoliv o schválenou banku správných úloh nebo závazné šablony.

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

## Testy: umístění, pojmenování a šablony

Nové testy ukládej do `N_rocnik/testy/<Tematicky_celek>/`, kde `N` je příslušný ročník. Název tematického celku odvoď podle skutečného učiva a existující struktury. **Nevytvářej automaticky samostatnou složku pro každý test**; varianty stejného testu ukládej vedle sebe do tematické složky. Další podadresář vytvoř jen tehdy, má-li konkrétní opodstatnění.

Pro každý nový test je závazná konvence:

`[cislo]_test_[nazev]_[varianty].tex`

Například `01_test_ExponencialniRovnice_AB.tex`, `01_test_ExponencialniRovnice_CD.tex` nebo `02_test_ExponencialniRovnice_GH.tex`. Číslo je dvojciferné, začíná obvykle `01` a vyjadřuje pořadí testu **v rámci konkrétního tématu**, nikoliv celého školního roku. Hodnotu `00` použij jen záměrně (např. vstupní diagnostika). V nových názvech souborů používej názvy témat bez diakritiky a mezer; zachovávej konzistentní zápis. Soubor je pojmenován podle skutečných variant uvnitř, nikoliv podle předpokladu.

**Každá dvojice variant má vlastní samostatný `.tex` soubor:** `AB`, `CD`, `EF`, `GH`, `IJ`, `KL`. Soubor s příponou `_AB.tex` obsahuje variantu A i B, `_CD.tex` obsahuje C i D atd. Neslučuj více dvojic do jednoho souboru; nevytvářej nepožadované dvojice. Pokud se zadává pouze jedna varianta, postup pojmenování domluv s učitelem, místo abys druhou automaticky vytvářel.

V `sablony/testy/` se používají dva výchozí typy šablon, **pokud jsou skutečně přítomné a funkční**:

- `A5x2.tex`: A4 na šířku se dvěma testy velikosti přibližně A5 vedle sebe, obvykle jedna varianta v každé polovině. Vhodné pro kratší testy a desetiminutovky.
- `A4.tex`: A4 na výšku, vhodná pro rozsáhlejší písemky; dvojice variant může zabírat samostatné stránky.

Před novým testem vyber vhodnou existující šablonu, **vytvoř z ní nový samostatný soubor** a zachovej její rozvržení, makra a hlavičku, pokud učitel nepožaduje změnu. Samotné šablony neupravuj při běžné tvorbě testu. Hlavička má obsahovat jméno a příjmení, třídu, datum, počet bodů a známku. Šablonu nikdy nepovažuj za matematicky ověřené zadání; výchozí ukázkové úlohy nahraď novým, zkontrolovaným obsahem. Neopisuj mechanicky staré testy z `import_testu/`.

Řešení, výsledky a případné bodovací schéma drž odděleně od zadání pro žáky. Ulož je jednoznačně vedle příslušného testu nebo podle dohodnuté struktury; nepřidávej je do tiskové žákovské verze bez pokynu. Pokud existují různé varianty, musí být zřejmé, ke které řešení patří.

## Testy: obtížnost a zadávání

Výchozí stupnice obtížnosti je následující:

- **A/B:** SPŠ, základní úroveň, zpravidla řádný termín.
- **C/D:** SPŠ, zvýšená obtížnost, často dopisování nebo oprava.
- **E/F:** SPŠ, vysoká obtížnost, často další dopisování nebo oprava; zpravidla těžší než C/D.
- **G/H:** gymnázium, základní gymnaziální úroveň, zpravidla řádný termín.
- **I/J:** gymnázium, velmi vysoká obtížnost, často dopisování nebo oprava.
- **K/L:** gymnázium, mimořádně náročná úroveň, často další dopisování nebo oprava; zpravidla těžší než I/J.

Platí dvě samostatné posloupnosti obtížnosti: **A/B < C/D < E/F** a **G/H < I/J < K/L**. Gymnaziální úlohy obvykle vyžadují větší míru abstrakce, propojování poznatků nebo důkazu. Nesrovnávej mechanicky každou dvojici napříč školami a nepovažuj přiřazení k typu školy za zákaz použití jiné varianty v konkrétní třídě. Konkrétní požadavek učitele má přednost před výchozí konvencí.

Vyšší obtížnost vytvářej zejména náročnější matematickou úvahou, nestandardními souvislostmi a vícefázovým řešením, nikoli jen většími čísly, zbytečně dlouhými výpočty či nepřiměřeným množstvím úloh. I opravné a náhradní termíny musí ověřovat stanovené učivo, být řešitelné v přiměřeném čase a odpovídat požadovanému hodnocení. **Varianty uvnitř jedné dvojice** musí mít srovnatelnou obtížnost, časovou náročnost, rozsah i bodování. Různé úlohy mohou testovat stejné dovednosti; pouhá výměna čísel není nutná.

**Opravná zkouška za pololetí či celý školní rok není automaticky další variantou běžného testu.** Zacházej s ní jako se samostatným typem dokumentu, který může mít odlišnou strukturu a rozsah. Starší zkoušky v `import_testu/opravne_zkousky/` jsou pouze neověřeným podkladem.

Nepřidávej kalkulačku, tabulky ani jiné pomůcky, pokud jejich použití nebylo povoleno. Jestliže chybí informace zásadní pro zadání testu (například rozsah látky, délka testu nebo povolené pomůcky), vyžádej si je před tvorbou.

## Pracovní listy

Pracovní listy ukládej do `N_rocnik/pracovni_listy/` a dále podle tématu; používej společné šablony ze `sablony/pracovni_listy/`, pokud existují. Vycházej z probíraného tématu a úrovně žáků. Pokud uživatel neurčí jinak, řaď úlohy od základního porozumění přes běžné procvičení po náročnější aplikace. U listů určených k vyplňování ponechávej přiměřené místo na výpočty, zápis nebo náčrtek; u vzorových listů respektuj jejich dosavadní úspornou sazbu. Pro grafy a geometrické obrázky používej přednostně zavedené nástroje projektu (například TikZ či pgfplots), pokud jsou vhodné. Výsledky a řešení udržuj oddělené od žákovské verze, není-li zadáno jinak. Staré pracovní listy v `import_testu/` nejsou automaticky obsahově ověřené.

## Přípravy na hodiny

Přípravy ukládej do `N_rocnik/pripravy/` a dále podle tématu; používej společné šablony ze `sablony/pripravy/`, pokud existují. Vycházej z učebnice, relevantního tematického plánu a zadaného ročníku, délky hodiny a výukového cíle. Podle potřeby navrhni motivaci, návaznost na předchozí učivo, výklad, typické chyby, otázky pro žáky, aktivitu, procvičení a orientační časový plán. Nepovažuj časové odhady za zaručené; upozorni, pokud je navržený obsah na danou hodinu příliš rozsáhlý. Rozlišuj interní metodickou přípravu učitele od materiálu pro žáky.

## Matematická kontrola

Každé nově vytvořené zadání i řešení zkontroluj. Ověř definiční obory, předpoklady, ekvivalenci úprav, správnost výpočtů, jednotky, grafy a jednoznačnost otázky. Kde je to praktické, použij nezávislou metodu: zpětné dosazení, symbolický či numerický výpočet, kontrolu krajních případů nebo jiný postup. Pouhé opakované přečtení stejného řešení nepovažuj za nezávislé ověření. Pokud kontrolu nelze provést, výslovně to sděl; netvrď, že bylo ověřeno něco, co ověřeno nebylo.

U testů navíc **zkontroluj každou variantu samostatně**: jednoznačnost zadání, existenci a podobu řešení, časovou náročnost, bodování a srovnatelnost obou variant. Pokud přebíráš úlohu ze staršího testu, ověř ji stejně důkladně jako novou; předchozí použití ve výuce není důkazem správnosti.

## Kompilace a kontrola výstupu

Po vytvoření či změně LaTeXového dokumentu použij existující překladač a nastavení projektu (např. `latexmk`), pokud jsou dostupné. Respektuj nastavení VS Code/LaTeX Workshop a případnou potřebu vyhledávací cesty k `ucebnice.sty`; neměň kvůli tomu automaticky každý jednotlivý `.tex` soubor. Zkontroluj protokol, chyby a významná varování. Je-li možné prohlédnout výsledné PDF, zkontroluj též diakritiku, matematickou sazbu, přetékání obsahu, velikosti grafů, rozvržení stránek a čitelnost při tisku. U šablony `A5x2.tex` zvlášť ověř, že se obě varianty skutečně vejdou na jednu A4 a nezasahují do sebe. Pokud PDF vizuálně nezkontroluješ, nepředstírej opak. Sděl, které soubory vznikly a zda kompilace proběhla úspěšně.

## Bezpečnost, Git a rozsah změn

Pracuj pouze v určeném projektu a podle nastavených oprávnění. Bez výslovného souhlasu nemaž ani hromadně nepřesouvej soubory, nepřepisuj sdílené šablony a nepřidávej závislosti nebo nástroje do systému. Neotevírej ani nezveřejňuj osobní údaje žáků, přístupové údaje či tajné klíče, pokud to není nezbytné pro výslovně zadanou bezpečnou operaci. Změny udržuj malé a přehledné; nepřeformátovávej nesouvisející části. Před rozsáhlými změnami předlož krátký plán. Po práci stručně shrň provedené úpravy, matematické ověření, výsledek kompilace a případná omezení. Git commity neprováděj bez zadání; před commitem ukaž, co se změnilo.

