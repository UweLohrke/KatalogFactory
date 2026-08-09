"""
KatalogFactory by U.L.

Datei:
app_settings.py

Version:
1.1.0

Beschreibung:
Zentrale Verwaltung aller Programmeinstellungen.

Verwendet beim ersten Start automatisch
die Standardordner aus der zentralen
Konfiguration.
"""

from config.app_config import (
    EXCEL_FOLDER,
    CATALOG_FOLDER,
)

from PySide6.QtCore import QSettings


class AppSettings:

    ORGANIZATION = "UL"
    APPLICATION = "KatalogFactory"

    def __init__(self):

        self.settings = QSettings(
            self.ORGANIZATION,
            self.APPLICATION,
        )

    # --------------------------------------------------
    # Excel-Datei
    # --------------------------------------------------

    def get_last_excel_file(self):

        return self.settings.value(
            "last_excel_file",
            "",
            type=str,
        )

    def set_last_excel_file(
        self,
        filename,
    ):

        self.settings.setValue(
            "last_excel_file",
            filename,
        )

    # --------------------------------------------------
    # Excel-Ordner
    # --------------------------------------------------

    def get_last_excel_folder(self):

        return self.settings.value(
            "last_excel_folder",
            str(EXCEL_FOLDER),
            type=str,
        )

    def set_last_excel_folder(
        self,
        folder,
    ):

        self.settings.setValue(
            "last_excel_folder",
            folder,
        )

    # --------------------------------------------------
    # Ausgabeordner
    # --------------------------------------------------

    def get_last_output_folder(self):

        return self.settings.value(
            "last_output_folder",
            str(CATALOG_FOLDER),
            type=str,
        )

    def set_last_output_folder(
        self,
        folder,
    ):

        self.settings.setValue(
            "last_output_folder",
            folder,
        )