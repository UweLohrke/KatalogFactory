"""
KatalogFactory by U.L.

Datei:
catalog_service.py

Version:
0.8.0a

Beschreibung:
Steuert den kompletten Ablauf der Katalogerstellung.
Die GUI ruft später ausschließlich diese Klasse auf.
"""

from importer.rewe_importer import ReweImporter
from catalog.catalog_builder import CatalogBuilder
from pdf.pdf_generator import PDFGenerator


class CatalogService:

    def __init__(self):

        self.importer = ReweImporter()
        self.builder = CatalogBuilder()
        self.pdf_generator = PDFGenerator()

    # --------------------------------------------------
    # Verfügbare Regionen
    # --------------------------------------------------

    def get_regions(self):

        return self.importer.get_regions()

    # --------------------------------------------------
    # Katalog erstellen
    # --------------------------------------------------

    def create_catalog(self, region):

        dataframe = self.importer.get_articles_for_region(region)

        katalog = self.builder.build(dataframe)

        pdf_datei = self.pdf_generator.create_pdf(
            region=region,
            katalog=katalog,
        )

        return pdf_datei