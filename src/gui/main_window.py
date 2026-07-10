"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.8.3

Beschreibung:
Hauptfenster der KatalogFactory.
Verwendet eigene GUI-Widgets.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
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
        # Excel-Datei
        # --------------------------------------------------

        layout.addWidget(
            QLabel("Excel-Datei")
        )

        excel_row = QHBoxLayout()

        self.excel_path = QLineEdit()

        self.excel_path.setPlaceholderText(
            "Keine Datei ausgewählt..."
        )

        button = QPushButton(
            "Auswählen..."
        )

        button.clicked.connect(
            self.select_excel_file,
        )

        excel_row.addWidget(
            self.excel_path,
        )

        excel_row.addWidget(
            button,
        )

        layout.addLayout(
            excel_row,
        )

        # --------------------------------------------------
        # Region
        # --------------------------------------------------

        layout.addWidget(
            QLabel("Region")
        )

        from PySide6.QtWidgets import QComboBox

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

    # --------------------------------------------------
    # Datei auswählen
    # --------------------------------------------------

    def select_excel_file(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Excel-Datei auswählen",
            "",
            "Excel (*.xlsx *.xls)",
        )

        if filename:

            self.excel_path.setText(
                filename,
            )


def run():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(
        app.exec()
    )