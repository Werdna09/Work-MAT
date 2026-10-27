# Kontrola příprav: mocniny, odmocniny a algebraické výrazy

Kontrola dokončena 27. 10. 2026. Vytvořeno 35 samostatných příprav ve formátech TEX a PDF, celkem 38 stran. Všechny výsledné strany byly vykresleny a vizuálně prohlédnuty.

## Rozsah a návaznost

- Mocniny a odmocniny: hodiny 25–40 včetně metodických příprav písemné práce 32 a průběžného testu 40.
- Algebraické výrazy: hodiny 41–58 včetně metodické přípravy testu 57. Doplněna je také společná pololetní hodina 69, kterou rozpis výslovně věnuje algebraickým výrazům a základům funkcí.
- Rozdělení učiva i hodinová dotace odpovídají `1_rocnik/tematicke_plany/Rozpis_vyuky_MAT_1_rocnik.tex`. Příprava 69 předpokládá probrání funkcí v hodinách 59–68; nezavádí jejich novou výuku a nezařazuje absolutní hodnotu plánovanou až na hodinu 70.
- Po ověření všech příslušných dvojic TEX/PDF byly pouze řádky „MOCNINY A ODMOCNINY“ a „ALGEBRAICKÉ VÝRAZY“ v `planovani/STAV_PRIPRAV.md` změněny na `HOTOVO`. Ostatní stavy zůstaly beze změny.

## Matematická a technická kontrola

Každé řešené i samostatné zadání bylo posouzeno včetně přípustných hodnot, znamének a výsledku. Přesná symbolická kontrola mnohočlenů a racionálních výrazů používá nezávislé roznásobení a křížové násobení s racionálními koeficienty. Rekurzivní vyhodnocování původních složených výrazů navíc kontrolovalo nulové vnitřní jmenovatele a nulové dělitele na zvolených kontrolních hodnotách. Úplné podmínky byly odvozeny také přímo z jednotlivých operací; konečný vzorek hodnot jejich obecné zdůvodnění nenahrazuje.

Odmocniny byly kontrolovány pomocí definice, zpětného umocnění, znaménka a nezávislého numerického výpočtu. U technických úloh byly zkontrolovány jednotky a převody. Obecná tvrzení o znaménku, prázdnosti oboru a přípustnosti úprav jsou zdůvodněna podmínkami pravidel, nikoli samotnou numerickou zkouškou. Podpůrné výpočty, logy a vykreslené stránky zůstávají mimo adresář materiálů.

Všech 35 dokumentů prošlo skutečným projektovým skriptem `scripts/build_latex.sh`, který spouští kontrolu struktury, kompilaci a ověření PDF. Poslední kompilace nehlásí `Overfull` ani `Underfull`. Každý spojený box má právě jeden oddělovač řešení. PDF leží vedle příslušného TEX, bez pomocných souborů v adresáři příprav. Byla vizuálně ověřena všechna záhlaví, česká diakritika, zlomky, exponenty, odmocniny, dělení stránek a čitelnost sazby.

Kontrolní otisky potvrdily zachování všech původních příprav, plánů, rozpisů, šablon, skillů i `AGENTS.md`. Jedinou změnou původního souboru je výše uvedená aktualizace dvou stavů. Nevznikl commit ani push.

## Přehled výstupů

| Hodina | Název | TEX | PDF | Stran |
|---|---|---|---|---:|
| 25 | Mocnina s přirozeným exponentem | [TEX](25_MOC_MocninaSPrirozenymExponentem.tex) | [PDF](25_MOC_MocninaSPrirozenymExponentem.pdf) | 1 |
| 26 | Součin a podíl mocnin | [TEX](26_MOC_SoucinAPodilMocnin.tex) | [PDF](26_MOC_SoucinAPodilMocnin.pdf) | 1 |
| 27 | Mocnina mocniny a součinu | [TEX](27_MOC_MocninaMocninySoucinAPodil.tex) | [PDF](27_MOC_MocninaMocninySoucinAPodil.pdf) | 1 |
| 28 | Nulový a záporný exponent | [TEX](28_MOC_NulovyAZapornyExponent.tex) | [PDF](28_MOC_NulovyAZapornyExponent.pdf) | 1 |
| 29 | Vědecký zápis a odhady | [TEX](29_MOC_VedeckyZapisAOdhady.tex) | [PDF](29_MOC_VedeckyZapisAOdhady.pdf) | 1 |
| 30 | Druhá a třetí odmocnina | [TEX](30_ODM_DruhaATretiOdmocnina.tex) | [PDF](30_ODM_DruhaATretiOdmocnina.pdf) | 1 |
| 31 | Mocniny s racionálním exponentem | [TEX](31_MOC_RacionalniExponent.tex) | [PDF](31_MOC_RacionalniExponent.pdf) | 1 |
| 32 | Čtvrtletní písemná práce | [TEX](32_MOC_CtvrtletniPisemnaPrace.tex) | [PDF](32_MOC_CtvrtletniPisemnaPrace.pdf) | 1 |
| 33 | Pravidla pro odmocniny | [TEX](33_ODM_PravidlaProOdmocniny.tex) | [PDF](33_ODM_PravidlaProOdmocniny.pdf) | 1 |
| 34 | Částečné odmocňování | [TEX](34_ODM_CastecneOdmocnovani.tex) | [PDF](34_ODM_CastecneOdmocnovani.pdf) | 1 |
| 35 | Usměrňování jednočlenného jmenovatele | [TEX](35_ODM_UsmernovaniJednohoClenu.tex) | [PDF](35_ODM_UsmernovaniJednohoClenu.pdf) | 1 |
| 36 | Usměrňování sdruženým výrazem | [TEX](36_ODM_SdruzeneVyrazy.tex) | [PDF](36_ODM_SdruzeneVyrazy.pdf) | 1 |
| 37 | Složené výrazy a podmínky | [TEX](37_ODM_SlozeneVyrazySMocninamiAOdmocninami.tex) | [PDF](37_ODM_SlozeneVyrazySMocninamiAOdmocninami.pdf) | 1 |
| 38 | Slovní a technické úlohy | [TEX](38_ODM_SlovniATechnickeUlohy.tex) | [PDF](38_ODM_SlovniATechnickeUlohy.pdf) | 1 |
| 39 | Opakování mocnin a odmocnin | [TEX](39_ODM_OpakovaniMocninAOdmocnin.tex) | [PDF](39_ODM_OpakovaniMocninAOdmocnin.pdf) | 1 |
| 40 | Průběžný test a rozbor | [TEX](40_ODM_PrubeznyTestMocninyAOdmocniny.tex) | [PDF](40_ODM_PrubeznyTestMocninyAOdmocniny.pdf) | 1 |
| 41 | Algebraický výraz a mnohočlen | [TEX](41_ALG_PojmyAMnohocleny.tex) | [PDF](41_ALG_PojmyAMnohocleny.pdf) | 2 |
| 42 | Sčítání a odčítání mnohočlenů | [TEX](42_ALG_ScitaniAOdcitaniMnohoclenu.tex) | [PDF](42_ALG_ScitaniAOdcitaniMnohoclenu.pdf) | 1 |
| 43 | Násobení mnohočlenu jednočlenem | [TEX](43_ALG_NasobeniJednoclenem.tex) | [PDF](43_ALG_NasobeniJednoclenem.pdf) | 1 |
| 44 | Násobení dvou mnohočlenů | [TEX](44_ALG_NasobeniMnohoclenu.tex) | [PDF](44_ALG_NasobeniMnohoclenu.pdf) | 1 |
| 45 | Dělení mnohočlenu jednočlenem | [TEX](45_ALG_DeleniMnohoclenuJednoclenem.tex) | [PDF](45_ALG_DeleniMnohoclenuJednoclenem.pdf) | 1 |
| 46 | Dělení mnohočlenů: algoritmus | [TEX](46_ALG_DeleniMnohoclenuMnohoclenem.tex) | [PDF](46_ALG_DeleniMnohoclenuMnohoclenem.pdf) | 1 |
| 47 | Dělení mnohočlenů se zbytkem | [TEX](47_ALG_DeleniSeZbytkem.tex) | [PDF](47_ALG_DeleniSeZbytkem.pdf) | 1 |
| 48 | Vytýkání společného činitele | [TEX](48_ALG_VytykaniASeskupovani.tex) | [PDF](48_ALG_VytykaniASeskupovani.pdf) | 1 |
| 49 | Druhé mocniny a rozdíl čtverců | [TEX](49_ALG_DruheMocninyARozdilCtvercu.tex) | [PDF](49_ALG_DruheMocninyARozdilCtvercu.pdf) | 1 |
| 50 | Kombinované rozklady | [TEX](50_ALG_KombinovaneRozklady.tex) | [PDF](50_ALG_KombinovaneRozklady.pdf) | 1 |
| 51 | Třetí mocniny a rozklady | [TEX](51_ALG_TretiMocninyARozklady.tex) | [PDF](51_ALG_TretiMocninyARozklady.pdf) | 2 |
| 52 | Lomené výrazy: podmínky a krácení | [TEX](52_ALG_LomeneVyrazyPodminkyAKraceni.tex) | [PDF](52_ALG_LomeneVyrazyPodminkyAKraceni.pdf) | 1 |
| 53 | Sčítání a odčítání lomených výrazů | [TEX](53_ALG_ScitaniAOdcitaniLomenychVyrazu.tex) | [PDF](53_ALG_ScitaniAOdcitaniLomenychVyrazu.pdf) | 1 |
| 54 | Násobení a dělení lomených výrazů | [TEX](54_ALG_NasobeniADeleniLomenychVyrazu.tex) | [PDF](54_ALG_NasobeniADeleniLomenychVyrazu.pdf) | 1 |
| 55 | Složené lomené výrazy | [TEX](55_ALG_SlozeneLomeneVyrazy.tex) | [PDF](55_ALG_SlozeneLomeneVyrazy.pdf) | 2 |
| 56 | Smíšené úpravy výrazů | [TEX](56_ALG_SmiseneUpravyVyrazu.tex) | [PDF](56_ALG_SmiseneUpravyVyrazu.pdf) | 1 |
| 57 | Průběžný test a rozbor | [TEX](57_ALG_PrubeznyTestAlgebraickeVyrazy.tex) | [PDF](57_ALG_PrubeznyTestAlgebraickeVyrazy.pdf) | 1 |
| 58 | Opakování a ověřování úprav | [TEX](58_ALG_OpakovaniAOverovaniUprav.tex) | [PDF](58_ALG_OpakovaniAOverovaniUprav.pdf) | 1 |
| 69 | Pololetní písemná práce | [TEX](69_ALG_PololetniPisemnaPrace.tex) | [PDF](69_ALG_PololetniPisemnaPrace.pdf) | 1 |

## Použité podklady a metodika

Závazným zdrojem rozsahu je ročníkový rozpis a plán SPŠ. Výklad vychází především z těchto kapitol:

- `ucebnice/01_Zakladni_poznatky/Mocniny_a_odmocniny/Mocniny a Odmocniny.tex`;
- `ucebnice/01_Zakladni_poznatky/Algebraicke_vyrazy/Algebraické výrazy.tex`;
- pro společnou hodinu 69 také `ucebnice/02_Funkce_a_rovnice/Zaklady_funkci/Funkce.tex`, pojem funkce a práce s lineárním předpisem.

V komentářích jednotlivých TEX je zaznamenán původ převzatých příkladů, vlastní tvorba i metodické zdroje. Zadané výrazy ze sešitu jsou v hodinách 28 (mocniny s parametrem), 36 (usměrnění), 47 (dělení se zbytkem), 51 (náročný rozklad); složené lomené výrazy s podmínkami v hodinách 55–56.

Ve stažených lekcích Realisticky.cz byly prostudovány relevantní výkladové části, metodické poznámky a vybrané ukázky gradace úloh. Převzata je inspirace postupným odvozováním, vlastním pokusem žáků a kontrolou po menších krocích. Přípravy obsahují vlastní formulace; cizí lekce ani jejich soubory příkladů nebyly doslovně přebírány. Veřejná zdrojová PDF jsou uložena přímo v `externi_zdroje/realisticky/`, nikoli v `/tmp`. Již přítomné podklady nebyly přepsány.

| Studijní lekce | Místní PDF | Původní adresa |
|---|---|---|
| 07 Druhá odmocnina | [PDF](../../externi_zdroje/realisticky/Odmocniny/07_Druha_odmocnina.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/02%20%C4%8C%C3%ADseln%C3%A9%20obory/07%20Druh%C3%A1%20odmocnina.pdf) |
| 08 Třetí odmocnina | [PDF](../../externi_zdroje/realisticky/Odmocniny/08_Treti_odmocnina.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/02%20%C4%8C%C3%ADseln%C3%A9%20obory/08%20T%C5%99et%C3%AD%20odmocnina.pdf) |
| 09 Usměrňování zlomků | [PDF](../../externi_zdroje/realisticky/Odmocniny/09_Usmernovani_zlomku.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/02%20%C4%8C%C3%ADseln%C3%A9%20obory/09%20Usm%C4%9Br%C5%88ov%C3%A1n%C3%AD%20zlomk%C5%AF.pdf) |
| 01 Mocniny s přirozeným mocnitelem | [PDF](../../externi_zdroje/realisticky/Mocniny/01_MocninySPrirozenymMocnitelem.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/01%20Mocniny%20s%20p%C5%99irozen%C3%BDm%20mocnitelem.pdf) |
| 02 Vzorce pro mocniny I | [PDF](../../externi_zdroje/realisticky/Mocniny/02_Vzorce_pro_mocniny_I.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/02%20Vzorce%20pro%20mocniny%20I.pdf) |
| 03 Vzorce pro mocniny II | [PDF](../../externi_zdroje/realisticky/Mocniny/03_Vzorce_pro_mocniny_II.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/03%20Vzorce%20pro%20mocniny%20II.pdf) |
| 04 KISS | [PDF](../../externi_zdroje/realisticky/Mocniny/04_KISS.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/04%20KISS.pdf) |
| 05 Mocniny s celým mocnitelem I | [PDF](../../externi_zdroje/realisticky/Mocniny/05_Mocniny_s_celym_mocnitelem_I.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/05%20Mocniny%20s%20cel%C3%BDm%20mocnitelem%20I.pdf) |
| 06 Mocniny s celým mocnitelem II | [PDF](../../externi_zdroje/realisticky/Mocniny/06_Mocniny_s_celym_mocnitelem_II.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/06%20Mocniny%20s%20cel%C3%BDm%20mocnitelem%20II.pdf) |
| 07 Mocniny s proměnnou v mocniteli | [PDF](../../externi_zdroje/realisticky/Mocniny/07_Mocniny_s_promennou_v_mocniteli.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/07%20Mocniny%20s%20prom%C4%9Bnnou%20v%20mocniteli.pdf) |
| 08 Exponenciální tvar čísla | [PDF](../../externi_zdroje/realisticky/Mocniny/08_Exponencialni_tvar_cisla.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/08%20Exponenci%C3%A1ln%C3%AD%20tvar%20%C4%8D%C3%ADsla.pdf) |
| 09 Výpočty s mocninami | [PDF](../../externi_zdroje/realisticky/Mocniny/09_Vypocty_s_mocninami.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/09%20V%C3%BDpo%C4%8Dty%20s%20mocninami.pdf) |
| 10 Mocniny - shrnutí | [PDF](../../externi_zdroje/realisticky/Mocniny/10_Mocniny_-_shrnuti.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/06%20Mocniny/10%20Mocniny%20-%20shrnut%C3%AD.pdf) |
| 01 Výrazy, definiční obor | [PDF](../../externi_zdroje/realisticky/Algebraicke_vyrazy/01_Vyrazy_definicni_obor.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/07%20V%C3%BDrazy/01%20V%C3%BDrazy,%20defini%C4%8Dn%C3%AD%20obor.pdf) |
| 01 Sčítání a odčítání mnohočlenů | [PDF](../../externi_zdroje/realisticky/Mnohocleny/01_Scitani_a_odcitani_mnohoclenu.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/01%20S%C4%8D%C3%ADt%C3%A1n%C3%AD%20a%20od%C4%8D%C3%ADt%C3%A1n%C3%AD%20mnoho%C4%8Dlen%C5%AF.pdf) |
| 02 Násobení mnohočlenů | [PDF](../../externi_zdroje/realisticky/Mnohocleny/02_Nasobeni_mnohoclenu.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/02%20N%C3%A1soben%C3%AD%20mnoho%C4%8Dlen%C5%AF.pdf) |
| 04 Použití vzorců při úpravě mnohočlenů II | [PDF](../../externi_zdroje/realisticky/Mnohocleny/04_Pouziti_vzorcu_pri_uprave_mnohoclenu_II.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/04%20Pou%C5%BEit%C3%AD%20vzorc%C5%AF%20p%C5%99i%20%C3%BAprav%C4%9B%20mnoho%C4%8Dlen%C5%AF%20II.pdf) |
| 05 Dělení mnohočlenů | [PDF](../../externi_zdroje/realisticky/Mnohocleny/05_Deleni_mnohoclenu.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/05%20D%C4%9Blen%C3%AD%20mnoho%C4%8Dlen%C5%AF.pdf) |
| 06 Rozklad mnohočlenů na součin I (vytýkání) | [PDF](../../externi_zdroje/realisticky/Mnohocleny/06_Rozklad_mnohoclenu_na_soucin_I_vytykani_.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/06%20Rozklad%20mnoho%C4%8Dlen%C5%AF%20na%20sou%C4%8Din%20I%20(vyt%C3%BDk%C3%A1n%C3%AD).pdf) |
| 07 Rozklad mnohočlenů na součin II (vzorce) | [PDF](../../externi_zdroje/realisticky/Mnohocleny/07_Rozklad_mnohoclenu_na_soucin_II_vzorce_.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/07%20Rozklad%20mnoho%C4%8Dlen%C5%AF%20na%20sou%C4%8Din%20II%20(vzorce).pdf) |
| 08 Rozklad mnohočlenů na součin III | [PDF](../../externi_zdroje/realisticky/Mnohocleny/08_Rozklad_mnohoclenu_na_soucin_III.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/08%20Mnoho%C4%8Dleny/08%20Rozklad%20mnoho%C4%8Dlen%C5%AF%20na%20sou%C4%8Din%20III.pdf) |
| 01 Krácení a rozšiřování lomených výrazů | [PDF](../../externi_zdroje/realisticky/Lomene_vyrazy/01_Kraceni_a_rozsirovani_lomenych_vyrazu.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/09%20Lomen%C3%A9%20v%C3%BDrazy/01%20Kr%C3%A1cen%C3%AD%20a%20roz%C5%A1i%C5%99ov%C3%A1n%C3%AD%20lomen%C3%BDch%20v%C3%BDraz%C5%AF.pdf) |
| 03 Sčítání a odčítání lomených výrazů II | [PDF](../../externi_zdroje/realisticky/Lomene_vyrazy/03_Scitani_a_odcitani_lomenych_vyrazu_II.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/09%20Lomen%C3%A9%20v%C3%BDrazy/03%20S%C4%8D%C3%ADt%C3%A1n%C3%AD%20a%20od%C4%8D%C3%ADt%C3%A1n%C3%AD%20lomen%C3%BDch%20v%C3%BDraz%C5%AF%20II.pdf) |
| 04 Násobení a dělení lomených výrazů | [PDF](../../externi_zdroje/realisticky/Lomene_vyrazy/04_Nasobeni_a_deleni_lomenych_vyrazu.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/09%20Lomen%C3%A9%20v%C3%BDrazy/04%20N%C3%A1soben%C3%AD%20a%20d%C4%9Blen%C3%AD%20lomen%C3%BDch%20v%C3%BDraz%C5%AF.pdf) |
| 05 Zjednodušování lomených výrazů I | [PDF](../../externi_zdroje/realisticky/Lomene_vyrazy/05_Zjednodusovani_lomenych_vyrazu_I.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/01%20Z%C3%A1kladn%C3%AD%20poznatky/09%20Lomen%C3%A9%20v%C3%BDrazy/05%20Zjednodu%C5%A1ov%C3%A1n%C3%AD%20lomen%C3%BDch%20v%C3%BDraz%C5%AF%20I.pdf) |
| 2.7.15 Mocniny s racionálním mocnitelem | [PDF](../../externi_zdroje/realisticky/Mocniny/15_MocninySRacionalnimMocnitelem.pdf) | [Realisticky.cz](http://www.realisticky.cz/ucebnice/01%20Matematika%20S%C5%A0/02%20Funkce%20a%20rovnice/07%20Mocnin%C3%A9%20funkce%20a%20odmocniny/15%20Mocniny%20s%20racion%C3%A1ln%C3%ADm%20mocnitelem.pdf) |

## Důležité metodické poznámky

- V nových přípravách jsou správně vymezeny racionální mocniny kladných základů, podmínky původního dělitele a nenulovost všech částí složeného zlomku. Nepřesnosti původní učebnice nejsou přebírány a učebnice sama nebyla upravena.
- Při usměrňování `1/(1+sqrt(x))` je případ `x=1` zachován zvlášť; násobení nulovým sdruženým výrazem by nebylo přípustné.
- Přesný výraz `3x^6-2x^3-3x^4+2` ze sešitu byl nezávisle rozložen na `(x-1)^2(3x^4+6x^3+6x^2+4x+2)`. Není tvrzena nerozložitelnost posledního činitele.
- Hodina 51 je obsahově náročná. Příprava rozlišuje základní práci od domácího procvičení a náročné rezervy; všechny položky nejsou zamýšleny jako povinné řešení během 45 minut.
- Kontrolní dosazování v hodině 58 je odlišeno od obecného důkazu identity. Jeden souhlasný příklad obecnou správnost nedokazuje.
- Metodické přípravy testových hodin jsou dokončené. Konkrétní žákovské testy, varianty, bodování a schvalování výběru se nadále řeší samostatně podle skillu `vytvor-test`. Žádný takový nový test nebyl vytvořen.
- Časová přiměřenost a gradace byly didakticky posouzeny podle rozpisu a podkladů; skutečné tempo konkrétní třídy nebylo prakticky změřeno.
