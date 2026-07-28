"""
KatalogFactory by U.L.

Datei:
manufacturer_provider.py

Version:
1.7.0

Beschreibung:
Bildprovider für Herstellerbilder.

Verwendet den ManufacturerService
als zentrale Schnittstelle und sammelt
unbekannte Hersteller für die spätere
Bearbeitung.
"""

from services.image_providers.base_provider import BaseProvider

from services.manufacturer_service import ManufacturerService

from services.unknown_manufacturer_service import (
    UnknownManufacturerService,
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

        print(f"[HERSTELLER] GTIN: {gtin}")

        if artikel is None:
            return None

        artikelname = artikel.get(
            "Artikel",
            "Unbekannt",
        )

        hersteller = artikel.get(
            "Zusatztext",
            "",
        )

        hersteller = ManufacturerService.normalize(
            hersteller
        )

        print(f"[HERSTELLER] Artikel: {artikelname}")
        print(f"[HERSTELLER] Hersteller: {hersteller}")

        daten = ManufacturerService.get(
            hersteller
        )

        if daten:

            print(
                f"[HERSTELLER] Website: {daten['website']}"
            )

        else:

            UnknownManufacturerService.add(
                hersteller
            )

            print(
                "[HERSTELLER] Hersteller nicht in Datenbank."
            )

        return None