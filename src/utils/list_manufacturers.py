"""
KatalogFactory by U.L.

Datei:
list_manufacturers.py

Version:
1.0.1

Beschreibung:
Ermittelt alle unterschiedlichen
Hersteller aus der Excel-Datei.
"""

from pathlib import Path

import pandas as pd

from config.app_config import EXCEL_FOLDER


def main():

    excel_dateien = sorted(EXCEL_FOLDER.glob("*.xlsx"))

    if not excel_dateien:
        print("Keine Excel-Datei gefunden.")
        return

    excel_datei = excel_dateien[0]

    print(f"Excel-Datei: {excel_datei}")

    df = pd.read_excel(excel_datei)

    hersteller = (
        df["Zusatztext"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    hersteller = sorted(
        {
            name
            for name in hersteller
            if name
        }
    )

    print()
    print(f"{len(hersteller)} Hersteller gefunden:")
    print()

    for name in hersteller:
        print(name)


if __name__ == "__main__":
    main()