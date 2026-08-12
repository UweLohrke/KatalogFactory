"""
KatalogFactory by U.L.

Datei:
catalog_service.py

Version:
1.2.0

Beschreibung:
Steuert den kompletten Ablauf der Katalogerstellung.
Die GUI kommuniziert ausschließlich mit dieser Klasse.
"""

from pathlib import Path

from importer.rewe_importer import ReweImporter
from catalog.catalog_builder import CatalogBuilder
from pdf.pdf_generator import PDFGenerator
from services.image_service import ImageService


class CatalogService:

    def __init__(self):

        self.importer = ReweImporter()
        self.builder = CatalogBuilder()
        self.pdf_generator = PDFGenerator()
        self.image_service = ImageService()

    # --------------------------------------------------
    # Regionen
    # --------------------------------------------------

    def get_regions(
        self,
        excel_file=None,
    ):

        return self.importer.get_regions(
            excel_file=excel_file,
        )

    # --------------------------------------------------
    # Katalog erstellen
    # --------------------------------------------------

    def create_catalog(
        self,
        excel_file,
        region,
        output_folder,
    ):
        """
        Erstellt einen PDF-Katalog.

        Parameter
        ----------
        excel_file : str | Path
            Pfad zur Excel-Datei.

        region : str
            Gewählte Region.

        output_folder : str | Path
            Zielordner für den PDF-Katalog.
        """

        excel_file = Path(
            excel_file,
        )

        output_folder = Path(
            output_folder,
        )

        # Excel laden

        dataframe = self.importer.get_articles_for_region(
            region,
            excel_file=excel_file,
        )

        # Hersteller gruppieren

        katalog = self.builder.build(
            dataframe,
        )

        # ----------------------------------------------
        # Fehlende Bilder herunterladen
        # ----------------------------------------------

        self.image_service.download_missing_images(
            katalog,
        )

        # ----------------------------------------------
        # PDF erzeugen
        # ----------------------------------------------

        pdf_datei = self.pdf_generator.create_pdf(
            region=region,
            katalog=katalog,
            output_folder=output_folder,
        )

        return pdf_datei
