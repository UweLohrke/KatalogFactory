"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.9.1

Beschreibung:
Hauptfenster der KatalogFactory.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from config.app_config import (
    STATUS_ERROR,
    STATUS_LOADING,
    STATUS_READY,
    STATUS_SUCCESS,
    WINDOW_HEIGHT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_WIDTH,
)

from services.catalog_service import CatalogService

from gui.widgets.header_widget import HeaderWidget
from gui.widgets.file_selector import FileSelector
from gui.widgets.region_selector import RegionSelector
from gui.widgets.output_selector import OutputSelector
from gui.widgets.create_button import CreateButton


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.catalog_service = CatalogService()

        self.setWindowTitle(
            "KatalogFactory by U.L."
        )

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        )

        self.setMinimumSize(
            WINDOW_MIN_WIDTH,
            WINDOW_MIN_HEIGHT,
        )

        self.create_ui()

    # --------------------------------------------------
    # Oberfläche
    # --------------------------------------------------

    def create_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget,
        )

        layout = QVBoxLayout()

        layout.setAlignment(
            Qt.AlignTop,
        )

        layout.setContentsMargins(
            30,
            25,
            30,
            20,
        )

        layout.setSpacing(
            16,
        )

        central_widget.setLayout(
            layout,
        )

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        self.header = HeaderWidget()

        layout.addWidget(
            self.header,
        )

        # --------------------------------------------------
        # Excel-Datei
        # --------------------------------------------------

        self.file_selector = FileSelector()

        layout.addWidget(
            self.file_selector,
        )

        # --------------------------------------------------
        # Region
        # --------------------------------------------------

        self.region_selector = RegionSelector(
            self.catalog_service,
        )

        layout.addWidget(
            self.region_selector,
        )

        # --------------------------------------------------
        # Ausgabeordner
        # --------------------------------------------------

        self.output_selector = OutputSelector()

        layout.addWidget(
            self.output_selector,
        )

        # --------------------------------------------------
        # Button
        # --------------------------------------------------

        self.create_button = CreateButton()

        self.create_button.get_button().clicked.connect(
            self.create_catalog,
        )

        layout.addWidget(
            self.create_button,
        )

        layout.addStretch()

        # --------------------------------------------------
        # Statusleiste
        # --------------------------------------------------

        self.status_bar = QStatusBar()

        self.status_bar.showMessage(
            STATUS_READY,
        )

        self.setStatusBar(
            self.status_bar,
        )

    # --------------------------------------------------
    # Katalog erstellen
    # --------------------------------------------------

    def create_catalog(self):

        excel_file = self.file_selector.get_file_path()

        region = self.region_selector.get_selected_region()

        output_folder = self.output_selector.get_output_path()

        if not excel_file:

            QMessageBox.warning(
                self,
                "Fehler",
                "Bitte eine Excel-Datei auswählen.",
            )

            return

        if not output_folder:

            QMessageBox.warning(
                self,
                "Fehler",
                "Bitte einen Ausgabeordner auswählen.",
            )

            return

        self.status_bar.showMessage(
            STATUS_LOADING,
        )

        try:

            pdf = self.catalog_service.create_catalog(
                excel_file=excel_file,
                region=region,
                output_folder=output_folder,
            )

            self.status_bar.showMessage(
                STATUS_SUCCESS,
            )
            

            QMessageBox.information(
                self,
                "Fertig",
                f"PDF erfolgreich erstellt:\n\n{pdf}",
            )

        except Exception as error:

            self.status_bar.showMessage(
                STATUS_ERROR,
            )

            QMessageBox.critical(
                self,
                "Fehler",
                str(error),
            )

def run():

    app = QApplication(
        sys.argv,
    )

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec(),
    )