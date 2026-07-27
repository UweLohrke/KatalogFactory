"""
KatalogFactory by U.L.

Datei:
open_food_facts_client.py

Version:
1.2.0

Beschreibung:
Kommunikation mit der
Open Food Facts API.

Liefert die Bild-URL
zu einer EH-GTIN.
"""

import time

import requests


class OpenFoodFactsClient:

    BASE_URL = (
        "https://world.openfoodfacts.org/api/v2/product"
    )

    def __init__(self):

        self.timeout = 10

        self.max_retries = 3

        self.retry_delay = 2

        self.headers = {
            "User-Agent": (
                "KatalogFactory/1.2 "
                "(https://github.com/UweLohrke/KatalogFactory)"
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

        for attempt in range(
            1,
            self.max_retries + 1,
        ):

            try:

                response = requests.get(
                    url,
                    headers=self.headers,
                    timeout=self.timeout,
                )

                print(
                    f"[OFF] Versuch {attempt}: HTTP {response.status_code}"
                )

                if response.status_code == 200:

                    data = response.json()

                    product = data.get(
                        "product",
                        {},
                    )

                    image_url = product.get(
                        "image_front_url",
                    )

                    if image_url:

                        print(
                            f"[OFF] Bild gefunden: {gtin}"
                        )

                    else:

                        print(
                            f"[OFF] Kein Bild: {gtin}"
                        )

                    return image_url

                if response.status_code in (
                    429,
                    500,
                    502,
                    503,
                    504,
                ):

                    print(
                        "[OFF] Server ausgelastet - neuer Versuch..."
                    )

                    if attempt < self.max_retries:

                        time.sleep(
                            self.retry_delay,
                        )

                    continue

                return None

            except requests.RequestException as error:

                print(
                    f"[OFF] Netzwerkfehler: {error}"
                )

                if attempt < self.max_retries:

                    time.sleep(
                        self.retry_delay,
                    )

        return None