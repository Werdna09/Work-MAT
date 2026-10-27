# Kontrola sady Kombinatorika, hodiny 29–41, 4. ročník SPŠ

Datum dokončení: 27. 10. 2026.

**Verdikt: bez zjištěné matematické chyby ve finální sadě.** Skutečně zkontrolováno všech 13 příprav, jejich výklad, podmínky vzorců a všech 122 číslovaných položek (121 převzatých položek plus opakování 39/C5 v 41/B1). Hodina 40 je metodická a neobsahuje číslované matematické zadání. Tento verdikt vyjadřuje rozsah provedené kontroly, nikoli absolutní záruku.

Pracovní postup odpovídal skillům `vytvor-pripravu` a `over-matematiku`. Skill `vytvor-test` byl respektován jako hranice budoucí samostatné tvorby testu; žádný žákovský test ani jeho varianty nevznikly. Sada byla tvořena a kontrolována po blocích 29–31, 32–34, 35–38 a 39–41.

## Výstupy

Všechny dokumenty jsou samostatně kompilovatelné, načítají `../../sablony/pripravy/priprava.sty` a PDF leží vedle zdrojů. Podle výslovného zadání učitele jsou cíle, předpoklady a časové rozvržení součástí učitelských poznámek. Rozsáhlejší zásoba úloh je rozlišena na práci v hodině, rezervu a domácí procvičení.

| Hodina a název | LaTeX | PDF | Stran | Kompilace | Matematická kontrola |
|---|---|---|---:|---|---|
| 29 – Úvod do kombinatoriky | [29_KMB_UvodDoKombinatoriky.tex](29_KMB_UvodDoKombinatoriky.tex) | [29_KMB_UvodDoKombinatoriky.pdf](29_KMB_UvodDoKombinatoriky.pdf) | 3 | OK | bez zjištěné chyby |
| 30 – Pravidlo součtu a součinu | [30_KMB_PravidloSouctuASoucinu.tex](30_KMB_PravidloSouctuASoucinu.tex) | [30_KMB_PravidloSouctuASoucinu.pdf](30_KMB_PravidloSouctuASoucinu.pdf) | 3 | OK | bez zjištěné chyby |
| 31 – Faktoriál | [31_KMB_Faktorial.tex](31_KMB_Faktorial.tex) | [31_KMB_Faktorial.pdf](31_KMB_Faktorial.pdf) | 3 | OK | bez zjištěné chyby |
| 32 – Permutace bez opakování; úvod do variací | [32_KMB_PermutaceBezOpakovaniAVariace.tex](32_KMB_PermutaceBezOpakovaniAVariace.tex) | [32_KMB_PermutaceBezOpakovaniAVariace.pdf](32_KMB_PermutaceBezOpakovaniAVariace.pdf) | 3 | OK | bez zjištěné chyby |
| 33 – Permutace s opakováním | [33_KMB_PermutaceSOpakovanim.tex](33_KMB_PermutaceSOpakovanim.tex) | [33_KMB_PermutaceSOpakovanim.pdf](33_KMB_PermutaceSOpakovanim.pdf) | 3 | OK | bez zjištěné chyby |
| 34 – Variace s opakováním | [34_KMB_VariaceSOpakovanim.tex](34_KMB_VariaceSOpakovanim.tex) | [34_KMB_VariaceSOpakovanim.pdf](34_KMB_VariaceSOpakovanim.pdf) | 3 | OK | bez zjištěné chyby |
| 35 – Kombinace bez opakování | [35_KMB_KombinaceBezOpakovani.tex](35_KMB_KombinaceBezOpakovani.tex) | [35_KMB_KombinaceBezOpakovani.pdf](35_KMB_KombinaceBezOpakovani.pdf) | 3 | OK | bez zjištěné chyby |
| 36 – Kombinační číslo | [36_KMB_KombinacniCislo.tex](36_KMB_KombinacniCislo.tex) | [36_KMB_KombinacniCislo.pdf](36_KMB_KombinacniCislo.pdf) | 3 | OK | bez zjištěné chyby |
| 37 – Vlastnosti kombinačních čísel | [37_KMB_VlastnostiKombinacnichCisel.tex](37_KMB_VlastnostiKombinacnichCisel.tex) | [37_KMB_VlastnostiKombinacnichCisel.pdf](37_KMB_VlastnostiKombinacnichCisel.pdf) | 3 | OK | bez zjištěné chyby |
| 38 – Pascalův trojúhelník | [38_KMB_PascaluvTrojuhelnik.tex](38_KMB_PascaluvTrojuhelnik.tex) | [38_KMB_PascaluvTrojuhelnik.pdf](38_KMB_PascaluvTrojuhelnik.pdf) | 3 | OK | bez zjištěné chyby |
| 39 – Binomická věta | [39_KMB_BinomickaVeta.tex](39_KMB_BinomickaVeta.tex) | [39_KMB_BinomickaVeta.pdf](39_KMB_BinomickaVeta.pdf) | 3 | OK | bez zjištěné chyby |
| 40 – Průběžný test z kombinatoriky | [40_KMB_PrubeznyTest.tex](40_KMB_PrubeznyTest.tex) | [40_KMB_PrubeznyTest.pdf](40_KMB_PrubeznyTest.pdf) | 2 | OK | bez zjištěné chyby (metodika, rozsah) |
| 41 – Smíšené kombinatorické úlohy | [41_KMB_SmiseneKombinatorickeUlohy.tex](41_KMB_SmiseneKombinatorickeUlohy.tex) | [41_KMB_SmiseneKombinatorickeUlohy.pdf](41_KMB_SmiseneKombinatorickeUlohy.pdf) | 4 | OK | bez zjištěné chyby |

Celkem vzniklo **13 souborů `.tex`, 13 PDF a tento kontrolní report; PDF mají dohromady 39 stran**.

## Chyba ve zdroji a její oprava

- **`import_hodiny/31_Faktorial.tex`, Metodické poznámky, druhá odrážka** → neomezeně zapsaná nerovnost `(a+b)! ≠ a!+b!` není univerzálně pravdivá → například pro `a=b=1` se obě strany rovnají 2 → ve finální hodině 31 je vysvětleno, že neexistuje obecné pravidlo pro rozdělení faktoriálu přes součet; protipříklad k takovému pravidlu je `(2+3)!=120`, ale `2!+3!=8` → **důležité**, jde o opravu formulace matematického tvrzení. Původní import zůstal beze změny.

V číselných výsledcích převzatých úloh nebyla nalezena chyba. Jejich hodnoty zůstaly zachovány.

## Upřesnění zadání a podmínek

Jde o odstranění implicitních předpokladů a doplnění vysvětlení, nikoli o nahrazení původních úloh jinými číselnými příklady.

| Zdrojové místo | Upřesnění ve finální přípravě |
|---|---|
| 29, C3 | Nevysvětlené značky stran mince H/T nahrazeny vysvětlenými L/R (líc/rub); čtyři výsledky se nemění. |
| 30, P4–P5 | Výslovná otázka na počet; u P5 je dovoleno opakování na nesousedních místech. Strom voleb vysvětlen tabulkou větví. |
| 31, P5 a C3 | Výslovně stanoven obor n ∈ ℕ₀, u rovnic požadovány nezáporné argumenty všech faktoriálů. |
| 32, P3–P5, C3–C5 | Doplněny úplné otázky na počet a předpoklad různých osob; u výsledku závodu bez dělených umístění, u funkcí různí nositelé. |
| 33, C1, C3–C5 | Zkratkovité pokyny „přeskup“ doplněny otázkou na počet; žetony stejné barvy jsou výslovně nerozlišitelné. |
| 34, P4–P5, C3–C4 | Explicitní povolení opakování, délka kódu místo „trojciferného kódu“, X/A skutečně patří do nabízené abecedy. |
| 35, P1, P3, C1, C3, C5 | Skupiny bez rozlišených funkcí, přesné velikosti a výslovné otázky na počty. Podmínky geometrických úloh zachovány. |
| 36, P3–P4, C3–C5 | Celočíselný obor, úplné vyřazení nepřípustných kořenů a zkoušky. Krajní výběry rozepsány. |
| 37, P5 | Celá n≥1, 1≤k≤n; faktor n/k má nenulový jmenovatel; doplněn i nezávislý důkaz dvojím počítáním. |
| 38, P4, C4–C5 | Jednotkové kroky jen doprava a nahoru; pro cestu přes bod uvedeny podmínky jeho dosažitelnosti. |
| 39, výklad | Reálné a,b, celočíselný exponent; případ n=0 vysvětlen jako identita konstantních polynomů. Rozlišeny index členu a exponent x, umocňování celého číselného koeficientu a znaménka. |
| 41, P1–P3, P6, C1–C6 | U komisí nerozlišené role; A/X součást abecedy a opakování výslovně dovoleno; binární abeceda {0,1}; u cest jednotkové kroky doprava/nahoru. |

## Soulad s rozpisem, kolize a úplnost

- Číslování a pořadí 29–41 odpovídá `4_rocnik/tematicke_plany/Rozpis_vyuky_MAT_4_rocnik.tex`, řádkům 29–41. Záhlaví používají stručné názvy témat, podrobnosti z rozpisu jsou rozvedeny uvnitř příprav.
- Rozpis v hodině 32 výslovně jmenuje permutace bez opakování. Import přidává úvod do variací bez opakování; tento rozdíl je uveden v přípravě. Zařazení variací do stejné hodiny je v souladu s výslovným zadáním učitele a předchází variacím s opakováním i testu.
- Hodina 40 dodržuje test T3 z variací, permutací a kombinací v délce 15–20 minut (doporučená konkrétní organizace: 3–21 min, tedy 18 minut). Binomická věta a důkazy identit nejsou automaticky přidány do rozsahu testu. Nejde o celohodinovou písemnou práci.
- Zdroj hodiny 40 obsahuje deset konkrétních diagnostických a opravných položek a zmínku o bodování. Tyto položky ani bodování nebyly do nové přípravy přetištěny podle výslovného požadavku nevytvářet testové zadání. Zachovány jsou jejich diagnostické cíle: pořadí, opakování, počáteční nula, nerozlišitelné kopie, volba modelu. Následná náprava odkazuje na již vypracované příklady v ostatních hodinách. Nejde o opomenutí učiva.
- V hodině 41 je navíc B1, totožná s původní 39/C5. Jde o dohledatelné opakování binomické věty v rámci rozsahu 2.1–2.3, nikoli o nové číselné zadání.
- Starší nečíslované `Uvod_do_kombinatoriky.tex` a `.pdf` zůstaly beze změny. Nová 29 je samostatná číslovaná příprava vyžádané sady; původní materiál nebyl přepsán ani přejmenován.
- Výklad a všechny původní P a C položky z hodin 29–39 a 41 jsou přítomny. Označení P odpovídá sekci „Řešené příklady“, C sekci „Procvičování pro studenty“ příslušného importu. Rozšířena jsou zejména zdůvodnění modelů, důkazy úplnosti případů a podmínky vzorců.
- Související tematický plán SPŠ byl přečten. `ucebnice/09_Kombinatorika/` neobsahuje obsahovou kapitolu a mezi místními pracovními listy ani externími zdroji nebyl nalezen odpovídající kombinatorický podklad. Hlavním zdrojem je všech třináct výslovně určených importů, včetně jejich PDF. Konkrétní lekce Realisticky.cz nebyly použity ani prohlášeny za samostatně ověřené.

## Nezávislá kontrola vzorců a důkazů

| Rozsah | Nezávislá kontrola a podmínky | Stav |
|---|---|---|
| Součet a součin (30) | Úplnost a disjunktnost větví; každý sled voleb odpovídá právě jednomu výsledku. U součinu ověřen stálý počet pokračování, nikoli požadavek stejné nabídky. | bez zjištěné chyby |
| Faktoriály (31) | Přesný rozvoj a vytknutí činitele; n=0 a kladnost jmenovatelů. U rovnic ekvivalentní kvadratická rovnice dokazuje úplnost, dosazení dává zpětnou kontrolu. | bez zjištěné chyby |
| Permutace/variace (32–34) | Postupné volby, jedinečnost bloku i rozpojení; stejné počty očíslovaných kopií. Ověřeny prázdné výběry a podmínka k≤n bez opakování; u opakování k může být větší než n. | bez zjištěné chyby |
| Kombinace (35–36) | Každá k-prvková skupina má přesně k! pořadí; krajní k=0,n. Geometrické objekty jednoznačně odpovídají výběrům bodů při uvedených podmínkách. | bez zjištěné chyby |
| Symetrie a Pascalův vztah (37) | Vzájemné přiřazení skupiny a doplňku; rozdělení podle přítomnosti pevné osoby. Vztah používán pouze pro vnitřní indexy, kraje zvlášť. | bez zjištěné chyby |
| Součet podmnožin a liché výběry (37) | Charakteristické posloupnosti ano/ne, párování změnou přítomnosti jednoho pevného prvku. P5 navíc dvojí počítání komise s vedoucím. | bez zjištěné chyby |
| Trojúhelník a mřížka (38) | Rekurze sousedních součtů porovnána s výpisy podmnožin; cesty přímo vypsány jako řetězce D/N a filtrovány podle návštěvy bodu. Náčrt zkontrolován vůči souřadnicím. | bez zjištěné chyby |
| Binomická věta (39) | Úplný výběr členů z n závorek; konkrétní rozvoje nezávisle přímým násobením polynomů bez binomických koeficientů. | bez zjištěné chyby |
| Smíšené úlohy (41) | Přímé filtrování všech kódů, čísel či skupin místo použitých doplňků a součinů. Ověřeno vzájemné vylučování a úplnost číselných případů. | bez zjištěné chyby |
| Metodická příprava (40) | Rozsah odpovídá rozpisu, žádné nové učivo ani testové varianty; odkazy k nápravě vedou na odpovídající skutečné příklady. | bez zjištěné chyby |

Výpočetní kontrola používá pouze standardní knihovnu Pythonu (`itertools`, `math`, přesná celá čísla a vlastní násobení polynomů). U konečných úloh proběhl úplný výpis, nikoli náhodné vzorkování. U obecných identit je kontrola do n=30 pouze podpůrná; obecnou platnost dokládá zvlášť prověřený důkaz. Nebyly instalovány žádné závislosti.

## Výsledky po jednotlivých úlohách

P a C jsou navázány na doslovná zdrojová zadání v komentářích `.tex`. U každé položky byly posouzeny pořadí, opakování, další omezení, úplnost a soulad slovního modelu s výpočtem. Následující tabulky zaznamenávají konkrétní druhou kontrolní metodu; neomezují kontrolu pouze na konečné číslo.

### Hodina 29: Úvod do kombinatoriky

Zdroj: [29_Uvod_do_kombinatoriky.tex](../../import_hodiny/29_Uvod_do_kombinatoriky.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 6 | bez zjištěné chyby | úplný výpis uspořádání |
| P2 | 3 | bez zjištěné chyby | sloučení dvojic lišících se pouze pořadím |
| P3 | 6 komisí; 12 obsazení míst | bez zjištěné chyby | úplný výpis obou druhů výběru |
| P4 | 27 | bez zjištěné chyby | úplný výpis kódů |
| C1 | 6 | bez zjištěné chyby | množiny dvojic |
| C2 | 6 | bez zjištěné chyby | úplný výpis obsazení židlí |
| C3 | LL, LR, RL, RR; 4 | bez zjištěné chyby | úplný výpis výsledků |
| C4 | pořadí ne; opakování ne | bez zjištěné chyby | záměna pořadí zachovává množinu, osoba se neopakuje |
| C5 | pořadí ano; opakování ano; úvodní nula ano | bez zjištěné chyby | přípustný PIN s počáteční nulou a opakováním |

### Hodina 30: Pravidlo součtu a součinu

Zdroj: [30_Pravidlo_souctu_a_soucinu.tex](../../import_hodiny/30_Pravidlo_souctu_a_soucinu.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 7 | bez zjištěné chyby | sjednocení disjunktních označených tarifů |
| P2 | 15 | bez zjištěné chyby | výpis všech dvojic |
| P3 | 4536 | bez zjištěné chyby | úplný průchod čtyřciferných čísel |
| P4 | 12 | bez zjištěné chyby | test číslic a dělitelnosti ve všech trojciferných číslech |
| P5 | 108 | bez zjištěné chyby | úplný výpis s filtrem sousednosti |
| C1 | 12 | bez zjištěné chyby | výpis dvojic |
| C2 | 12 | bez zjištěné chyby | sjednocení disjunktních cest |
| C3 | 1296 | bez zjištěné chyby | úplný výpis kódů |
| C4 | 180 | bez zjištěné chyby | úplný průchod trojciferných čísel |
| C5 | 48 | bez zjištěné chyby | úplný výpis s filtrem |

### Hodina 31: Faktoriál

Zdroj: [31_Faktorial.tex](../../import_hodiny/31_Faktorial.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 720; 56 | bez zjištěné chyby | výpis pořadí a dvojic; navíc ručně zkrácen poměr |
| P2 | (n+2)(n+1), n ∈ ℕ₀ | bez zjištěné chyby | přesná kontrola n=0…30 podpůrně; obecná platnost ručně z rozvoje faktoriálu |
| P5 | n+2, n ∈ ℕ₀ | bez zjištěné chyby | přesná kontrola n=0…30 podpůrně; obecná platnost ručně z rozvoje faktoriálu |
| C3 | (n+3)(n+2), n ∈ ℕ₀ | bez zjištěné chyby | přesná kontrola n=0…30 podpůrně; obecná platnost ručně z rozvoje faktoriálu |
| P3 | 36 | bez zjištěné chyby | výpis neuspořádaných dvojic místo faktoriálového zlomku |
| P4 | n=5 | bez zjištěné chyby | přesné dosazení; úplnost rozkladem kvadratické rovnice a podmínkou n≥1 |
| C1 | 120 | bez zjištěné chyby | výpis uspořádání |
| C2 | 110 | bez zjištěné chyby | výpis uspořádaných dvojic |
| C4 | 21 | bez zjištěné chyby | výpis neuspořádaných dvojic |
| C5 | n=7 | bez zjištěné chyby | dosazení; úplnost přes (n−7)(n+6) a definiční obor |

### Hodina 32: Permutace bez opakování

Zdroj: [32_Permutace_bez_opakovani.tex](../../import_hodiny/32_Permutace_bez_opakovani.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 720 | bez zjištěné chyby | úplný výpis všech pořadí |
| P2 | 240 | bez zjištěné chyby | filtr sousedství v úplném výpisu |
| P3 | 480 | bez zjištěné chyby | přímý filtr nesousedství místo odečítání |
| P4 | 336 | bez zjištěné chyby | výpis výsledků medailových pozic |
| P5 | 2160 | bez zjištěné chyby | výpis všech sedmiciferných uspořádání s filtrem parity |
| C1 | 120 | bez zjištěné chyby | výpis uspořádání knih |
| C2 | 90 | bez zjištěné chyby | výpis dvojic závodníků s rozlišenými rolemi |
| C3 | 24 | bez zjištěné chyby | výpis řad s pevnou první osobou |
| C4 | 210 | bez zjištěné chyby | výpis trojic funkcionářů |
| C5 | 240 | bez zjištěné chyby | přímá kontrola sousedství |

### Hodina 33: Permutace s opakováním

Zdroj: [33_Permutace_s_opakovanim.tex](../../import_hodiny/33_Permutace_s_opakovanim.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 60 | bez zjištěné chyby | očíslované kopie sloučeny do shodných viditelných slov |
| P2 | 30 | bez zjištěné chyby | množina všech různých přeskupení |
| P3 | 35 | bez zjištěné chyby | výpis binárních řetězců s filtrem počtu jedniček |
| P4 | 12 | bez zjištěné chyby | přímý filtr souvislého AAA ve všech slovech |
| P5 | 21 | bez zjištěné chyby | výpis všech barevných řad s pevnou četností |
| C1 | 30 | bez zjištěné chyby | množina různých přeskupení |
| C2 | 10 | bez zjištěné chyby | výpis binárních řad |
| C3 | MMAA, AMMA, AAMM; 3 | bez zjištěné chyby | přímý výpis slov se sousedními M |
| C4 | 560 | bez zjištěné chyby | množina různých barevných uspořádání |
| C5 | 20 | bez zjištěné chyby | přímý filtr NN ve všech přeskupeních |

### Hodina 34: Variace s opakováním

Zdroj: [34_Variace_s_opakovanim.tex](../../import_hodiny/34_Variace_s_opakovanim.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 10000 | bez zjištěné chyby | úplný výpis PINů |
| P2 | 9000 | bez zjištěné chyby | počet celých čísel v intervalu |
| P3 | 120 bez opakování; 216 s opakováním | bez zjištěné chyby | úplné výpisy pro obě pravidla opakování |
| P4 | 27 | bez zjištěné chyby | přímý filtr právě jednoho A |
| P5 | 271 | bez zjištěné chyby | přímý filtr sedmičky místo doplňku |
| C1 | 243 | bez zjištěné chyby | úplný výpis |
| C2 | 20 | bez zjištěné chyby | úplný výpis bez opakování |
| C3 | 256 | bez zjištěné chyby | filtrování celé pětiznakové abecedy |
| C4 | 65 | bez zjištěné chyby | přímý filtr A místo doplňku |
| C5 | 1080 | bez zjištěné chyby | průchod všech čtyřciferných čísel a filtr cifer |

### Hodina 35: Kombinace bez opakování

Zdroj: [35_Kombinace_bez_opakovani.tex](../../import_hodiny/35_Kombinace_bez_opakovani.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 84 | bez zjištěné chyby | výpis neuspořádaných trojic |
| P2 | 15 | bez zjištěné chyby | sloučení dvojic podle krajních bodů; ruční kontrola geometrické jednoznačnosti |
| P3 | 150 | bez zjištěné chyby | výpis všech čtveřic a filtr počtu dívek |
| P4 | 35 | bez zjištěné chyby | přímý výpis nesousedních dvojic vrcholů místo odečtení stran |
| P5 | 30 | bez zjištěné chyby | přímý filtr právě jedné určené osoby |
| C1 | 28 | bez zjištěné chyby | výpis dvojic |
| C2 | 35 | bez zjištěné chyby | výpis trojic a ruční kontrola nekolinearity v předpokladu |
| C3 | 60 | bez zjištěné chyby | přímý filtr počtu mužů |
| C4 | 10 | bez zjištěné chyby | výpis dvojic karet |
| C5 | 56 | bez zjištěné chyby | přímý filtr předepsaného hráče |

### Hodina 36: Kombinační číslo

Zdroj: [36_Kombinacni_cislo.tex](../../import_hodiny/36_Kombinacni_cislo.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 120 | bez zjištěné chyby | výpis skupin místo faktoriálového výpočtu |
| P2 | 66 | bez zjištěné chyby | přímý výpis desetiprvkových skupin |
| P3 | n=10 | bez zjištěné chyby | výpis dvojic; úplnost ručně kvadratickým rozkladem |
| P4 | n=7 | bez zjištěné chyby | výpis dvojic; úplnost ručně dělením kladným n |
| P5 | 15 | bez zjištěné chyby | přímý filtr dvou povinných členů |
| C1 | 56 | bez zjištěné chyby | výpis trojic |
| C2 | 55 | bez zjištěné chyby | výpis devítiprvkových skupin |
| C3 | n=13 | bez zjištěné chyby | výpis singletonů; jednoznačnost n=13 z definice |
| C4 | n=8 | bez zjištěné chyby | výpis dvojic; úplnost rozkladem (n−8)(n+7) |
| C5 | 1; 1 | bez zjištěné chyby | přímý výpis úplné a prázdné skupiny |

### Hodina 37: Vlastnosti kombinačních čísel

Zdroj: [37_Vlastnosti_kombinacnich_cisel.tex](../../import_hodiny/37_Vlastnosti_kombinacnich_cisel.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 45 | bez zjištěné chyby | přímý výpis osmic bez symetrie |
| P2 | C(10,4)=210 | bez zjištěné chyby | výpis obou stran Pascalova vztahu |
| P3 | 126 bez P + 84 s P = 210 | bez zjištěné chyby | přímé rozdělení všech komisí podle přítomnosti P |
| P4 | 32 | bez zjištěné chyby | výpis charakteristických funkcí podmnožin |
| P5 | C(n,k) = n/k · C(n−1,k−1), 1≤k≤n | bez zjištěné chyby | podpůrná přesná kontrola do n=30; obecný důkaz nezávisle počítáním komisí s vedoucím |
| C1 | 12 | bez zjištěné chyby | přímý výpis jedenáctic |
| C2 | C(8,4)=70 | bez zjištěné chyby | výpis skupin místo použití identity |
| C3 | C(9,3)=84 | bez zjištěné chyby | výpis skupin obou velikostí |
| C4 | 64 | bez zjištěné chyby | výpis podmnožin po velikostech |
| C5 | 64 | bez zjištěné chyby | přímé filtrování lichých velikostí místo párování |

### Hodina 38: Pascalův trojúhelník

Zdroj: [38_Pascaluv_trojuhelnik.tex](../../import_hodiny/38_Pascaluv_trojuhelnik.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 1, 6, 15, 20, 15, 6, 1 | bez zjištěné chyby | rekurze sousedních součtů; porovnání s přímými počty podmnožin |
| P2 | 32 | bez zjištěné chyby | rekurze a přímý součet místo 2^n |
| P3 | 35 | bez zjištěné chyby | úplný výpis řetězců kroků |
| P4 | 18 | bez zjištěné chyby | přímý filtr návštěvy bodu místo součinu úseků |
| P5 | 28 | bez zjištěné chyby | rekurze Pascalova trojúhelníku |
| C1 | 1, 4, 6, 4, 1 | bez zjištěné chyby | rekurze sousedních součtů |
| C2 | 20 | bez zjištěné chyby | rekurze a indexování od nuly |
| C3 | 128 | bez zjištěné chyby | přímý součet rekurzivně získaného řádku |
| C4 | 10 | bez zjištěné chyby | úplný výpis kroků |
| C5 | 9 | bez zjištěné chyby | přímý filtr průchodu bodem |

### Hodina 39: Binomická věta

Zdroj: [39_Binomicka_veta.tex](../../import_hodiny/39_Binomicka_veta.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | x⁴+8x³+24x²+32x+16 | bez zjištěné chyby | opakované násobení mnohočlenů místo binomické věty |
| P2 | 8x³−12x²y+6xy²−y³ | bez zjištěné chyby | přímé násobení dvojrozměrných polynomů |
| P3 | 40 | bez zjištěné chyby | koeficient získán přímým roznásobením |
| P4 | 240 | bez zjištěné chyby | koeficient získán přímým roznásobením |
| P5 | Σ C(n,k)=2ⁿ, n≥0 | bez zjištěné chyby | podpůrná kontrola do n=30; obecná identita nezávisle počítáním podmnožin |
| C1 | a³+3a²b+3ab²+b³ | bez zjištěné chyby | přímé násobení polynomů |
| C2 | x⁴−4x³+6x²−4x+1 | bez zjištěné chyby | přímé roznásobení všech závorek |
| C3 | 54 | bez zjištěné chyby | přímý koeficient z násobení |
| C4 | 125 | bez zjištěné chyby | přímé roznásobení a kontrola x=0 |
| C5 | -80 | bez zjištěné chyby | přímé roznásobení, bez čtení binomického koeficientu |

### Hodina 40: Průběžný test z kombinatoriky

Zdroj: [40_Podklad_prubezny_test.tex](../../import_hodiny/40_Podklad_prubezny_test.tex).

Metodická kontrola bez zjištěné chyby: žádné číslované zadání ani varianty. Zkontrolována organizace, předepsaný rozsah a odkazy k nápravě.

### Hodina 41: Smíšené kombinatorické úlohy

Zdroj: [41_Smisene_kombinatoricke_ulohy.tex](../../import_hodiny/41_Smisene_kombinatoricke_ulohy.tex).

| Úloha | Výsledek | Stav | Nezávislá metoda / poznámka |
|---|---|---|---|
| P1 | 80 | bez zjištěné chyby | přímý filtr alespoň jedné ženy místo doplňku |
| P2 | 781 | bez zjištěné chyby | úplný výpis s filtrem přítomnosti A |
| P3 | 120+300=420 | bez zjištěné chyby | průchod všech čtyřciferných čísel a filtr místo součinů podle cifer |
| P4 | 480 | bez zjištěné chyby | přímý filtr nesousedství |
| P5 | 56 | bez zjištěné chyby | úplný výpis binárních řetězců |
| P6 | 30 | bez zjištěné chyby | přímý zákaz současného výběru obou |
| C1 | 36 | bez zjištěné chyby | přímý filtr alespoň jedné z A,B |
| C2 | 61 | bez zjištěné chyby | přímý filtr X |
| C3 | 10 | bez zjištěné chyby | úplný výpis s filtrem počtu jedniček |
| C4 | 48 | bez zjištěné chyby | přímý filtr sousedních knih |
| C5 | 90 | bez zjištěné chyby | úplný výpis skupin s filtrem počtu žen |
| C6 | 20 | bez zjištěné chyby | úplný výpis cest místo kombinačního čísla |
| B1 | -80 | bez zjištěné chyby | opakované násobení mnohočlenů; opakování 39/C5 |

## Technická a vizuální kontrola

- Každý dokument byl sestaven skutečným projektovým `scripts/build_latex.sh`; po úpravách byly příslušné dokumenty sestaveny znovu stejným postupem. Poslední kompilace všech 13 dokumentů jsou úspěšné a nehlásí `Overfull` ani `Underfull`.
- Byl ověřen počet stran pomocí `pdfinfo`, čitelnost všech PDF, umístění vedle `.tex`, počet prostředí a právě jeden `\tcblower` v každém spojeném boxu.
- Všech 39 výsledných stran bylo vykresleno a vizuálně prohlédnuto, včetně změněných stran po opravách. Kontrolována byla diakritika, rovnice, tabulky, nekolizní záhlaví, dělení boxů, Pascalův trojúhelník a náčrt mřížky. V hodině 36 bylo odstraněno oddělení krátkého zadání P3 od jeho řešení.
- Podpůrná kontrola souřadnic extrahovaného textu nenašla text mimo očekávané tiskové okraje. Tato kontrola nenahrazovala vizuální prohlídku.
- Hashová kontrola všech 50 původních souborů zahrnutých do vstupního snímku potvrdila zachování importů, plánů, šablon, projektových skillů, `AGENTS.md` i starší úvodní přípravy. Nevznikl commit ani push. Pomocné soubory kontrol a kompilace byly ponechány mimo adresář materiálů.

## Omezení a použití při výuce

Žádná požadovaná příprava ani PDF nechybí a nezůstává nedokončená kompilace nebo matematická kontrola. Časové odhady jsou metodickým návrhem, nikoli výsledkem ověření v konkrétní třídě. Zvláště hodiny 32, 37 a 41 mají širší zásobu úloh než je vhodné vyřešit povinně za 45 minut; přípravy konkrétně určují jádro, volitelnou rezervu a domácí práci. Reálné tempo upraví učitel podle znalostí třídy a výsledků testu.

Skutečný průběžný test záměrně nebyl vytvořen. Jeho konkrétní úlohy, případné varianty, podmínky a pomůcky budou řešeny samostatným postupem `vytvor-test` se schválením výběru učitelem. Toto omezení nebrání použití metodické přípravy hodiny 40.
