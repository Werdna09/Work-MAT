# Funkce v 1. ročníku SPŠ – nezávislý rozbor a návrh výuky

**Datum revize:** 31. 10. 2026  
**Repozitář:** https://github.com/Werdna09/Work-MAT  
**Status:** analytický návrh k rozhodnutí učitele; žádné změny GitHubu, příprav ani rozpisu.

## 1. Zdroje a jejich závaznost

1. **Původní tematický plán** „Tématický plán1.pdf“ (SPŠ a Gymnázium Na Třebešíně; 1. ročník, strojírenství, platnost od 1. 9. 2020), dostupný mezi podklady uživatele. Uvádí 4 hodiny týdně, 136 hodin ročně. Únorových **12 hodin se vztahuje společně na 4.1–4.6**, tedy nejen funkce, nýbrž i lineární rovnice; konkrétní počet hodin *pouze* na funkce z něj nelze vyčíst. Kvadratické funkce spadají pod 5.1 v dubnovém tematickém celku.
2. **Aktuální ročníkový rozpis** [`1_rocnik/tematicke_plany/Rozpis_vyuky_MAT_1_rocnik.tex`](https://github.com/Werdna09/Work-MAT/blob/main/1_rocnik/tematicke_plany/Rozpis_vyuky_MAT_1_rocnik.tex). Vyčleňuje hodiny **59–72**, z nichž 69 je písemná práce; tj. **13 výukových hodin + 1 písemná práce**. Hodiny 103–109 se věnují kvadratické funkci. Tento podrobný rozpis představuje projektové rozhodnutí, nikoliv doslovnou hodinovou dotaci jednotlivých podbodů původního plánu.
3. **Autorova učebnice:** [`Funkce.tex`](https://github.com/Werdna09/Work-MAT/blob/main/ucebnice/02_Funkce_a_rovnice/Zaklady_funkci/Funkce.tex); [`Lineární funkce.tex`](https://github.com/Werdna09/Work-MAT/blob/main/ucebnice/02_Funkce_a_rovnice/Linearni_funkce_a_rovnice/Line%C3%A1rn%C3%AD%20funkce.tex); [`Lineární funkce s abs.tex`](https://github.com/Werdna09/Work-MAT/blob/main/ucebnice/02_Funkce_a_rovnice/Funkce_s_absolutni_hodnotou/Line%C3%A1rn%C3%AD%20funkce%20s%20abs.tex); [`Kvadratické funkce.tex`](https://github.com/Werdna09/Work-MAT/blob/main/ucebnice/02_Funkce_a_rovnice/Kvadraticke_funkce_a_rovnice/Kvadratick%C3%A9%20funkce.tex).
4. **Realisticky.cz**, kapitoly [`Funkce a rovnice`](https://www.realisticky.cz/dil.php?id=8): 020103 Zobrazení, 020104 Funkce/definiční obor, 020105–020106 Graf funkce, 020108–020111 Lineární funkce, 020113–020114 Rostoucí/klesající funkce, 020115 Slovní úlohy, 020401 Funkce absolutní hodnota, 020406 Sudá/lichá, 020501 Kvadratická funkce. Učebnice Realisticky.cz má jemnější členění: **jedna externí lekce neznamená jednu naši hodinu**. Některé lekce bylo možné posoudit v textovém extraktu; webové snímky příslušných PDF selhávaly, úplná obrazová revize externích PDF proto neproběhla.
5. **Aktuální přípravy 59–72** v [`1_rocnik/pripravy/`](https://github.com/Werdna09/Work-MAT/tree/main/1_rocnik/pripravy/), čteny jako výchozí návrhy k nezávislému posouzení. Úroveň pokrytí byla ověřena na zdrojových `.tex`; neprobíhala kompletní matematická a vizuální recenze každého PDF.

## 2. Co je podstatné a co je nad rámec

### Nezbytné dovednosti pro první blok (59–72)

- Rozhodnout, zda pravidlo či diagram určuje funkci, interpretovat **vstup–výstup** a jednoznačnost.
- Rozlišit **funkci**, její **předpis**, **argument**, **funkční hodnotu**, **definiční obor** a **obor hodnot**; nezaměňovat obor hodnot a cílovou množinu.
- Přejít mezi tabulkou, jednoduchým předpisem, grafem a slovní situací; rozpoznat, které údaje tabulka neurčuje.
- Z grafu odečíst hodnoty, najít argumenty dané hodnoty, průsečíky s osami, intervaly kladných/záporných hodnot, monotonicitu a význačné body; číst otevřené/uzavřené krajní body.
- Používat `y=ax+b`: význam **a** (změna na jednotku argumentu) a **b** (hodnota při x=0); sestrojit graf, vypočítat předpis z dvojice bodů, vyšetřit znaménko a konstantní případ `a=0`.
- Modelovat reálnou situaci pomocí lineární funkce, uvádět jednotky a **smysluplnou doménu** (diskrétní počty kusů, nezáporný čas, omezení kapacity).
- Na jednoduchém obrázku porovnat dvě přímky a vysvětlit průsečík jako okamžik shody dvou hodnot.
- Sestrojit `y=|x|`, jednoduché posuny / násobky a číst sudost či lichost na zvládnutelných příkladech; bez systematických rovnic s absolutní hodnotou.

### Není nutné soustavně zařazovat do tohoto bloku

Kartézský součin a binární relace jako samostatnou formalistickou lekci; úplnou teorii injektivity/bijekce, složené a inverzní funkce, periodicitu, konvexitu/konkávnost, komplexní důkazy omezenosti, extrémy obecné funkce, rekurentní posloupnosti a parametrické systémy přímek. Autorova učebnice tato témata obsahuje, **ale šíře učebnice není závazný rozsah jedné kapitoly v prvním ročníku**. Mnohé se vrátí u dalších funkcí a ve vyšších ročnících.

## 3. Nezávislý audit existujícího bloku

| Soubor / hodina | Hodnocení a konkrétní zásah |
|---|---|
| **59 Úvod do funkcí** | Má asi 330 řádků zdroje, 3 definiční boxy, 10 řešených příkladů a čtyři procvičovací boxy; materiál je přiznaně částečně rezervní, přesto příliš široký pro snadné použití. Redukovat **povinné jádro** na jednoznačné přiřazení, jeden diagram, značení a základní dosazení. Rekurenci, velkou teorii množin a kružnici ponechat jako samostatné učitelské rezervy nebo přesunout. Úvodní komentář odkazuje na údajný `Podklady_pro_tvorbu_priprav_Funkce.md`, který při ověřování v repozitáři na uvedeném místě nebyl nalezen. |
| **60 Definiční obor a obor hodnot** | Dobré jádro. U každého příkladu důsledně oddělovat D(f), H(f), cílovou množinu a případná omezení slovního zadání. Výraz a funkce se shodným předpisem a jiným oborem nejsou tatáž funkce. |
| **61 Graf a průsečíky** | Dobrá návaznost, ale přidává i čtení intervalů růstu/poklesu. Ponechat orientaci v grafu a průsečíky; početné grafové úkoly rozdělit do 61–62. |
| **62 Monotonie, sudost a lichost** | Dvě metodicky náročné oblasti v 45 minutách; obsahuje šest definičních boxů. **Odlehčit:** zde vyhradit samostatnou hodinu čtení grafů, jejich změn a první intuitivní monotonie. Formální sudost/lichost zařadit do 71 po seznámení s absolutní hodnotou, grafy x² a x³. |
| **63–65 Lineární funkce a graf** | Dobré pořadí, ale riziko opakování kreslení stejné přímky bez nového posunu v dovednostech. Rozdělit: 63 význam lineární závislosti; 64 vliv parametrů a,b a směrnice; 65 graf z různých zadání, předpis ze dvou bodů a omezený obor. |
| **66 Konstantní funkce** | Samostatných 45 minut je potenciálně mnoho na pouhou definici `a=0`. Spojit s vodorovnou/svislou přímkou, omezeným oborem a podrobnou prací s D,H, monotonii v nepřísném smyslu nevyžadovat v jádru. |
| **67–68 Aplikace a porovnávání** | Obsahově správné, zachovat. V 67 preferovat jeden opravdu promyšlený model před řadou mělkých úloh. V 68 srovnávat graficky i početně, avšak teoretické ekvivalentní úpravy rovnic až v 73. |
| **69 Pololetní písemná práce** | Podrobný rozpis ji nyní klade až po prvních deseti hodinách funkcí a zahrnuje základy funkcí; původní školní tematický plán uvádí druhou písemnou po algebraických výrazech, v lednu. To je **skutečný organizační rozpor**, který má být vědomě schválen. Písemka nesmí zahrnovat funkce s absolutní hodnotou (až 70). |
| **70 Funkce s absolutní hodnotou** | Dobré místo po lineárních funkcích. Zachovat základní graf, absolutní hodnotu jako předpis po částech a lehké posuny; složité vnořené absolutní hodnoty až později. |
| **71 Procvičování grafů a vlastností** | Lze změnit na souhrnné grafové vlastnosti a **sudost/lichost**, bez duplicitních dlouhých definic z 62. Zachovat významnou samostatnou práci. |
| **72 Opakování a přechod k rovnici** | Dobrá propojující hodina. Opravit případné nekonzistentní zápisy neomezených intervalů (u nekonečna vždy kulatá závorka a konzistentně `+\infty`). Novou obecnou teorii řešení rovnic odložit do 73. |

## 4. Návrh konkrétního pořadí – hodiny 59–72

**Počítá se s 45 minutami na hodinu.** U všech výkladových hodin počítat přibližně s 5 minutami navázání/diagnostiky, 12–18 minutami odvození a společné práce, 15–20 minutami žákovských úloh a 5 minutami kontroly. Následující specifické rozpisy dávají součet 45 minut; jsou orientační, nikoliv povinnou hlavičkou přípravy.

| Hod. | Doporučený přesný název | Povinný obsah – co a jak | 45min jádro (min) | Zdroje |
|---|---|---|---|---|
| **59** | **Co je funkce?** | Motivace ze závislosti obsahu čtverce nebo ceny na počtu kusů → vstup/výstup; jednoznačnost šipkami a protikladem; f(x) a x; dosazení a opačná otázka. Jeden formalizační box. | 5 motivace + 10 diagramy + 10 definice/zápis + 15 úlohy + 5 kontrola | Učebnice *Funkce* / „Co je funkce“; Realisticky 020103–020104 |
| **60** | **Definiční obor a obor hodnot** | U výrazu: co má smysl; u modelu: co je dovoleno; D a H z tabulky i jednoduchého grafu; otevřené a uzavřené krajní body; cílová množina odlišná od H. | 5 + 12 + 10 + 13 + 5 | Učebnice / D,H; Realisticky 020104–020105 |
| **61** | **Graf funkce – čtení a průsečíky** | Souřadnice (x;f(x)); čtení f(a), hledání x při f(x)=c; svislicový test; průsečíky a nulové body; žák pracuje s vytištěným grafem, ne pouze projekcí. | 5 + 12 + 10 + 13 + 5 | Učebnice / Grafy; Realisticky 020105 |
| **62** | **Graf funkce – vlastnosti z obrázku** | Samostatná práce s 2–3 záměrně odlišnými grafy: D,H, znaménko, maximální/minimální hodnoty na zobrazeném oboru, růst/pokles/konstantní úseky. První grafický a slovní význam monotonie; bez sudosti/lichosti. | 5 + 8 + 20 + 7 + 5 | Realisticky 020106, 020113; učebnice / vlastnosti |
| **63** | **Lineární funkce a její předpis** | Z rovnoměrného přírůstku odvodit y=ax+b; co znamená být lineární; tabulka a první přímka; kontrast vůči nelineární závislosti. | 5 + 10 + 15 + 10 + 5 | Učebnice *Lineární funkce*; Realisticky 020108–020109 |
| **64** | **Směrnice a průsečík s osou y** | Vliv a a b na přímku; ze dvou bodů odvodit změnu y na jednotku x: (y₂−y₁)/(x₂−x₁), x₁≠x₂; znaménko a a růst/pokles; posuny při stejném a. | 5 + 15 + 10 + 10 + 5 | Učebnice / parametry; Realisticky 020110, 020113 |
| **65** | **Sestrojení grafu a určení předpisu** | Konstrukce tabulkou a pomocí a,b; volba dvou vhodných bodů; získání předpisu ze dvou bodů nebo z grafu; úsek přímky při omezeném D. Povinně alespoň dva samostatné obrázky na mřížce. | 5 + 10 + 20 + 5 + 5 | Učebnice / graf, předpis z bodů; Realisticky 020109–020111 |
| **66** | **Konstantní funkce a omezený definiční obor** | a=0, f(x)=b, vodorovný graf a H={b}; proč svislá přímka není grafem funkce y(x); porovnání přímky, polopřímky a úsečky při různém D; otevřené/uzavřené krajní body. | 5 + 10 + 15 + 10 + 5 | Učebnice *Lineární funkce*; Realisticky 020109–020111 |
| **67** | **Lineární funkce v praxi** | Jeden poctivý model: pevná sazba + cena za jednotku nebo nádrž s přítokem/odtokem; určit proměnnou, jednotky, koeficienty, doménu, graf a odpověď v kontextu. Rezerva druhý model. | 5 + 10 + 20 + 5 + 5 | Učebnice / technické a ekonomické úlohy; Realisticky 020108, 020115 |
| **68** | **Porovnávání lineárních funkcí** | Dvě přímky v jedné soustavě; význam průsečíku, rovnoběžnost a splývání; jednoduché grafické i početní porovnání; aplikačně dvě cenové nabídky. | 5 + 10 + 20 + 5 + 5 | Učebnice / porovnávání přímek; Realisticky 020112, 020115 |
| **69** | **Pololetní písemná práce** | Samostatný učitelský test. Pokud zůstává v tomto termínu: **algebra + základy funkcí po 68**, nikoliv absolutní hodnota nebo rovnice. Přesná náplň a trvání podle schváleného testu. | Až 45 min podle testu | Ročníkový rozpis; dořešit rozpor s původním školním TP |
| **70** | **Funkce s absolutní hodnotou** | Graf y=|x| jako dvě větve, předpis po částech, vrchol a H; jednoduché y=|x−p|+q a y=a|x|. Každou změnu ověřit na kontrolních bodech. | 5 + 15 + 15 + 5 + 5 | Učebnice *Lineární funkce s abs*; Realisticky 020401 |
| **71** | **Vlastnosti funkcí – monotónnost a souměrnost** | Porovnat grafy lineární, konstantní, |x|, x² a x³; intervaly růstu/poklesu, extrémy na jednoduchých grafech; sudost f(−x)=f(x) a lichost f(−x)=−f(x) včetně podmínky souměrného D. | 5 + 15 + 15 + 5 + 5 | Učebnice / vlastnosti; Realisticky 020406, 020113 |
| **72** | **Souhrn funkcí a grafická interpretace rovnice** | Integrované čtení a sestrojení grafu; f(x)=c a f(x)=g(x) jako průsečíky; úlohy s omezeným D; jen intuitivní přechod k rovnici, formalizace ekvivalentních úprav až 73. | 5 + 10 + 15 + 10 + 5 | Učebnice *Funkce*, *Lineární funkce*; Realisticky 020112 / 020209 |

### Logika návaznosti

`jednoznačné přiřazení → předpis a obory → graf a jeho čtení → rovnoměrná změna → lineární funkce → směrnice/graf → modelování → dvě přímky → absolutní hodnota → souměrnost a vlastnosti → grafická rovnice`.

Zatímco současná 62. hodina kombinuje růst, pokles, sudost a lichost, nová 62. hodina slouží k důkladnějšímu čtení grafů. Sudost a lichost se přirozeně ukáže v 71. hodině na více typech grafů.

## 5. Mini-diagnostika a podmínka posunu dál

Před 63. hodinou by většina třídy měla bez pomoci zvládnout:

1. poznat nefunkční diagram nebo graf (dva výstupy pro stejný vstup);
2. vypočítat f(−2), odečíst f(−2) z grafu a rozpoznat rozdíl;
3. určit D,H a vysvětlit krajní body na zadaném úseku;
4. najít, kde je graf nad osou x a kde protíná osu x;
5. rozlišit růst funkčních hodnot od kladnosti těchto hodnot.

Před písemnou 69:

1. z f(x)=ax+b sestrojit graf a vysvětlit oba koeficienty;
2. určit a,b z vhodného grafu či dvou bodů;
3. číst D,H i z omezeného úseku;
4. vytvořit a vyložit jednoduchý lineární model včetně jednotek;
5. porovnat dvě přímky a interpretovat jejich průsečík.

Diagnostika má sloužit k opravě konkrétních nedostatků; **nepřidávat automaticky další test** nad již plánované písemné práce.

## 6. Matematické a metodické zásady

- **Funkce je předpis/přiřazení spolu s doménou:** stejný algebraický výraz na různých D nemusí určovat tutéž funkci.
- **Nezaměňovat cílovou množinu a obor hodnot** – důležité zejména u diagramů.
- **Výjimky z domény:** graf kreslený jen v okně není automaticky omezenou funkcí; v modelu se naproti tomu D často skutečně omezuje.
- **Grafové vlastnosti:** `f(x)>0` neznamená „roste“; znaménko f a monotonicita jsou jiné otázky.
- **Konstantní funkce:** vodorovná přímka; přísně neroste ani neklesá. Nepřísnou monotonii lze nabídnout až po vysvětlení příslušných definic.
- **Sudost a lichost:** zkoumat nejen f(−x), ale také symetrii D vůči nule.
- **Bod vs. dvojice:** psát konzistentně `(x;y)` pro souřadnice a `\langle a;b\rangle` pro uzavřený interval v české konvenci projektu. Např. `H=\langle2;+\infty)`.
- **Průsečíky a rovnice:** rovnost hodnot dvou funkcí je motivací, nikoliv náhradou následného výkladu ekvivalentních úprav rovnic.
- **Žákovská aktivita:** při čtení grafů tisknout graf zvlášť, při konstrukci používat mřížku; prezentace samotná nestačí.
- **Matematika technického modelu:** vždy uvádět jednotky a doménu (např. cena kusů na `\mathbb N_0`, spojitý čas na intervalu, nádrž do plné kapacity).

## 7. Budoucí kvadratické funkce – závazná návaznost, nikoliv součást tohoto bloku

Ve školním plánu jde o **samostatný celek 5.1**, v interním ročníkovém rozpisu především **hodiny 103–109** (sedm výukových hodin), následně 110 souhrnná práce a 111–128 kvadratické rovnice a nerovnice; 129 a 132 se ke kvadratické funkci vracejí aplikačně/opakováním. Autorova učebnice `Kvadratické funkce.tex` je rozsáhlá, včetně vrcholového tvaru, doplnění na čtverec, průsečíků, parametrů i optimalizace. To **neopravňuje** zavádět celou kapitolu už v 59–72.

Doporučená návaznost později: 103 základní parabola a její vlastnosti → 104 vliv a → 105 posuny a vrcholový tvar → 106 doplnění na čtverec → 107 průsečíky a nulové body → 108 konstrukce grafu z obecného tvaru → 109 samostatné porovnávání grafů; do 129 ponechat kontextové optimum. Zdroje Realisticky 020501–020506 (zpočátku 020501–020503).

## 8. Rozhodnutí před zahájením oprav a pořadí práce

1. **Potvrdit rozpis 59–72** jako naše pracovní číslování. Původní školní plán neurčuje zvlášť 13 hodin funkcí; nelze tvrdit, že jde o jeho doslovnou dotaci.
2. **Vědomě rozhodnout o písemce 69:** ponechat smíšený obsah (algebra + základy funkcí), nebo ji přesunout bez narušení součtu 136 hodin. Zde je jako výchozí zachovaná, protože už je v aktuálním ročníkovém rozpisu.
3. **Přepracovat 59, 61–62, 65–66 a 71** jako priority; **60, 63–64, 67–68, 70 a 72** spíš cíleně zrevidovat, ne celé zahodit.
4. **Připravit dva různé tisknutelné listy grafů** k 61–62 a prázdnou mřížku k 65; grafy v učitelské přípravě nenahrazují žákův pracovní prostor.
5. **Provést nezávislou matematickou kontrolu každé nové přípravy a PDF** a aktualizovat ročníkový rozpis až po schválení změn. Nepoužívat `\boxed{}` a nepřidávat pseudo-definice, redundantní R1/D1 označení ani další látku jen podle sousední kapitoly na Realisticky.cz.
6. **Termín první souhrnné písemky P1 je v ročníkovém rozpisu nadále neurčen:** až se zařadí, musí se její hodina vědomě umístit do 136h rozpočtu, nikoli tiše přidat.

---

**Omezení nezávislého rozboru:** Původní školní tematický plán byl čten z dříve dostupného PDF v uživatelských podkladech (platnost 2020), současný detailní ročníkový rozpis a učebnice přímo z aktuálního veřejného repozitáře. Neprohlašujeme plnou shodu těchto verzí plánů ani úplnou vizuální kontrolu všech lekcí Realisticky.cz: textová verze vybraných lekcí byla dostupná, zatímco obrazové zobrazení několika externích PDF se nezdařilo. Časové rozvržení je odborný návrh, ne záznam reálného měření délky úloh ve třídě.
