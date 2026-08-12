"""
KatalogFactory by U.L.

Datei:
region_selector.py

Version:
0.9.0

Beschreibung:
Widget zur Auswahl einer Region.

Die Regionen werden erst geladen,
wenn der Benutzer eine Excel-Datei
ausgewählt hat.
"""

from pathlib import Path

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
        self.excel_file = None

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

        self.region_combo.setEnabled(
            False,
        )

        layout.addWidget(
            self.region_combo,
        )

    # --------------------------------------------------
    # Excel-Datei setzen
    # --------------------------------------------------

    def set_excel_file(
        self,
        excel_file,
    ):

        self.excel_file = Path(
            excel_file,
        )

        self.load_regions()

    # --------------------------------------------------
    # Regionen laden
    # --------------------------------------------------

    def load_regions(self):

        self.region_combo.clear()

        if self.excel_file is None:

            self.region_combo.setEnabled(
                False,
            )

            return

        regionen = self.catalog_service.get_regions(
            excel_file=self.excel_file,
        )

        self.region_combo.addItems(
            regionen,
        )

        self.region_combo.setEnabled(
            bool(regionen),
        )

    # --------------------------------------------------
    # Aktuelle Auswahl
    # --------------------------------------------------

    def get_selected_region(self):

        return self.region_combo.currentText()
