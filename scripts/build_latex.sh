#!/usr/bin/env bash
set -Eeuo pipefail

# Pouziti z fish/bashe: bash scripts/build_latex.sh 1_rocnik/pripravy/04_VRL_Kvantifikatory.tex
# Kompiluje pouze jeden soubor z Work/MAT. Pomocne soubory zustanou v /tmp.

if [[ $# -ne 1 || "$1" == "-h" || "$1" == "--help" ]]; then
  echo "Pouziti: bash scripts/build_latex.sh CESTA_K_SOUBORU.tex" >&2
  exit 2
fi

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
if [[ ! -f "$1" && -f "$project_root/$1" ]]; then
  tex_candidate="$project_root/$1"
else
  tex_candidate="$1"
fi
if [[ ! -f "$tex_candidate" ]]; then
  echo "CHYBA: Zdrojovy soubor nebyl nalezen: $1" >&2
  exit 2
fi
tex_path="$(realpath -- "$tex_candidate")"
if [[ "$tex_path" != "$project_root"/* ]]; then
  echo "CHYBA: Soubor musi lezet v projektu $project_root" >&2
  exit 2
fi
if [[ "$tex_path" != *.tex ]]; then
  echo "CHYBA: Ocekavan .tex soubor." >&2
  exit 2
fi
command -v latexmk >/dev/null || { echo "CHYBA: Neni dostupny latexmk." >&2; exit 127; }
command -v pdflatex >/dev/null || { echo "CHYBA: Neni dostupny pdflatex." >&2; exit 127; }

name="$(basename -- "$tex_path" .tex)"
pdf_dest="$(dirname -- "$tex_path")/$name.pdf"
work_dir="$(mktemp -d "${TMPDIR:-/tmp}/mat-latex.XXXXXXXX")"
trap 'rm -rf -- "$work_dir"' EXIT

printf 'Kontrola LaTeXove struktury: %s\n' "$tex_path"
python3 "$project_root/scripts/check_structure.py" "$tex_path"
printf '\nKompilace do docasne slozky (zdroje a ostatni soubory zustanou beze zmen):\n'
if ! latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir="$work_dir" "$tex_path" >"$work_dir/build.stdout" 2>&1; then
  echo 'CHYBA: LaTeX se nepodarilo zkompilovat. Nalezene chyby:' >&2
  grep -En -A3 -B2 '(^!|LaTeX Error|Undefined control sequence|Emergency stop|Fatal error occurred|Runaway argument)' \
    "$work_dir/build.stdout" | tail -n 35 >&2 || true
  echo 'Poslednich 20 radku logu:' >&2
  tail -n 20 "$work_dir/build.stdout" >&2
  exit 1
fi
pdf_tmp="$work_dir/$name.pdf"
if [[ ! -s "$pdf_tmp" ]]; then
  echo "CHYBA: latexmk skoncil, ale PDF v docasne slozce chybi: $pdf_tmp" >&2
  exit 1
fi

# Vystup se overi pred kopirovanim; neuspech neprepise stare PDF.
python3 "$project_root/scripts/verify_pdf.py" "$pdf_tmp"

# Diagnostika radku s presahy (orientacni; varovani nemusi byt zavazna).
if [[ -f "$work_dir/$name.log" ]]; then
  if grep -En '(^|[[:space:]])(Overfull|Underfull) \\hbox|Overfull \\vbox' "$work_dir/$name.log"; then
    echo 'POZOR: V LaTeX logu jsou varovani o sazbe, zkontroluj odpovidajici strany.'
  fi
fi
cp -- "$pdf_tmp" "$pdf_dest"
python3 "$project_root/scripts/verify_pdf.py" "$pdf_dest"
echo "HOTOVO: PDF ulozeno vedle zdroje: $pdf_dest"
echo 'Poznamka: Automaticka kontrola nenahrazuje vizualni kontrolu stran a matematickou revizi.'
