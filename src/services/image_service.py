"""
KatalogFactory by U.L.

Datei:
image_service.py

Version:
1.1.2

Beschreibung:
Verwaltet Produktbilder.

Aufgaben:
- Lokalen Bildcache verwalten
- Fehlende Bilder herunterladen
- Bilder aktualisieren
"""

from pathlib import Path

import requests

from services.image_providers.provider_manager import (
    ProviderManager,
)


class ImageService:

    def __init__(self):

        project_path = Path(__file__).resolve().parents[2]

        self.image_folder = project_path / "bilder"

        self.image_folder.mkdir(
            exist_ok=True,
        )

        self.provider_manager = ProviderManager()

    # --------------------------------------------------
    # Bildpfad ermitteln
    # --------------------------------------------------

           # --------------------------------------------------
    # Bildpfad ermitteln
    # --------------------------------------------------

    def get_image_path(
        self,
        gtin,
    ):


        gtin = str(gtin).strip()

        image_path = (
            self.image_folder /
            f"{gtin}.jpg"
        )

        print(f"GTIN: {gtin}")
        print(f"Suche: {image_path}")
        print(f"Existiert: {image_path.exists()}")

        if image_path.exists():

            return image_path

        return None

    # --------------------------------------------------
    # Bild vorhanden?
    # --------------------------------------------------

    def has_image(
        self,
        gtin,
    ):

        return (
            self.get_image_path(
                gtin,
            )
            is not None
        )

    # --------------------------------------------------
    # Einzelnes Bild herunterladen
    # --------------------------------------------------

    def download_image(
        self,
        gtin,
    ):

        image_url = self.provider_manager.get_image_url(
            gtin,
    )

        if image_url is None:

            return None

        image_path = (
            self.image_folder /
            f"{gtin}.jpg"
        )

        try:

            response = requests.get(
                image_url,
                timeout=20,
            )

            if response.status_code != 200:

                return None

            image_path.write_bytes(
                response.content,
            )

            return image_path

        except Exception:

            return None

    # --------------------------------------------------
    # Bild aus lokalem Cache liefern
    # --------------------------------------------------

    def get_image(
        self,
        gtin,
    ):
        """
        Liefert ausschließlich ein lokal
        vorhandenes Bild.

        Während der PDF-Erstellung werden
        keine Internetzugriffe durchgeführt.
        """

        return self.get_image_path(
            gtin,
        )

    # --------------------------------------------------
    # Fehlende Bilder herunterladen
    # --------------------------------------------------

    def download_missing_images(
        self,
        katalog,
    ):

        gtins = set()

        for artikel_liste in katalog.values():

            for artikel in artikel_liste:

                gtin = str(
                    artikel["EH GTIN"]
                ).strip()

                gtins.add(
                    gtin,
                )

        print()

        print(
            f"{len(gtins)} eindeutige GTIN(s) gefunden."
        )

        print()

        downloaded = 0
        skipped = 0
        missing = 0

        for gtin in sorted(gtins):

            if self.has_image(
                gtin,
            ):

                skipped += 1

                continue

            print(
                f"Lade Bild: {gtin}"
            )

            image = self.download_image(
                gtin,
            )

            if image is None:

                missing += 1

            else:

                downloaded += 1

        print()

        print(
            "Bildprüfung abgeschlossen."
        )

        print(
            f"Vorhanden : {skipped}"
        )

        print(
            f"Geladen   : {downloaded}"
        )

        print(
            f"Kein Bild : {missing}"
        )

        print()