"""
KatalogFactory by U.L.

Datei:
unknown_manufacturer_service.py

Version:
1.0.0

Beschreibung:
Sammelt unbekannte Hersteller.

Jeder unbekannte Hersteller wird
pro Programmlauf nur einmal gespeichert.

Später dient dieser Service als
Grundlage für die GUI und die
automatische Erweiterung der
Herstellerdatenbank.
"""


class UnknownManufacturerService:

    _manufacturers = set()

    @classmethod
    def add(cls, name):

        if not name:
            return

        cls._manufacturers.add(name)

    @classmethod
    def exists(cls, name):

        return name in cls._manufacturers

    @classmethod
    def get_all(cls):

        return sorted(cls._manufacturers)

    @classmethod
    def clear(cls):

        cls._manufacturers.clear()

    @classmethod
    def count(cls):

        return len(cls._manufacturers)