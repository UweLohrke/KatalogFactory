"""
KatalogFactory by U.L.

Datei:
output_selector.py

Version:
0.8.6

Beschreibung:
Widget zur Auswahl des Ausgabeordners.
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


class OutputSelector(QWidget):

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

        label = QLabel(
            "Ausgabeordner",
        )

        layout.addWidget(
            label,
        )

        row = QHBoxLayout()

        self.output_path = QLineEdit()

        self.output_path.setPlaceholderText(
            "Kein Ausgabeordner ausgewählt..."
        )

        button = QPushButton(
            "Auswählen..."
        )

        button.clicked.connect(
            self.select_folder,
        )

        row.addWidget(
            self.output_path,
        )

        row.addWidget(
            button,
        )

        layout.addLayout(
            row,
        )

    # --------------------------------------------------
    # Ordner auswählen
    # --------------------------------------------------

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Ausgabeordner auswählen",
        )

        if folder:

            self.output_path.setText(
                folder,
            )

    # --------------------------------------------------
    # Zugriff von außen
    # --------------------------------------------------

    def get_output_path(self):

        return self.output_path.text()