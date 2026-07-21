"""
KatalogFactory by U.L.

Datei:
open_food_facts_client.py

Version:
1.1.0

Beschreibung:
Kommunikation mit der
Open Food Facts API.

Liefert die Bild-URL
zu einer EH-GTIN.
"""

import requests


class OpenFoodFactsClient:

    BASE_URL = (
        "https://world.openfoodfacts.org/api/v2/product"
    )

    def __init__(self):

        self.timeout = 10

        self.headers = {
            "User-Agent": (
                "KatalogFactory/1.1 "
                "(https://github.com/ul/katalogfactory)"
            ),
            "Accept": "application/json",
        }

    # --------------------------------------------------
    # Bild-URL ermitteln
    # --------------------------------------------------

    def get_image_url(
        self,
        gtin,
    ):

        gtin = str(
            gtin,
        ).strip()

        url = (
            f"{self.BASE_URL}/{gtin}.json"
        )

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
            )

            print(
                "HTTP:",
                response.status_code,
            )

            if response.status_code != 200:

                return None

            data = response.json()

            product = data.get(
                "product",
                {},
            )

            image_url = product.get(
                "image_front_url",
            )

            print(
                "Bild:",
                image_url,
            )

            return image_url

        except Exception as error:

            print(
                "Fehler:",
                error,
            )

            return None