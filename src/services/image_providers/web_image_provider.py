"""
KatalogFactory by U.L.

Datei:
web_image_provider.py

Version:
0.3.1

Beschreibung:
Vorbereitung der zukünftigen
Websuche nach Produktbildern.

Der Provider erhält den kompletten
Artikeldatensatz und kann dadurch
später auf alle Informationen
zugreifen.
"""

from services.image_providers.base_provider import BaseProvider


class WebImageProvider(BaseProvider):

    @property
    def name(self):
        return "Web Image"

    def get_image_url(
        self,
        gtin,
        artikel=None,
    ):

        print("[WEB] -------------------------")
        print(f"[WEB] GTIN: {gtin}")

        if artikel is not None and hasattr(artikel, "get"):

            artikelname = artikel.get(
                "Artikel",
                ""
            )

            hersteller = artikel.get(
                "Zusatztext",
                ""
            )

            print(f"[WEB] Artikel    : {artikelname}")
            print(f"[WEB] Hersteller: {hersteller}")

        else:

            print(
                "[WEB] Kein Artikeldatensatz übergeben."
            )

        print(
            "[WEB] Websuche noch nicht implementiert."
        )

        print("[WEB] -------------------------")

        return None