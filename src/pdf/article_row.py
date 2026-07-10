"""
KatalogFactory

Datei:
article_row.py

Version:
0.5.3

Beschreibung:
Zeichnet eine kompakte Artikelzeile für den PDF-Katalog.
Die Version 0.5.3 reduziert den Platzbedarf deutlich und
bereitet die spätere Einbindung echter Produktbilder vor.
"""

from reportlab.lib.units import cm


class ArticleRow:

    # Höhe einer kompletten Artikelzeile
    ROW_HEIGHT = 2.7 * cm

    def draw(self, pdf, artikel, x, y, page_width):

        # --------------------------------------------------
        # Produktbild (Platzhalter)
        # --------------------------------------------------

        image_size = 2.2 * cm

        pdf.rect(
            x,
            y - image_size,
            image_size,
            image_size,
        )

        pdf.setFont("Helvetica", 7)

        pdf.drawCentredString(
            x + image_size / 2,
            y - image_size / 2,
            "Bild",
        )

        # --------------------------------------------------
        # Artikelinformationen
        # --------------------------------------------------

        text_x = x + image_size + 0.4 * cm

        pdf.setFont(
            "Helvetica-Bold",
            11,
        )

        pdf.drawString(
            text_x,
            y - 0.3 * cm,
            str(artikel["Artikel"]),
        )

        pdf.setFont(
            "Helvetica",
            9,
        )

        pdf.drawString(
            text_x,
            y - 0.9 * cm,
            str(artikel["Mengentext"]),
        )

        pdf.drawString(
            text_x,
            y - 1.5 * cm,
            f"EH GTIN: {artikel['EH GTIN']}",
        )

        # --------------------------------------------------
        # Preise
        # --------------------------------------------------

        price_x = page_width - 5.8 * cm

        pdf.setFont(
            "Helvetica-Bold",
            9,
        )

        pdf.drawRightString(
            price_x,
            y - 0.3 * cm,
            f"LP: {artikel['Listenpreis (EUR)']:.2f} €",
        )

        pdf.drawRightString(
            price_x,
            y - 0.9 * cm,
            f"UVP: {artikel['UVP']:.2f} €",
        )

        # --------------------------------------------------
        # Barcode (Platzhalter)
        # --------------------------------------------------

        barcode_width = 2.4 * cm
        barcode_height = 1.8 * cm

        barcode_x = page_width - 4.6 * cm

        pdf.rect(
            barcode_x,
            y - barcode_height,
            barcode_width,
            barcode_height,
        )

        pdf.setFont(
            "Helvetica",
            7,
        )

        pdf.drawCentredString(
            barcode_x + barcode_width / 2,
            y - barcode_height / 2,
            "Barcode",
        )