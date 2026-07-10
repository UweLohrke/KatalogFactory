"""
KatalogFactory

Datei:
image_loader.py

Version:
0.6.1

Beschreibung:
Lädt Produktbilder anhand der EH-GTIN.
"""

from pathlib import Path


class ImageLoader:

    def __init__(self):

        project_path = Path(__file__).resolve().parents[2]
        self.image_folder = project_path / "bilder"

    def get_image(self, artikel):

        gtin = str(artikel["EH GTIN"]).strip()

        image_path = self.image_folder / f"{gtin}.jpg"

        if image_path.exists():
            return image_path

        return None