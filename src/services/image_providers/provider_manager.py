"""
KatalogFactory by U.L.

Datei:
provider_manager.py

Version:
1.2.1

Beschreibung:
Verwaltet alle Bildprovider.

Die Provider werden in einer
festen Reihenfolge abgefragt,
bis ein Bild gefunden wurde.
"""

from services.image_providers.manufacturer_provider import (
    ManufacturerProvider,
)

from services.image_providers.open_food_facts_provider import (
    OpenFoodFactsProvider,
)


class ProviderManager:

    def __init__(self):

        self.providers = [

            ManufacturerProvider(),

            OpenFoodFactsProvider(),

        ]

    # --------------------------------------------------
    # Bild suchen
    # --------------------------------------------------

    def get_image_url(
        self,
        gtin,
        artikel=None,
    ):

        for provider in self.providers:

            print(
                f"Suche bei: {provider.name}"
            )

            image_url = provider.get_image_url(
                gtin,
                artikel,
            )

            if image_url is not None:

                print(
                    f"Bild gefunden über {provider.name}"
                )

                return image_url

        print(
            "Kein Bild gefunden."
        )

        return None