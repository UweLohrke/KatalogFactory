"""
KatalogFactory by U.L.

Datei:
header_widget.py

Version:
1.0.0

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

        main_layout.setSpacing(
            2,
        )

        self.setLayout(
            main_layout,
        )

        # --------------------------------------------------
        # Titel
        # --------------------------------------------------

        title_layout = QHBoxLayout()

        title_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        title_layout.setSpacing(
            1,
        )

        title_layout.setAlignment(
            Qt.AlignLeft,
        )

        title = QLabel(
            "KatalogFactory"
        )

        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            """
        )

        signature = QLabel(
            "by U.L."
        )

        signature.setStyleSheet(
            """
            font-size: 9px;
            color: #9A9A9A;
            padding-top: 11px;
            """
        )

        title_layout.addWidget(
            title,
        )

        title_layout.addWidget(
            signature,
        )

        title_layout.addStretch()

        main_layout.addLayout(
            title_layout,
        )

        # --------------------------------------------------
        # Version
        # --------------------------------------------------

        version = QLabel(
            f"Version {APP_VERSION}"
        )

        version.setStyleSheet(
            """
            color: #8A8A8A;
            font-size: 11px;
            """
        )

        main_layout.addWidget(
            version,
        )