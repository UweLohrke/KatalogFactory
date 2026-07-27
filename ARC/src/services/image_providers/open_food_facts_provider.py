"""
KatalogFactory by U.L.

Datei:
open_food_facts_provider.py

Version:
1.2.0

Beschreibung:
Bildprovider für Open Food Facts.
"""

from services.image_providers.base_provider import (
    BaseProvider,
)

from services.open_food_facts_client import (
    OpenFoodFactsClient,
)


class OpenFoodFactsProvider(BaseProvider):

    def __init__(self):

        self.client = OpenFoodFactsClient()

    @property
    def name(self):

        return "Open Food Facts"

    def get_image_url(
        self,
        gtin,
        artikel=None,
    ):

        return self.client.get_image_url(
            gtin,
        )