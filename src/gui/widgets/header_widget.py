"""
KatalogFactory by U.L.

Datei:
header_widget.py

Version:
0.8.3

Beschreibung:
Header-Widget der KatalogFactory.
Zeigt Programmname, Signatur und Version.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from config.app_config import APP_VERSION


class HeaderWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.create_ui()

    # --------------------------------------------------
    # Oberfläche
    # --------------------------------------------------

    def create_ui(self):

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.setLayout(
            main_layout,
        )

        # ----------------------------------------------
        # Titelzeile
        # ----------------------------------------------

        title_row = QHBoxLayout()

        title_row.setAlignment(
            Qt.AlignLeft,
        )

        title = QLabel(
            "KatalogFactory",
        )

        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            """
        )

        signature = QLabel(
            "by U.L.",
        )

        signature.setStyleSheet(
            """
            font-size: 10px;
            color: #A0A0A0;
            padding-top: 10px;
            padding-left: 5px;
            """
        )

        title_row.addWidget(
            title,
        )

        title_row.addWidget(
            signature,
        )

        title_row.addStretch()

        main_layout.addLayout(
            title_row,
        )

        # ----------------------------------------------
        # Version
        # ----------------------------------------------

        version = QLabel(
            f"Version {APP_VERSION}",
        )

        version.setStyleSheet(
            """
            color: gray;
            margin-top: 8px;
            """
        )

        main_layout.addWidget(
            version,
        )