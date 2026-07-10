"""
KatalogFactory by U.L.

Datei:
file_selector.py

Version:
0.8.4

Beschreibung:
Widget zur Auswahl einer Excel-Datei.
"""

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class FileSelector(QWidget):

    def __init__(self):

        super().__init__()

        self.create_ui()

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

        # Überschrift

        label = QLabel(
            "Excel-Datei",
        )

        layout.addWidget(
            label,
        )

        # Eingabezeile

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

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Excel-Datei auswählen",
            "",
            "Excel (*.xlsx *.xls)",
        )

        if filename:

            self.file_path.setText(
                filename,
            )

    # --------------------------------------------------
    # Zugriff von außen
    # --------------------------------------------------

    def get_file_path(self):

        return self.file_path.text()