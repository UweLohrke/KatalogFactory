"""
KatalogFactory by U.L.

Datei:
main_window.py

Version:
0.8.1

Beschreibung:
Hauptfenster der KatalogFactory.
Erste GUI mit Auswahl einer Excel-Datei.
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
    APP_NAME,
    APP_VERSION,
    STATUS_READY,
    WINDOW_HEIGHT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_WIDTH,
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(APP_NAME)

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
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(30, 25, 30, 20)
        layout.setSpacing(15)

        central_widget.setLayout(layout)

        # --------------------------------------------------
        # Titel
        # --------------------------------------------------

        title = QLabel(APP_NAME)
        title.setStyleSheet(
            "font-size:24px; font-weight:bold;"
        )

        layout.addWidget(title)

        version = QLabel(f"Version {APP_VERSION}")
        version.setStyleSheet("color: gray;")

        layout.addWidget(version)

        layout.addSpacing(20)

        # --------------------------------------------------
        # Excel-Datei
        # --------------------------------------------------

        label = QLabel("Excel-Datei")

        layout.addWidget(label)

        row = QHBoxLayout()

        self.excel_path = QLineEdit()
        self.excel_path.setPlaceholderText(
            "Keine Datei ausgewählt..."
        )

        button = QPushButton("Auswählen...")

        button.clicked.connect(
            self.select_excel_file,
        )

        row.addWidget(self.excel_path)
        row.addWidget(button)

        layout.addLayout(row)

        layout.addStretch()

        # --------------------------------------------------
        # Statusleiste
        # --------------------------------------------------

        status = QStatusBar()
        status.showMessage(STATUS_READY)

        self.setStatusBar(status)

    # --------------------------------------------------
    # Excel-Datei auswählen
    # --------------------------------------------------

    def select_excel_file(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Excel-Datei auswählen",
            "",
            "Excel (*.xlsx *.xls)",
        )

        if filename:

            self.excel_path.setText(filename)


def run():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())