---
name: vytvor-pripravu
description: Vytvoř nebo uprav učitelskou přípravu na hodinu matematiky v repozitáři Work/MAT. Použij při zadání konkrétní vyučovací hodiny nebo úpravě existující přípravy; nepoužívej pro testy, pracovní listy ani učebnici.
---

# Vytvoření nebo úprava učitelské přípravy (Work/MAT)

Pracuj v kořeni repozitáře `Work/MAT`. Tento skill popisuje **postup**, nikoli nový vzhled dokumentů. Závazné projektové pokyny jsou v `AGENTS.md`, podrobná pravidla a příklady v `sablony/pripravy/TUTORIAL_pripravy.md`. Nepřepisuj jejich obsah sem a při nesouladu podkladů na rozpor upozorni.

## Postup

1. **Ověř zadání a rozsah.** Urči ročník, číslo hodiny, téma a zda jde o novou přípravu, nebo úpravu existující. Nesahej na nesouvisející hodiny, testy, pracovní listy, osnovy ani společný styl bez výslovného pokynu.
2. **Prostuduj skutečný stav projektu.** Přečti `AGENTS.md`, `sablony/pripravy/TUTORIAL_pripravy.md`, `sablony/pripravy/TEMPLATE_Priprava.tex`, `sablony/pripravy/priprava.sty` a nejbližší související přípravu v `N_rocnik/pripravy/`. Pokud něco chybí, řekni to; nevytvářej domnělé náhrady.
3. **Ověř návaznost.** Respektuj výslovné zadání učitele a schválenou osnovu, pokud je v projektu dostupná; porovnej relevantní `N_rocnik/tematicke_plany/SPS.pdf` či `GYM.pdf`, okolní hodiny a související kapitolu v `ucebnice/`. Nevymýšlej číslování ani nepřizpůsobuj naši osnovu automaticky číslování Realisticky.cz.
4. **Vyber podklady.** Preferuj autorovu učebnici, existující pracovní listy a skutečně dostupné materiály v `externi_zdroje/`. Realisticky.cz používej jako metodickou inspiraci. Nevydávej nepřečtenou lekci za ověřenou a nepřebírej rozsáhlé chráněné pasáže bez odpovídajícího oprávnění. Použité zdroje eviduj v komentářích `.tex` nebo interním přehledu.
5. **Připrav didaktický obsah.** Napiš srozumitelný souvislý výklad, přesné samostatné definice, vhodně odstupňované příklady, úplná řešení a jen užitečné metodické poznámky. Rozsahem respektuj reálnou vyučovací hodinu. Rozlišuj základní látku a volitelné rozšíření.
6. **Použij existující sazbu.** Soubor ukládej přímo do `N_rocnik/pripravy/` jako `[NN]_[TTT]_[PopisnyNazev].tex`, není-li stanoveno jinak. Pro přípravu přímo v této složce použij `\input{../../sablony/pripravy/priprava.sty}` a `\nastavPripravu{...}{...}{...}{...}`. Každou definici vlož samostatně do `definiceBox`. Zadání s řešením zapisuj do `prikladReseniBox` nebo `zadaniReseniBox` s jediným `\tcblower`. Učitelské poznámky piš přes `\poznamka{...}`. Nepřidávej automaticky cíle, harmonogram, úvodní metadatovou hlavičku ani zápatí. Nepiš lokální kopie maker ze stylu.
7. **Zkontroluj obsah.** U každého výpočtu ověř podmínky, ekvivalentnost úprav a výsledek; kde to dává smysl, použij nezávislou kontrolu. Ověř češtinu, značení a návaznost na předchozí hodinu. Chybu ve zdrojovém zadání neřeš tichou svévolnou změnou.
8. **Zkompiluj a ověř výstup.** Pokud v projektu existuje funkční `scripts/build_latex.sh`, používej přednostně tento společný postup z kořene repozitáře:

   ```bash
   ./scripts/build_latex.sh N_rocnik/pripravy/NN_TTT_PopisnyNazev.tex
   ```

   Dosaď skutečnou cestu. Skript provádí základní kontrolu struktury, kompiluje do dočasného adresáře a po úspěchu ověřuje PDF uložené **vedle příslušného `.tex`**. Jestliže skript neexistuje, použij zavedený postup `latexmk -cd -pdf -interaction=nonstopmode -halt-on-error <cesta.tex>` a ověř umístění PDF. Pokud skript existuje, ale selže, chybu vyšetři a neskryj ji tím, že přepneš na jiný postup bez vysvětlení. Zkontroluj log a je-li možné vykreslení PDF, vizuálně prověř všechny stránky. Automatická kontrola PDF nenahrazuje matematickou kontrolu ani kontrolu sazby. Neoznačuj neprovedenou kontrolu za hotovou.
9. **Shrň dokončenou práci.** Uveď cestu k `.tex` a případnému `.pdf`, rozsah změn, výsledek matematické a technické kontroly a případné nedořešené problémy. Nedělej commit ani push bez výslovného pokynu.

## Hranice použití

- Tento skill je určen jen pro **učitelské přípravy**. Pro testy, pracovní listy a kapitoly učebnice používej jejich vlastní projektové pokyny.
- Pokud uživatel žádá pouze návrh nebo revizi, nevytvářej bez důvodu další soubory.
- Pokud ročník, téma či číslo hodiny nelze bezpečně zjistit z podkladů, označ nejistotu; nenahrazuj ji vymyšlenou osnovou.
