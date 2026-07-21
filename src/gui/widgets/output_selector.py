"""
KatalogFactory by U.L.

Datei:
output_selector.py

Version:
1.0.0

Beschreibung:
Widget zur Auswahl des Ausgabeordners.
Merkt sich automatisch den zuletzt verwendeten Ordner.
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

from gui.settings.app_settings import AppSettings


class OutputSelector(QWidget):

    def __init__(self):

        super().__init__()

        self.settings = AppSettings()

        self.create_ui()
        self.output_path.setText(
        self.settings.get_last_output_folder()
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

        last_folder = self.settings.get_last_output_folder()

        folder = QFileDialog.getExistingDirectory(
            self,
            "Ausgabeordner auswählen",
            last_folder,
        )

        if folder:

            self.output_path.setText(
                folder,
            )

            self.settings.set_last_output_folder(
                folder,
            )

    # --------------------------------------------------
    # Zugriff von außen
    # --------------------------------------------------

    def get_output_path(self):

        return self.output_path.text()