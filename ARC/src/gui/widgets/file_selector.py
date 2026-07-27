"""
KatalogFactory by U.L.

Datei:
file_selector.py

Version:
1.0.0

Beschreibung:
Widget zur Auswahl einer Excel-Datei.
Merkt sich automatisch den zuletzt verwendeten Ordner.
"""

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from gui.settings.app_settings import AppSettings


class FileSelector(QWidget):

    def __init__(self):

        super().__init__()

        self.settings = AppSettings()

        self.create_ui()
        self.file_path.setText(
    self.settings.get_last_excel_file()
)

    # --------------------------------------------------
    # Oberfläche
    # --------------------------------------------------

    def create_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.setLayout(
            layout,
        )

        label = QLabel(
            "Excel-Datei",
        )

        layout.addWidget(
            label,
        )

        row = QHBoxLayout()

        self.file_path = QLineEdit()

        self.file_path.setPlaceholderText(
            "Keine Datei ausgewählt..."
        )

        button = QPushButton(
            "Auswählen..."
        )

        button.clicked.connect(
            self.select_file,
        )

        row.addWidget(
            self.file_path,
        )

        row.addWidget(
            button,
        )

        layout.addLayout(
            row,
        )

    # --------------------------------------------------
    # Datei auswählen
    # --------------------------------------------------

    def select_file(self):

        last_folder = self.settings.get_last_excel_folder()

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Excel-Datei auswählen",
            last_folder,
            "Excel (*.xlsx *.xls)",
        )

        if filename:

            self.file_path.setText(
                filename,
            )

            self.settings.set_last_excel_folder(
                str(Path(filename).parent)
            )
            self.settings.set_last_excel_file(
                filename
            )

    # --------------------------------------------------
    # Zugriff von außen
    # --------------------------------------------------

    def get_file_path(self):

        return self.file_path.text()