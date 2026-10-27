#!/usr/bin/env python3
"""Základní kontrola struktury LaTeXu, zvláště učitelských příprav. Python stdlib."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def without_comments(source: str) -> str:
    # Neescapované % začíná komentář; pro obvyklé zápisy LaTeXu dostačující.
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in source.splitlines())


def main() -> int:
    parser = argparse.ArgumentParser(description="Kontrola základní struktury souboru .tex")
    parser.add_argument("tex", type=Path)
    args = parser.parse_args()
    path = args.tex.resolve()
    if not path.is_file():
        parser.error(f"Soubor neexistuje: {path}")
    code = without_comments(path.read_text(encoding="utf-8-sig"))
    errors: list[str] = []
    warnings: list[str] = []

    # Dílčí kapitoly přes \input nemusí být samostatně kompilovatelné.
    if r"\documentclass" not in code:
        warnings.append("Chybí \\documentclass; možná jde o dílčí kapitolu, nikoli samostatný dokument.")
        for item in warnings:
            print(f"UPOZORNENI: {item}")
        return 0

    for tag in (r"\begin{document}", r"\end{document}"):
        if tag not in code:
            errors.append(f"Chybí {tag}")

    if re.search(r"(?:^|/)\d+_rocnik/pripravy/", path.as_posix()):
        if not re.fullmatch(r"\d{2}_[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]{3}_[^/]+\.tex", path.name):
            warnings.append("Název přípravy neodpovídá doporučenému NN_TTT_PopisnyNazev.tex")
        if r"\nastavPripravu" not in code:
            errors.append("Příprava nemá \\nastavPripravu")
        if "priprava.sty" not in code:
            errors.append("Příprava neodkazuje na společný priprava.sty")
        if r"\newtcolorbox" in code:
            warnings.append("Lokální definice boxů; ověř, zda se neduplikuje společný styl.")
        for box in ("prikladReseniBox", "zadaniReseniBox"):
            opens = len(re.findall(r"\\begin\{" + box + r"\}", code))
            closes = len(re.findall(r"\\end\{" + box + r"\}", code))
            if opens != closes:
                errors.append(f"Nesouhlasí begin/end prostředí {box}: {opens}/{closes}")
        total_joined = sum(len(re.findall(r"\\begin\{" + b + r"\}", code)) for b in ("prikladReseniBox", "zadaniReseniBox"))
        separators = len(re.findall(r"\\tcblower\b", code))
        if total_joined != separators:
            errors.append(f"Propojené boxy: {total_joined} zahájení, ale {separators} oddělovačů \\tcblower")

    for item in warnings:
        print(f"UPOZORNENI: {item}")
    for item in errors:
        print(f"CHYBA: {item}", file=sys.stderr)
    if errors:
        return 1
    print("OK: Základní struktura LaTeXu odpovídá očekávání.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
