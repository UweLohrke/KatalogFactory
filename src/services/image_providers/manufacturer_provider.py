"""
KatalogFactory by U.L.

Datei:
manufacturer_provider.py

Version:
1.3.0

Beschreibung:
Bildprovider für Herstellerbilder.

Diese Klasse sucht Produktbilder
direkt beim Hersteller.

Die eigentliche Suchlogik wird
schrittweise erweitert.
"""

from services.image_providers.base_provider import (
    BaseProvider,
)


class ManufacturerProvider(BaseProvider):

    @property
    def name(self):

        return "Hersteller"

    def get_image_url(
        self,
        gtin,
        artikel=None,
    ):
        """
        Vorbereitungsstufe für die Herstellersuche.

        Momentan werden lediglich
        Informationen ausgegeben.
        Die eigentliche Suche folgt
        im nächsten Sprint.
        """

        print(
            f"[HERSTELLER] GTIN: {gtin}"
        )

        if artikel is not None:

            artikelname = artikel.get(
                "Artikel",
                "Unbekannt",
            )

            print(
                f"[HERSTELLER] Artikel: {artikelname}"
            )

        return None