# Kontrola nových příprav 05–11 – 1. ročník SPŠ

Kontrola 27. 10. 2026 podle skillů `vytvor-pripravu` a `over-matematiku`.
Verdikt pro nové přípravy: **bez zjištěné matematické chyby**.
Zkontrolován celý výklad, definice, všechna zadání i řešení včetně rezervy
a domácí práce. Označení P, S, R a D odpovídají názvům boxů v dokumentech.

| Úloha / soubor v `1_rocnik/pripravy/` | Výsledek kontroly | Stav | Nezávislá metoda a poznámka |
|---|---|---|---|
| `05_CIS_PrirozenaACelaCisla.tex`: P1–P3, S1–S2, R1, D1 | Znaménka a pořadí operací souhlasí; P3 = 21, R1a = −8. Nula není přirozená. | Bez zjištěné chyby | Přesné vyčíslení, kontrola dělení násobením, opačná čísla a protipříklady obecných výroků. |
| `06_CIS_RacionalniCislaAZlomky.tex`: P1–P3, S1–S2, R1, D1 | Krácení, rozšiřování i porovnání souhlasí; R1b má právě n = 9. | Bez zjištěné chyby | Python `Fraction`, křížové součiny, převod na stejnou jednotku, kontrola mezí; nulový jmenovatel vyloučen. |
| `07_CIS_RealnaCislaAZaokrouhlovani.tex`: P1–P3, S1, R1, D1 | Obory a pořadí čísel souhlasí; zaokrouhlení respektuje uvedené pravidlo přesné poloviny. | Bez zjištěné chyby | `Decimal` s `ROUND_HALF_UP` a nezávisle přesné vzdálenosti k násobkům daného řádu; meze √2 ověřeny druhými mocninami. Důkaz iracionality 1 + √2 kontrolován sporem. |
| `08_CIS_Intervaly.tex`: P1–P3, S1–S2, R1, D1 | Nerovnosti, závorky, příslušnost bodů i úplné výčty celých čísel souhlasí. | Bez zjištěné chyby | Dosazení obou krajů, bodů uvnitř i vně; přesné výčty celých čísel; porovnání obrázků s nerovnostmi. |
| `09_CIS_AbsolutniHodnota.tex`: P1–P4, S1–S2, R1, D1 | Výpočty a vzdálenosti souhlasí; odlišeny dva body, jediný bod a žádný bod podle požadované vzdálenosti. | Bez zjištěné chyby | Přesná aritmetika a délky úseků na ose; zpětné dosazení doplněno argumentem úplnosti pomocí obou stran středu. Obecná chybná tvrzení vyvrácena konkrétními dvojicemi. |
| `10_CIS_PrubeznyTestARozbor.tex`: P1, S1–S2, R1, D1 | Výpočty, pravdivosti a negace souhlasí; dokument obsahuje pouze organizaci testu a následné procvičování. | Bez zjištěné chyby | Úplné pravdivostní tabulky negací spojek, přesná aritmetika, svědkové a krajní body. Žádné žákovské zadání testu nebylo vytvořeno. |
| `11_CIS_CiselneOboryAVyroky.tex`: P1–P3, S1–S2, R1, D1 | Změny pravdivosti podle oboru, negace i protipříklady souhlasí; x² ≥ x platí na Z, na Q nikoli. | Bez zjištěné chyby | Úplný výčet konečného oboru, kontrola svědků v příslušném oboru; negace kvantifikace ověřena pro všechny vlastnosti tříprvkového oboru. Obecné důkazy prověřeny zvlášť, nikoli odvozeny ze vzorkování. |

Základní známé vlastnosti √2 a π jsou uvedeny jako známá matematická fakta;
iracionalita není vyvozována z konečného výpisu desetinných číslic.
U záporných čísel je výslovně sjednáno zaokrouhlení přesné poloviny od nuly.

Zdroje a návaznost: prostudován rozpis, plán SPŠ, relevantní části vlastní
učebnice a více místních lekcí Realisticky.cz. Přesné cesty a použité části
jsou v komentářích jednotlivých `.tex`. Zkontrolována návaznost na hodiny
04 a 12, zejména konvence přirozených čísel a význam oboru proměnné.
Nové konkrétní úlohy a jejich řešení jsou vlastní tvorba.
Množinové operace, systematické úpravy mocnin a obecné algoritmy řešení
rovnic s absolutní hodnotou nebyly přesunuty do těchto hodin.

Při studiu zdroje nalezena důležitá chyba v
`ucebnice/01_Zakladni_poznatky/Ciselne_obory/Číselné obory.tex`,
oddíl Racionální čísla: v řetězci zápisů čísla 2/3 je také zlomek
−126/−198 = 7/11, který se 2/3 nerovná. Chyba nebyla převzata;
učebnice zůstala podle zadání beze změny.

Časové odhady jsou orientační, nikoli změřené ve třídě. Běžné hodiny
mají základ přibližně 35 minut a zásobu rezervy na 10–15 minut k výběru;
domácí práce je určena přibližně na 15–20 minut (u 05 a 07 asi 15 minut).
Hodina 10 počítá s 18minutovým testem v povoleném rozmezí 15–20 minut,
navazující výukou do 45 minut a domácí prací na 10–15 minut. Její rezerva
nahrazuje část navazujícího procvičení.

Všech sedm dokumentů bylo sestaveno pomocí `scripts/build_latex.sh`.
PDF 05–09 a 11 mají po třech stranách, PDF 10 dvě strany: celkem 20 stran.
Všechny strany byly vykresleny a vizuálně zkontrolovány: záhlaví,
diakritika, matematické značky, řešení, číselné osy a hranice boxů.
Nevhodně roztažený řádek definice v 05 byl upraven a znovu zkontrolován.

`planovani/STAV_PRIPRAV.md` zůstává beze změny: v úvodním tematickém celku
dosud chybějí přípravy 13–24. Vytvoření 05–11 proto celý celek nedokončilo.
Kontrola otisků potvrdila zachování všech 175 předem zaznamenaných souborů
příprav, učebnice, šablon, skillů, plánů, plánování a kořenového `AGENTS.md`.
Nevznikl commit ani push.
