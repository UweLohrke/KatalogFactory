"""
KatalogFactory by U.L.

Datei:
region_selector.py

Version:
0.8.5

Beschreibung:
Widget zur Auswahl einer Region.
Die verfügbaren Regionen werden über
den CatalogService geladen.
"""

from PySide6.QtWidgets import (
    QLabel,
    QComboBox,
    QVBoxLayout,
    QWidget,
)


class RegionSelector(QWidget):

    def __init__(self, catalog_service):

        super().__init__()

        self.catalog_service = catalog_service

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
            "Region",
        )

        layout.addWidget(
            label,
        )

        self.region_combo = QComboBox()

        self.load_regions()

        layout.addWidget(
            self.region_combo,
        )

    # --------------------------------------------------
    # Regionen laden
    # --------------------------------------------------

    def load_regions(self):

        regionen = self.catalog_service.get_regions()

        self.region_combo.addItems(
            regionen,
        )

    # --------------------------------------------------
    # Aktuelle Auswahl
    # --------------------------------------------------

    def get_selected_region(self):

        return self.region_combo.currentText()