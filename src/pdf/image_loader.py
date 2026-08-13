"""
KatalogFactory by U.L.

Datei:
image_loader.py

Version:
1.2.0

Beschreibung:
Lädt Produktbilder über den ImageService
und stellt Hilfsfunktionen für die
Bilddarstellung bereit.

Wenn kein Ecoinform-Bild vorhanden ist,
wird der zentrale Produktbild-Platzhalter
verwendet.
"""

from PIL import Image

from config.app_config import (
    PLACEHOLDER_IMAGE,
)

from services.image_service import (
    ImageService,
)


class ImageLoader:

    def __init__(self):

        self.image_service = ImageService()

    # --------------------------------------------------
    # Bildpfad ermitteln
    # --------------------------------------------------

    def get_image(
        self,
        artikel,
    ):

        gtin = str(
            artikel["EH GTIN"]
        ).strip()

        image_path = (
            self.image_service.get_image(
                gtin,
            )
        )

        if image_path is not None:

            return image_path

        # --------------------------------------------------
        # Kein Ecoinform-Bild vorhanden
        # --------------------------------------------------

        print(
            f"[BILD] Kein Ecoinform-Bild: {gtin}"
        )

        print(
            f"[BILD] Verwende Platzhalter: "
            f"{PLACEHOLDER_IMAGE}"
        )

        return PLACEHOLDER_IMAGE

    # --------------------------------------------------
    # Bild vorhanden?
    # --------------------------------------------------

    def has_image(
        self,
        artikel,
    ):

        gtin = str(
            artikel["EH GTIN"]
        ).strip()

        return (
            self.image_service.get_image(
                gtin,
            )
            is not None
        )

    # --------------------------------------------------
    # Originalgröße des Bildes
    # --------------------------------------------------

    def get_image_size(
        self,
        artikel,
    ):

        image_path = self.get_image(
            artikel,
        )

        if image_path is None:

            return None

        with Image.open(
            image_path,
        ) as image:

            return image.size

    # --------------------------------------------------
    # Optimale Darstellung im Bildrahmen berechnen
    # --------------------------------------------------

    def calculate_image_layout(
        self,
        image_width,
        image_height,
        frame_width,
        frame_height,
    ):

        scale = min(
            frame_width / image_width,
            frame_height / image_height,
        )

        draw_width = (
            image_width * scale
        )

        draw_height = (
            image_height * scale
        )

        offset_x = (
            frame_width - draw_width
        ) / 2

        offset_y = (
            frame_height - draw_height
        ) / 2

        return (
            draw_width,
            draw_height,
            offset_x,
            offset_y,
        )