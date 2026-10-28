# Tvorba příprav na hodiny matematiky

**Pracovní standard pro `~/Work/MAT` · verze 1.2 (28. 10. 2026)**

Tento dokument popisuje, jak vytvářet a dlouhodobě udržovat **učitelské přípravy** pro 1.–4. ročník. Slouží učiteli, Codexu i Claude Code. Společná pravidla kvality, časové náročnosti a spolupráce určuje [AGENTS.md](../../AGENTS.md); zde jsou technické postupy a ukázky. V případě rozporu upozorni na konflikt a nevymýšlej si řešení.

## 1. Kam jednotlivé soubory patří

Umístění odpovídá **skutečné struktuře** repozitáře `~/Work/MAT`:

```text
~/Work/MAT/
├── AGENTS.md                    # společná projektová pravidla
├── 1_rocnik/
│   ├── pripravy/
│   │   ├── 01_ÚVD_ÚvodníHodina.tex
│   │   ├── 02_VRL_CoJeVyrok.tex
│   │   └── 03_VRL_PravdivostSlozenychVyroku.tex
│   ├── testy/
│   ├── pracovni_listy/
│   └── tematicke_plany/
├── 2_rocnik/pripravy/
├── 3_rocnik/pripravy/
├── 4_rocnik/pripravy/
└── sablony/
    ├── pripravy/
    │   ├── priprava.sty
    │   ├── TEMPLATE_Priprava.tex
    │   └── TUTORIAL_pripravy.md
    ├── testy/
    └── pracovni_listy/
```

Styl, vzor i tutorial patří do `sablony/pripravy/`. Každá vlastní příprava patří do `<ročník>_rocnik/pripravy/`.

`priprava.sty` je **jeden společný zdroj vzhledu**. Nekopíruj jej do každé hodiny. V každém ročníkovém `.tex` použij relativní cestu `../../sablony/pripravy/priprava.sty`.

Kořenový `AGENTS.md` na tento tutorial odkazuje. Při běžné tvorbě hodiny upravuj pouze zadaný materiál a potřebnou evidenci; společná pravidla a šablony mají vlastní rozsah změn podle zadání učitele.

## 2. Pojmenování příprav

Formát názvu souboru:

```text
[číslo_hodiny]_[TŘÍPÍSMENNÁ_ZKRATKA]_[PopisnýNázev].tex
```

Příklady:

```text
01_ÚVD_ÚvodníHodina.tex
02_VRL_CoJeVyrok.tex
21_ALG_PravidlaProNásobeníADělení.tex
41_ALG_DěleníPolynomů.tex
```

- **Číslo je pořadí vyučovací hodiny v daném ročníku**, nikoliv pořadí lekce na Realisticky.cz; pro hodiny 1–9 používej úvodní nulu (`01`–`09`), od 100 trojciferné číslo.
- **Zkratka má tři písmena** a označuje širší téma. Používej již zavedené zkratky (např. `ÚVD`, `VRL`, `ALG`); nové vytvářej konzistentně, bez svévolného přejmenování existujících souborů.
- Popisný název píš bez mezer, ve stylu `CoJeVyrok`. Názvy nepřejmenovávej bez požadavku uživatele. Diakritika je možná, pokud ji už projekt používá.
- Nezakládej další hodinu jen proto, že na Realisticky.cz existuje samostatná lekce. Rozhoduje naše skutečná osnova a počet hodin.

## 3. Povinná sazba a vizuální pravidla

**Dokument má být pro učitele, nikoliv automaticky pracovním listem k rozdání žákům.** Používej střídmý černobílý LaTeX (A4, 11pt, Latin Modern).

V horním **záhlaví** každé stránky:

- vlevo: `1. ročník | Výroková logika`,
- vpravo: `02: Co je výrok?`.

Neuváděj úvodní tabulkovou hlavičku. **Nepřidávej povinně** sekce *Cíle hodiny*, *Průběh hodiny* nebo minutový harmonogram. **Nevkládej zápatí** ani závěrečný formální seznam zdrojů do PDF. Nadpisy v textu používej jen tam, kde pomohou orientaci.

### Typy obsahu

| Prvek | Použití | LaTeX |
|---|---|---|
| Definice | Jeden vymezený matematický pojem | `definiceBox` |
| Příklad s řešením | Zadání a bezprostředně navazující řešení v jednom rámečku | `prikladReseniBox` a `\tcblower` |
| Zadání s řešením | Samostatná úloha a navazující řešení v jednom rámečku | `zadaniReseniBox` a `\tcblower` |
| Samotný příklad | Ukázka nebo úloha bez uvedeného řešení | `prikladBox` |
| Samotné zadání | Úloha bez uvedeného řešení | `zadaniBox` |
| Poznámka pro učitele | Co říci, zdůraznit, přeskočit, na co dát pozor | `\poznamka{...}` |
| Očekávané řešení | Spodní část spojeného boxu, šedé písmo a jemně šedý podklad | `\tcblower` uvnitř `prikladReseniBox` / `zadaniReseniBox` |
| Oddíl | Volitelný mezititulek | `\blok{...}` |

**Zásada: jedna definice = jeden `definiceBox`.** Například *atomický výrok* a *složený výrok* nesmí být ve stejném boxu. Definice piš přesně a zvlášť, bez směšování s řešeným příkladem. Definice by měla být typicky jedna až tři věty; hned po ní může následovat příklad.

Výklad zůstává černý. Učitelské poznámky jsou **šedé, mimo rámeček**. Řešení patří **do spodní části téhož rámečku jako příklad nebo zadání**, aby horní a dolní část tvořily jeden vizuální celek. Spodní část má velmi světlé šedé pozadí, jemnou oddělovací čáru a šedý text. Nepoužívej dva nezávislé boxy pod sebou, pokud mezi nimi má být přímá návaznost.

Používej `prikladReseniBox` nebo `zadaniReseniBox` a uvnitř **přesně jedno** `\tcblower`: před ním je zadání, za ním řešení. Do řešení můžeš psát běžný text i vícerádkový matematický zápis (`align*`, `aligned`, `gather*`, zlomky, soustavy apod.). Starší příkaz `\reseni{...}` zůstává z technických důvodů funkční, **pro nové přípravy ho ale nepoužívej**. Pro úlohy bez řešení ponech samostatný `prikladBox` nebo `zadaniBox`.

## 4. Kostra `.tex`

Po zkopírování `sablony/pripravy/TEMPLATE_Priprava.tex` do správné ročníkové složky uprav metadata a napiš skutečný obsah. Nejmenší platná kostra:

```latex
\documentclass[11pt,a4paper]{article}
\input{../../sablony/pripravy/priprava.sty}
\nastavPripravu{1. ročník}{Výroková logika}{02}{Co je výrok?}

\begin{document}

\blok{Motivace}
Krátký vstup do tématu.

\begin{definiceBox}
\textbf{Výrok} je sdělení, u něhož má smysl určit pravdivostní hodnotu.
\end{definiceBox}

\begin{prikladReseniBox}
Urči, zda je tvrzení $2+3=5$ pravdivé.
\tcblower
Ano, jde o pravdivý výrok.
\end{prikladReseniBox}
\poznamka{Na začátku nech žáky vysvětlit jejich postup.}

\end{document}
```

Není nutné používat všechny typy boxů v každé hodině. Jednotlivé definice zůstávají oddělené. Zadání a jeho řešení jsou v jednom rámu, pouze oddělená jemnou linkou.

Pro výpočty zapisuj řešení například takto:

```latex
\begin{zadaniReseniBox}
Uprav výraz $3(x-2)+2x$.
\tcblower
\begin{align*}
3(x-2)+2x &= 3x-6+2x \\
          &= 5x-6.
\end{align*}
\end{zadaniReseniBox}
```

Po `\tcblower` nezačínej další `tcolorbox` a nepřidávej druhé samostatné řešení pod rámeček.

## 5. Jak vytvořit novou hodinu (při zadané tvorbě)

1. **Zjisti skutečný stav repozitáře** (`AGENTS.md`, ročníková složka, podobné přípravy a šablona). Nic nepřepisuj naslepo.
2. **Urči číslo, téma a rozsah** podle našeho schváleného rozpisu. Ověř návaznost předchozí a následující hodiny; pokud materiály nesouhlasí, upozorni, ale neupravuj jinou hodinu bez zadání.
3. **Přečti tento tutorial a šablonu.** Použij centrální `priprava.sty`, nevkládej lokální kopii jeho definic do každého souboru.
4. **Připrav didaktickou posloupnost:** motivace → jednoznačné definice → krátké vysvětlení → společné příklady → samostatné úlohy → případně shrnutí. Pořadí a rozsah přizpůsob konkrétnímu tématu, netvoř povinné administrativní sekce.
5. **Piš úlohy ve stoupající obtížnosti.** Každé řešení vkládej do přímo navazující spodní části pomocí `\tcblower`; uveď správný výsledek a dostatečně stručné vysvětlení. Nevyzrazuj řešení uvnitř zadání, pokud to není záměrná ukázka.
6. **Používej šedé poznámky smysluplně:** náročná místa, typické chyby, vhodná otázka, volitelné rozšíření, varianty tempa. Nepiš obecné fráze bez informační hodnoty.
7. **Ověř matematiku a češtinu** v každém příkladu, včetně krajních případů, znamének a symboliky. Rozlišuj tvrzení, příklad, poznámku a definici.
8. **Zkompiluj PDF**, zkontroluj log a alespoň vizuálně strany. Oprav zalamování, přetékání i přehnaně dlouhé boxy.
9. **Odevzdej soubory `.tex` a případně `.pdf`** a uveď, co vzniklo. Nevytvářej změny v jiných částech projektu, pokud nejsou součástí zadání.

### Převod původních samostatných příprav

Starší příprava mohla obsahovat celý design v preambuli. Při migraci zachovej obsah `\begin{document}` až `\end{document}`, ale původní definice balíčků, boxů a hlaviček nahraď `\input{../../sablony/pripravy/priprava.sty}` + `\nastavPripravu{...}`. Tím se změny vzhledu budou řídit centrálně.

## 6. Realisticky.cz jako podklad

Realisticky.cz může sloužit pro **didaktickou inspiraci, pořadí výkladu a hledání typů úloh**. Neznamená to ale automaticky, že všechny jejich lekce musí být zařazeny do našeho plánu.

Pro studium lokální knihovny, porovnání skutečných PDF, evidenci zdrojů a omezení aktualizací či šíření platí část [Lokální knihovna Realisticky.cz](../../AGENTS.md#lokální-knihovna-realistickycz). Následující poznámky ukazují použití zdroje v přípravě, nejsou další licencí ani pokynem ke stahování.

- U každé hodiny si poznamenej **skutečně použitý** název a URL lekce, například v komentáři na začátku `.tex` (`% Inspirace: ...`). Kódy ani odkazy nevymýšlej.
- Z webu **nekopíruj celé lekce, velké bloky textu či soubory příkladů** do vlastních materiálů bez odpovídajícího oprávnění. Připrav vlastní formulace a vlastní úlohy inspirované metodou, anebo pracuj s materiálem v mezích skutečně získané licence/oprávnění. Pouhý veřejný přístup není automaticky svolením k přepracování nebo dalšímu šíření.
- Pokud zdroj není dostupný, napiš to a zpracuj originální přípravu podle tématu; **netvrď, že jsi konkrétní lekci ověřil**, pokud se to nestalo.
- Neoznačuj autorská řešení z původního webu za vlastní. Zdroje lze uchovat v komentáři souboru nebo v repozitářové evidenci, aniž by se tiskly do zápatí.

## 7. Kompilace a kontrola

Při tvorbě nebo opravě použij z kořene `~/Work/MAT` přednostně společný postup podle `AGENTS.md`:

```bash
./scripts/build_latex.sh 1_rocnik/pripravy/02_VRL_CoJeVyrok.tex
```

Následující přímý příkaz slouží jako náhradní postup, pokud společný skript chybí; selhání existujícího skriptu nejprve vyšetři:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error \
  1_rocnik/pripravy/02_VRL_CoJeVyrok.tex
```

`-cd` je důležité, protože cesta `../../sablony/pripravy/priprava.sty` vychází z ročníkové složky. Při jiné struktuře adresářů uprav relativní cestu; při úpravě stylu kontroluj kompatibilitu již vytvořených hodin. V režimu recenze pouze pro čtení nekompiluj; prohlédni existující PDF a neověřenou aktuálnost zaznamenej.

Při kompilaci dej pozor na:

- znaky `%`, `&`, `_` a `#` v běžném textu (escape `\%`, `\&`, `\_`, `\#`),
- matematické zápisy v `\(...\)` nebo `$...$`,
- správné párování prostředí `\begin`/`\end`,
- `Overfull \\hbox`, přetékající boxy, osamocené nadpisy,
- nepřiměřenou délku: příprava má být použitelná pro skutečnou vyučovací hodinu.

Samostatné definice a zadání se nerozdělují mezi stránky. Spojené boxy se u delšího řešení **mohou rozdělit mezi stránky**, ale při běžné délce zachovají obě části pohromadě. Při nevhodném zlomu raději přeuspořádej příklady nebo rozděl úlohu do didakticky smysluplných kroků.

## 8. Kontrolní seznam před dokončením

- [ ] Číslo, zkratka a název odpovídají osnově a názvu souboru.
- [ ] Záhlaví vlevo uvádí ročník a globální téma; vpravo číslo a název hodiny.
- [ ] Každá definice je ve vlastním `definiceBox`.
- [ ] Zadání s řešením používají spojený `prikladReseniBox` / `zadaniReseniBox` a `\tcblower`.
- [ ] Vícerádkové matematické zápisy jsou v řešeních správně sázené.
- [ ] Poznámky učitele jsou šedě, řešení tvoří šedou spodní část boxu.
- [ ] Nevznikla automaticky sekce *Cíle hodiny*, *Průběh hodiny* ani zápatí.
- [ ] Obsah je didakticky návazný a vejde se do reálné hodinové dotace.
- [ ] Použité zdroje jsou zaznamenány a užití cizích materiálů je oprávněné.
- [ ] PDF se úspěšně přeloží a vizuálně nemá chyby.

## 9. Ukázkové zadání pro Codex

> Připrav hodinu `03_VRL_PravdivostSlozenychVyroku.tex` pro 1. ročník podle naší schválené osnovy. Nejdřív přečti projektová pravidla a `sablony/pripravy/TUTORIAL_pripravy.md`, styl v `sablony/pripravy/priprava.sty` a předchozí hodinu. Použij společné boxy, každou definici odděl do vlastního boxu, řešení připoj pomocí `\tcblower` do spodní části stejného rámečku a učitelské poznámky piš šedě. Vytvoř přiměřené množství úloh s kontrolou řešení, zkompiluj PDF a vizuálně ověř výsledek. Pokud je k dispozici odpovídající lekce Realisticky.cz, použij ji jako metodickou inspiraci a zdroj zaznamenej; nevymýšlej odkazy a nepřejímej rozsáhlé chráněné pasáže.

---

**Smysl šablony:** dlouhodobě jednotný vzhled a rychlá příprava výuky. **Smysl každé přípravy:** být skutečně použitelná přímo při hodině.
