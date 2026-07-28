"""
KatalogFactory by U.L.

Datei:
manufacturer_service.py

Version:
1.0.0

Beschreibung:
Verwaltet Herstellerinformationen.

Diese erste Version prüft lediglich,
ob ein Hersteller in der bekannten
Herstellerdatenbank vorhanden ist.

Später wird dieser Service die
SQLite-Datenbank verwenden.
"""

from config.manufacturer_aliases import (
    MANUFACTURER_ALIASES,
)

from config.manufacturers import (
    MANUFACTURERS,
)


class ManufacturerService:

    @staticmethod
    def normalize(name):

        if not name:
            return ""

        name = (
            str(name)
            .strip()
            .upper()
        )

        return MANUFACTURER_ALIASES.get(
            name,
            name,
        )

    @staticmethod
    def exists(name):

        name = ManufacturerService.normalize(
            name
        )

        return name in MANUFACTURERS

    @staticmethod
    def get(name):

        name = ManufacturerService.normalize(
            name
        )

        return MANUFACTURERS.get(name)