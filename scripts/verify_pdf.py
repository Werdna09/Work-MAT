#!/usr/bin/env python3
"""Kontrola existence a čitelnosti výsledného PDF. Pouze stdlib + PDF nástroje OS."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Ověření výstupního PDF")
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    pdf = args.pdf.resolve()
    if not pdf.is_file() or pdf.stat().st_size < 100:
        print(f"CHYBA: PDF chybí nebo je podezřele malé: {pdf}", file=sys.stderr)
        return 1
    if pdf.open("rb").read(5) != b"%PDF-":
        print("CHYBA: Soubor nemá hlavičku %PDF-.", file=sys.stderr)
        return 1
    if shutil.which("pdfinfo"):
        proc = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
        if proc.returncode != 0:
            print("CHYBA: pdfinfo nedokázalo PDF přečíst:\n" + proc.stderr, file=sys.stderr)
            return 1
        match = re.search(r"^Pages:\s*(\d+)", proc.stdout, re.M)
        if not match or int(match.group(1)) < 1:
            print("CHYBA: Nepodařilo se zjistit platný počet stran.", file=sys.stderr)
            return 1
        print(f"OK: PDF má {match.group(1)} stran; velikost {pdf.stat().st_size} B.")
    else:
        print("UPOZORNENI: pdfinfo není instalováno; kontrola počtu stran se přeskočí.")
    if shutil.which("pdftotext"):
        proc = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True)
        if proc.returncode != 0:
            print("UPOZORNENI: Nepodařilo se ověřit text PDF přes pdftotext.")
        elif len(proc.stdout.strip()) < 15:
            print("UPOZORNENI: PDF neobsahuje mnoho extrahovatelného textu; prohlédni stránky.")
    print("UPOZORNENI: Skript nezaručuje správnou sazbu, bezchybnou diakritiku ani matematickou správnost.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
