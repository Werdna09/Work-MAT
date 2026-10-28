---
name: over-matematiku
description: "Nezávisle prověř matematickou správnost zadání, řešení, důkazů, grafů a výpočtů v projektu Work/MAT. Použij při kontrole testu, učitelské přípravy, pracovního listu či učebnice nebo při podezření na chybu. Tento skill není určen k tvorbě nového zadání."
---

# Nezávislá matematická kontrola — Work/MAT

Tento skill je **kontrolní postup**, nikoli šablona ani oprávnění měnit soubory. Respektuj kořenový `AGENTS.md`, zejména část **Matematická kontrola**, pravidla pro testy a ochranu existujících souborů. Ověřuj skutečný obsah souboru, nikoli jen předchozí tvrzení, že je správný. Pokud probíhá tvorba přípravy nebo testu, postupuj podle příslušného Skillu; tento postup může doplnit kontrolu, ale nenahrazuje schválení výběru úloh učitelem.

## Rozsah a režim práce

1. **Zjisti, co se kontroluje.** Identifikuj přesnou cestu a rozsah (jedna úloha, celý dokument, jedna varianta, všechny varianty). Při jednoznačném zadání nepožaduj zbytečné upřesnění. Jestliže chybí podstatná část zadání, řekni přesně která; nepředstírej přístup k neexistujícím zdrojům.
2. **Pracuj standardně jen pro čtení.** Nepřepisuj `.tex`, PDF ani zdrojové úlohy a nespouštěj kompilaci, která je mění. Neopravuj čísla nebo předpoklady tiše. Pokud učitel výslovně požaduje opravu souboru, nejprve uveď nalezenou chybu, navrhni minimální opravu a respektuj pravidla schvalování změn testu v `AGENTS.md`; již výslovně schválenou opravu nezdržuj opakovaným dotazem. Bez výslovného požadavku nedělej commit, push ani instalaci závislostí. Pro předání nezávislé recenze použij `planovani/recenze/README.md`; role obou nástrojů určuje `AGENTS.md`.
3. **Čti doslovné zadání a řešení.** U `.tex` ověř příslušné prostředí, případné `\input`, lokální makra a další relevantní části; u testů přečti každou požadovanou variantu a její oddělené řešení. Lze-li zadání oddělit bezpečně od řešení, nejprve je vyřeš naslepo a teprve potom čti autorské řešení. Zahrň i rezervní a domácí úlohy, pokud spadají do zadaného rozsahu. Pokud výsledek závisí na obrázku nebo grafu, prohlédni jej, je-li dostupný. Zjisti, zda byl uveden číselný obor, zaokrouhlování, parametry, pomůcky a požadovaná metoda.

## Kontrola každé úlohy

4. **Ověř smysluplnost zadání.** Zkontroluj definiční obor, podmínky existence, význam symbolů, jednoznačnost instrukcí a skutečnost, zda tvrzení nebo úloha odpovídá již probrané látce (pokud je to předmětem kontroly). Označ úlohu za nejednoznačnou, má-li více legitimních výkladů či odpovědí, které zadání nevylučuje.
5. **Vyřeš úlohu nezávisle.** Neber původní řešení jako důkaz správnosti. Pokud možno zvol **jinou cestu** (například algebraické odvození versus ověření pomocí grafu, rozklad versus substituce, geometrickou argumentaci versus souřadnice). Potom porovnej mezikroky a konečný výsledek.
6. **Zkontroluj úplnost a ekvivalenci.** Hlídej násobení či dělení výrazem, který může být nulový; znaménko při úpravě nerovnic; mocnění a odmocňování; absolutní hodnoty; logaritmy a exponenty; hranice intervalů; trigonometrickou periodicitu; parametry a zvláštní případy. Ověř, že řešení neztrácí platné kořeny a nepřidává neplatné.
7. **Doplň zpětnou kontrolu.** Dosazení kořenů do **původního** zadání, vyzkoušení krajních či degenerovaných případů a číselné ověření mohou odhalit chybu. **Samotné dosazení nalezených kořenů nedokazuje, že jiná řešení neexistují.** Pro úplnost uveď i argument, proč další řešení být nemohou.
8. **Prověř další typy úloh podle potřeby.** U důkazů zkontroluj platnost každého logického kroku a obecnost tvrzení; u geometrie konfiguraci, omezení a jednotky; u funkcí definiční obor a graf; u statistiky význam vzorců (souborový/výběrový rozptyl), váhy, interpretaci a zaokrouhlení. U kombinatoriky rozliš pořadí, opakování a započtení stejných možností.
9. **Testy ověřuj po variantách.** Kontroluj každé zadání a řešení samostatně, rozsah látky, srovnatelnost A/B, C/D atd. a realistickou časovou náročnost. Pokud je dostupný pouze návrh testu, vyjádři závěry o návrhu, nikoli o neexistujícím finálním PDF.

## Nástroje a míra jistoty

10. **Použij dostupné prostředky přiměřeně.** Běžné algebraické úlohy kontroluj vlastními přesnými úpravami. Doplňkově lze využít Python standardní knihovnu (`fractions`, `math`, `itertools`, `decimal`) či již instalované nástroje. Je-li `sympy` dostupné, může pomoci, ale **jeho absence není chyba projektu**. Neinstaluj jej ani jiné balíčky bez povolení; přejdi na ruční nebo vestavěnou alternativu. U logaritmických, trigonometrických a numerických rovnic rozliš přesnou a přibližnou kontrolu.
11. **Nespoléhej na shodu jedné metody se sebou samou.** Stejná algebraická úprava zopakovaná v kódu není nezávislé ověření. Pro kontrolu s velkým počtem případů lze použít úplné vyčíslení, pokud je množina konečná a přiměřeně malá; jinak lze vzorkování použít pouze jako podpůrný test.
12. **Udržuj dohledatelnost.** Zapisuj soubor, variantu, označení úlohy a konkrétní místo chyby (případně řádek v `.tex`). U předávané recenze zaznamenej také verzi, Git stav a otisky kontrolovaných souborů podle `planovani/recenze/README.md`; commit není podmínkou. Nerozšiřuj závěr na nezkontrolované části. Pokud je některý podklad nedostupný, označ přesně, jaký vliv má toto omezení na verdikt. Pravidla pro studium externích PDF stanoví `AGENTS.md`; chybějící knihovnu neaktualizuj.

## Výstup z kontroly

13. Nejprve stručně sděl verdikt a rozsah: **bez zjištěné chyby / chyba / nejednoznačnost / nelze ověřit**. „Bez zjištěné chyby“ znamená jen kontrolu uvedeného rozsahu, nikoli absolutní záruku správnosti.
14. U zjištěných problémů uveď v tomto pořadí: **soubor a úloha → co je špatně → proč → správné řešení nebo minimální návrh opravy → závažnost** podle `planovani/recenze/README.md`. Matematické chyby odděl od stylistických či metodických doporučení.
15. Při rozsáhlejším ověření sestav stručnou tabulku „úloha – výsledek – stav – poznámka“. U každé varianty potvrď, zda byla skutečně zkontrolována. Uveď použitou **nezávislou metodu**, nejen frázi „matematicky ověřeno“.
16. **Žádná tichá změna.** Ve výchozím režimu nevytvářej ani neupravuj materiály. Pokud byl výslovně vyžádán opravený soubor, po provedení opravy spusť relevantní kompilaci a vizuální kontrolu podle `AGENTS.md`, je-li to možné, a vypiš všechny změněné cesty.

## Příklady spuštění

- „Použij `$over-matematiku` a nezávisle zkontroluj všechny příklady a řešení v `1_rocnik/pripravy/04_VRL_Kvantifikatory.tex`. Nic neupravuj.“
- „Použij `$over-matematiku` a ověř obě varianty v `2_rocnik/testy/ExponencialniRovnice/01_test_ExponencialniRovnice_AB.tex` včetně úplnosti kořenů. Uveď případné nesrovnalosti, žádné soubory neměň.“
