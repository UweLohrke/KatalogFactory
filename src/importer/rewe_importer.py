"""
KatalogFactory by U.L.

Datei:
rewe_importer.py

Version:
0.9.2

Beschreibung:
Importiert REWE-Exceldateien.
Unterstützt sowohl den Standardordner
als auch eine explizit ausgewählte Datei.
"""

import sys
from pathlib import Path

import pandas as pd


class ReweImporter:

    def __init__(self):

        if getattr(sys, "frozen", False):
            self.project_path = Path(sys._MEIPASS)
        else:
            self.project_path = Path(__file__).resolve().parents[2]

        self.excel_folder = self.project_path / "excel"

    # --------------------------------------------------
    # Excel-Datei suchen
    # --------------------------------------------------

    def find_excel_file(self):

        files = list(
            self.excel_folder.glob("*.xlsx")
        )

        if not files:

            raise FileNotFoundError(
                f"Keine Excel-Datei im Ordner '{self.excel_folder}' gefunden."
            )

        return files[0]

    # --------------------------------------------------
    # Excel laden
    # --------------------------------------------------

    def load_excel(
        self,
        excel_file=None,
    ):

        if excel_file is None:

            excel_file = self.find_excel_file()

        dataframe = pd.read_excel(
            excel_file,
        )

        return Path(excel_file), dataframe

    # --------------------------------------------------
    # Regionen
    # --------------------------------------------------

    def get_regions(
        self,
        excel_file=None,
    ):

        _, dataframe = self.load_excel(
            excel_file,
        )

        return [

            column

            for column in dataframe.columns

            if isinstance(column, str)

            and column.startswith(
                "REWE"
            )

        ]

    # --------------------------------------------------
    # Artikel
    # --------------------------------------------------

    def get_articles_for_region(
        self,
        region,
        excel_file=None,
    ):

        _, dataframe = self.load_excel(
            excel_file,
        )

        if region not in dataframe.columns:

            raise ValueError(
                f"Region '{region}' nicht gefunden."
            )

        dataframe = dataframe[
            dataframe["Status"] != "#NV"
        ]

        artikel = dataframe[
            dataframe[region] == "X"
        ]

        return artikel