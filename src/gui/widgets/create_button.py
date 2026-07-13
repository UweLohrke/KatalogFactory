"""
KatalogFactory by U.L.

Datei:
create_button.py

Version:
0.9.3

Beschreibung:
Widget für den Button
"Katalog erstellen".
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CreateButton(QWidget):

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
            20,
            0,
            0,
        )

        self.setLayout(
            layout,
        )

        self.button = QPushButton(
            "KATALOG ERSTELLEN",
        )

        self.button.setMinimumHeight(
            48,
        )

        self.button.setCursor(
            Qt.PointingHandCursor,
        )

        self.button.setStyleSheet(
            """
            QPushButton {

                font-size: 15px;
                font-weight: bold;

            }
            """
        )

        layout.addWidget(
            self.button,
        )

    # --------------------------------------------------
    # Zugriff auf Button
    # --------------------------------------------------

    def get_button(self):

        return self.button

    # --------------------------------------------------
    # Button deaktivieren
    # --------------------------------------------------

    def disable(self):

        self.button.setEnabled(
            False,
        )

    # --------------------------------------------------
    # Button aktivieren
    # --------------------------------------------------

    def enable(self):

        self.button.setEnabled(
            True,
        )