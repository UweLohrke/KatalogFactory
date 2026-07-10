"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.8.4

Beschreibung:
Hauptfenster der KatalogFactory.
Zusammenführung der GUI-Widgets.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
    QComboBox,
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

        layout.addWidget(
            HeaderWidget(),
        )

        # --------------------------------------------------
        # Excel-Auswahl
        # --------------------------------------------------

        self.file_selector = FileSelector()

        layout.addWidget(
            self.file_selector,
        )

        # --------------------------------------------------
        # Region
        # --------------------------------------------------

        layout.addWidget(
            QLabel("Region"),
        )

        self.region_combo = QComboBox()

        self.region_combo.addItems(
            self.catalog_service.get_regions()
        )

        layout.addWidget(
            self.region_combo,
        )

        layout.addStretch()

        # --------------------------------------------------
        # Status
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
        app.exec()
    )