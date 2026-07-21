"""
KatalogFactory by U.L.

Datei:
manufacturer_provider.py

Version:
1.2.0

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
        Zurzeit noch keine Suche.

        Rückgabe:
            None
        """

        return None