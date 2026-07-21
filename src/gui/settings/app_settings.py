"""
KatalogFactory by U.L.

Datei:
app_settings.py

Version:
1.0.0

Beschreibung:
Zentrale Verwaltung aller Programmeinstellungen.
"""

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
            "",
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
            "",
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