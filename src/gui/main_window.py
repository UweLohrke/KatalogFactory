"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.8.6

Beschreibung:
Hauptfenster der KatalogFactory.
Zusammenführung aller GUI-Widgets.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from config.app_config import (
    STATUS_READY,
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

        layout.addStretch()

        # --------------------------------------------------
        # Statusleiste
        # --------------------------------------------------

        status = QStatusBar()

        status.showMessage(
            STATUS_READY,
        )

        self.setStatusBar(
            status,
        )


def run():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec(),
    )