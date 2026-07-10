"""
KatalogFactory

Datei:
image_loader.py

Version:
0.7.2

Beschreibung:
Lädt Produktbilder anhand der EH-GTIN und stellt
Hilfsfunktionen für die Bilddarstellung bereit.
"""

from pathlib import Path
from PIL import Image


class ImageLoader:

    def __init__(self):

        project_path = Path(__file__).resolve().parents[2]
        self.image_folder = project_path / "bilder"

    # --------------------------------------------------
    # Bildpfad ermitteln
    # --------------------------------------------------

    def get_image(self, artikel):

        gtin = str(artikel["EH GTIN"]).strip()

        image_path = self.image_folder / f"{gtin}.jpg"

        if image_path.exists():
            return image_path

        return None

    # --------------------------------------------------
    # Bild vorhanden?
    # --------------------------------------------------

    def has_image(self, artikel):

        return self.get_image(artikel) is not None

    # --------------------------------------------------
    # Originalgröße des Bildes
    # --------------------------------------------------

    def get_image_size(self, artikel):

        image_path = self.get_image(artikel)

        if image_path is None:
            return None

        with Image.open(image_path) as image:
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
        """
        Berechnet die optimale Bildgröße innerhalb
        eines festen Bildrahmens.

        Rückgabe:
            draw_width,
            draw_height,
            offset_x,
            offset_y
        """

        scale = min(
            frame_width / image_width,
            frame_height / image_height,
        )

        draw_width = image_width * scale
        draw_height = image_height * scale

        offset_x = (frame_width - draw_width) / 2
        offset_y = (frame_height - draw_height) / 2

        return (
            draw_width,
            draw_height,
            offset_x,
            offset_y,
        )