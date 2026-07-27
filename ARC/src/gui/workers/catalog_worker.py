"""
KatalogFactory by U.L.

Datei:
catalog_worker.py

Version:
1.0.0

Beschreibung:
Worker für die Katalogerstellung.
Wird später in einem eigenen Thread ausgeführt.
"""

from PySide6.QtCore import QObject, Signal

from services.catalog_service import CatalogService


class CatalogWorker(QObject):

    finished = Signal(str)

    error = Signal(str)

    def __init__(
        self,
        excel_file,
        region,
        output_folder,
    ):

        super().__init__()

        self.catalog_service = CatalogService()

        self.excel_file = excel_file
        self.region = region
        self.output_folder = output_folder

    def run(self):

        try:

            pdf = self.catalog_service.create_catalog(
                excel_file=self.excel_file,
                region=self.region,
                output_folder=self.output_folder,
            )

            self.finished.emit(str(pdf))

        except Exception as error:

            self.error.emit(str(error))