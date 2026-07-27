"""
KatalogFactory

Datei:
barcode_generator.py

Version:
0.6.2

Beschreibung:
Erzeugt einen EAN-13 Barcode aus der EH-GTIN.
"""

from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF


class BarcodeGenerator:

    def draw(self, pdf, gtin, x, y):

        gtin = str(gtin).strip()

        # ReportLab erwartet die ersten 12 Stellen.
        # Die Prüfziffer wird automatisch berechnet.
        if len(gtin) == 13:
            gtin = gtin[:-1]

        barcode = eanbc.Ean13BarcodeWidget(gtin)

        barcode.barWidth = 0.85
        barcode.barHeight = 18

        drawing = Drawing(95, 45)
        drawing.add(barcode)

        renderPDF.draw(
            drawing,
            pdf,
            x,
            y,
        )