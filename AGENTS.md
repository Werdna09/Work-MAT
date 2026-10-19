# Pokyny pro AI agenta – matematické výukové materiály

## Účel projektu

Repozitář slouží středoškolskému učiteli matematiky k tvorbě učebnice, příprav na vyučování, testů a pracovních listů. Výsledné výukové materiály vytvářej v českém jazyce a v LaTeXu, pokud uživatel výslovně nepožaduje jinak. Vždy respektuj požadovaný ročník, úroveň žáků, rozsah učiva a účel dokumentu. Neznámé důležité parametry si vyjasni; u drobností zvol přiměřený předpoklad a uveď jej.

## Organizace projektu a tematické plány

Primární struktura projektu je podle ročníků (`1_rocnik/` až `4_rocnik/`) a uvnitř podle tematických celků. Jejich názvy a pořadí určují skutečné tematické plány; nepředpokládej je podle obecného kurikula. Každý ročník může mít v `tematicke_plany/` dva plány: SPŠ (společný pro strojírenské a informatické obory) a GYM (gymnázium). Při práci s konkrétním ročníkem prostuduj relevantní plán, pokud je dostupný, a zohledni návaznost učiva a časovou dotaci. Rozdíly mezi plány případně uveď, ale neber je jako nepřekročitelnou hranici obsahu či obtížnosti.

Učebnice, přípravy a pracovní listy jsou společné pro SPŠ i gymnázium; nerozděluj je automaticky podle typu školy. Materiály vybírá a přizpůsobuje učitel podle konkrétní třídy. Tematický celek může podle potřeby obsahovat `ucebnice/`, `pripravy/`, `pracovni_listy/` a `testy/`, ale nevytvářej prázdné struktury bez důvodu. Stávající kořenové složky se mohou používat do dokončení reorganizace; nic z nich nepřesouvej bez schválení. Původní repozitář `~/ucebnice/` slouží jako archiv a zdroj inspirace; bez výslovného pokynu jej neupravuj.

## Existující podklady a šablony

Než začneš tvořit nebo upravovat dokument, prohlédni související soubory, šablony, makra a vzorové materiály dostupné v repozitáři. Přednost mají skutečné soubory projektu před obecnými pravidly uvedenými zde. Nevydávej níže popsané zvyklosti za ověřené vlastnosti projektu, dokud nenajdeš odpovídající soubory. Pokud podklady chybějí, stručně upozorni, že pracuješ bez vzoru.

Zachovávej existující členění projektu, názvy souborů a kompilovací postup. Nevytvářej duplicitní šablony, nadbytečné adresáře ani nová makra, jestliže stávající řešení stačí. Případné rozdíly mezi šablonami nepřepisuj plošně bez souhlasu.

## Autorský styl a matematické značení

Zachovej především autorův styl formátování LaTeXu: strukturu dokumentu, členění na odstavce, způsob zápisu rovnic, prostředí, odsazování a prostorové uspořádání. Druhotně zachovej styl vyjadřování. Upřednostňuj souvislý, plynulý a srozumitelný matematický výklad před zbytečným množstvím nadpisů, seznamů a vizuálních bloků. Při revizi měň jen to, co je nutné pro věcnou, jazykovou či didaktickou správnost.

Používej konzistentní českou matematickou terminologii, správnou symboliku a návaznost na dříve zavedené pojmy. Definice, tvrzení, důkazy a příklady rozlišuj podle vzorů projektu. Není-li doložena autorova volba, nevynucuj své oblíbené značení ani vlastní úpravu vzhledu.

## Učebnice

Při pokračování učebnice si přečti navazující části a ověř, jak jsou zavedeny pojmy a značení. Je-li v projektu soubor `ucebnice.sty` a prostředí jako `definition`, `example`, `solution` nebo příkaz `\historybox`, používej je v souladu se skutečnou definicí a existujícími příklady. Nevkládej do textu nové stylové balíčky ani nepřepisuj preambuli bez důvodu. Nevytvářej izolovanou kapitolu odlišnou stylem od zbytku učebnice.

Výklad má být odborně přesný, ale přístupný středoškolákům. Vysvětluj motivaci, podmínky platnosti a význam prováděných kroků; nepřeskakuj podstatné úvahy. Historické poznámky a citace používej jen s doložitelným zdrojem, nikdy je nevymýšlej.

## Testy a varianty

Před vytvořením testu vyhledej aktuální šablonu. Použij existující rozložení a hlavičku. Pokud je relevantní autorova šablona se dvěma testy formátu A5 na jedné A4 na šířku, zachovej tento způsob sazby; nevnucuj jej ale každému zadání. Hlavička podle používaného vzoru obsahuje jméno, třídu, datum, body a známku.

Varianty tvoř pouze v požadovaném rozsahu. Používej dvojice A/B, C/D a E/F pro standardní obtížnost (primárně SPŠ) a G/H, I/J a K/L pro vyšší obtížnost (primárně GYM). Toto rozdělení je výchozí konvence, nikoli zákaz použít libovolnou variantu v jiné třídě. V každé dvojici zajisti srovnatelnou obtížnost, časovou náročnost, rozsah a bodování. Není nutné měnit pouze čísla; různé úlohy však musí testovat srovnatelné dovednosti. Nepředpokládej, že jsou vždy požadovány všechny varianty.

Připrav řešení a případně bodovací schéma odděleně od zadání pro žáky. Nepřidávej kalkulačku, tabulky ani jiné pomůcky, pokud jejich použití nebylo povoleno. Jestliže chybí informace zásadní pro zadání testu (například rozsah látky nebo povolené pomůcky), vyžádej si ji před tvorbou.

## Pracovní listy

Vycházej z probíraného tématu a úrovně žáků. Pokud uživatel neurčí jinak, řaď úlohy od základního porozumění přes běžné procvičení po náročnější aplikace. U listů určených k vyplňování ponechávej přiměřené místo na výpočty, zápis nebo náčrtek; u vzorových listů respektuj jejich dosavadní úspornou sazbu. Pro grafy a geometrické obrázky používej přednostně zavedené nástroje projektu (například TikZ či pgfplots), pokud jsou vhodné. Výsledky a řešení udržuj oddělené od žákovské verze, není-li zadáno jinak.

## Přípravy na hodiny

Vycházej z učebnice, relevantního tematického plánu a zadaného ročníku, délky hodiny a výukového cíle. Podle potřeby navrhni motivaci, návaznost na předchozí učivo, výklad, typické chyby, otázky pro žáky, aktivitu, procvičení a orientační časový plán. Nepovažuj časové odhady za zaručené; upozorni, pokud je navržený obsah na danou hodinu příliš rozsáhlý. Rozlišuj interní metodickou přípravu učitele od materiálu pro žáky.

## Matematická kontrola

Každé nově vytvořené zadání i řešení zkontroluj. Ověř definiční obory, předpoklady, ekvivalenci úprav, správnost výpočtů, jednotky, grafy a jednoznačnost otázky. Kde je to praktické, použij nezávislou metodu: zpětné dosazení, symbolický či numerický výpočet, kontrolu krajních případů nebo jiný postup. Pouhé opakované přečtení stejného řešení nepovažuj za nezávislé ověření. Pokud kontrolu nelze provést, výslovně to sděl; netvrď, že bylo ověřeno něco, co ověřeno nebylo.

## Kompilace a kontrola výstupu

Po vytvoření či změně LaTeXového dokumentu použij existující překladač a nastavení projektu (např. `latexmk`), pokud jsou dostupné. Zkontroluj protokol, chyby a významná varování. Je-li možné prohlédnout výsledné PDF, zkontroluj též diakritiku, matematickou sazbu, přetékání obsahu, velikosti grafů, rozvržení stránek a čitelnost při tisku. Pokud PDF vizuálně nezkontroluješ, nepředstírej opak. Sděl, které soubory vznikly a zda kompilace proběhla úspěšně.

## Bezpečnost, Git a rozsah změn

Pracuj pouze v určeném projektu a podle nastavených oprávnění. Bez výslovného souhlasu nemaž ani hromadně nepřesouvej soubory, nepřepisuj sdílené šablony a nepřidávej závislosti nebo nástroje do systému. Neotevírej ani nezveřejňuj osobní údaje žáků, přístupové údaje či tajné klíče, pokud to není nezbytné pro výslovně zadanou bezpečnou operaci. Změny udržuj malé a přehledné; nepřeformátovávej nesouvisející části. Před rozsáhlými změnami předlož krátký plán. Po práci stručně shrň provedené úpravy, matematické ověření, výsledek kompilace a případná omezení.

