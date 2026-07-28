"""
KatalogFactory by U.L.

Datei:
manufacturer_provider.py

Version:
1.5.0

Beschreibung:
Bildprovider für Herstellerbilder.

Diese Klasse sucht Produktbilder
direkt beim Hersteller.

Vor der Suche wird der Herstellername
über die Alias-Tabelle auf eine
einheitliche Schreibweise normalisiert.
"""

from services.image_providers.base_provider import (
    BaseProvider,
)

from config.manufacturers import (
    MANUFACTURERS,
)

from config.manufacturer_aliases import (
    MANUFACTURER_ALIASES,
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

        print(
            f"[HERSTELLER] GTIN: {gtin}"
        )

        if artikel is not None:

            artikelname = artikel.get(
                "Artikel",
                "Unbekannt",
            )

            hersteller = (
                artikel.get(
                    "Zusatztext",
                    "",
                )
                .strip()
                .upper()
            )

            hersteller = MANUFACTURER_ALIASES.get(
                hersteller,
                hersteller,
            )

            print(
                f"[HERSTELLER] Artikel: {artikelname}"
            )

            print(
                f"[HERSTELLER] Hersteller: {hersteller}"
            )

            daten = MANUFACTURERS.get(
                hersteller
            )

            if daten:

                print(
                    f"[HERSTELLER] Website: {daten['website']}"
                )

            else:

                print(
                    "[HERSTELLER] Hersteller nicht in Datenbank."
                )

        return None