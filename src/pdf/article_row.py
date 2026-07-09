"""
KatalogFactory

Datei:
article_row.py

Version:
0.5.0

Beschreibung:
Zeichnet eine einzelne Artikelzeile in den PDF-Katalog.
In Version 0.5.0 werden zunächst Platzhalter für Produktbild
und Barcode verwendet.
"""

from reportlab.lib.units import cm


class ArticleRow:

    def draw(self, pdf, artikel, x, y, page_width):

        # --------------------------------------------------
        # Produktbild (Platzhalter)
        # --------------------------------------------------

        pdf.rect(
            x,
            y - 3 * cm,
            3 * cm,
            3 * cm
        )

        pdf.setFont("Helvetica", 8)

        pdf.drawCentredString(
            x + 1.5 * cm,
            y - 1.5 * cm,
            "Bild"
        )

        # --------------------------------------------------
        # Artikelinformationen
        # --------------------------------------------------

        text_x = x + 3.6 * cm

        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(
            text_x,
            y - 0.4 * cm,
            str(artikel["Artikel"])
        )

        pdf.setFont("Helvetica", 10)

        pdf.drawString(
            text_x,
            y - 1.0 * cm,
            str(artikel["Mengentext"])
        )

        pdf.drawString(
            text_x,
            y - 1.6 * cm,
            f"EH GTIN: {artikel['EH GTIN']}"
        )

        # --------------------------------------------------
        # Preise
        # --------------------------------------------------

        preis_x = page_width - 6 * cm

        pdf.setFont("Helvetica-Bold", 10)

        pdf.drawRightString(
            preis_x,
            y - 0.4 * cm,
            f"LP: {artikel['Listenpreis (EUR)']:.2f} €"
        )

        pdf.drawRightString(
            preis_x,
            y - 1.1 * cm,
            f"UVP: {artikel['UVP']:.2f} €"
        )

        # --------------------------------------------------
        # Barcode (Platzhalter)
        # --------------------------------------------------

        barcode_x = page_width - 5 * cm

        pdf.rect(
            barcode_x,
            y - 2.8 * cm,
            3 * cm,
            2.2 * cm
        )

        pdf.setFont("Helvetica", 8)

        pdf.drawCentredString(
            barcode_x + 1.5 * cm,
            y - 1.7 * cm,
            "Barcode"
        )