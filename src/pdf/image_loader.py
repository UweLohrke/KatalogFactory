"""
KatalogFactory

Datei:
image_loader.py

Version:
0.7.1

Beschreibung:
Lädt Produktbilder anhand der EH-GTIN und liefert
Informationen über vorhandene Bilder.
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
    # Bildgröße ermitteln
    # --------------------------------------------------

    def get_image_size(self, artikel):

        image_path = self.get_image(artikel)

        if image_path is None:
            return None

        with Image.open(image_path) as image:

            return image.size

    # --------------------------------------------------
    # Prüfen, ob Bild vorhanden
    # --------------------------------------------------

    def has_image(self, artikel):

        return self.get_image(artikel) is not None