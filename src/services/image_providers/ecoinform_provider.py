"""
KatalogFactory by U.L.

Datei:
ecoinform_provider.py

Version:
2.1.0

Beschreibung:
Bildprovider für lokale Ecoinform-Bilder.

Die Bilder liegen zentral im
iCloud-Ordner der KatalogFactory.
"""

from pathlib import Path

from config.app_config import IMAGE_FOLDER

from services.image_providers.base_provider import (
    BaseProvider,
)


class EcoinformProvider(BaseProvider):

    def __init__(self):

        self.image_folder = Path(
            IMAGE_FOLDER,
        )

    # --------------------------------------------------
    # Provider-Name
    # --------------------------------------------------

    @property
    def name(self):

        return "Ecoinform"

    # --------------------------------------------------
    # Bild suchen
    # --------------------------------------------------

    def get_image_url(
        self,
        gtin,
        artikel=None,
    ):

        gtin = str(
            gtin
        ).strip()

        image = (
            self.image_folder /
            f"{gtin}.jpg"
        )

        if image.exists():

            return image

        return None
