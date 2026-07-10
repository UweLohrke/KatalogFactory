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
from pdf.image_loader import ImageLoader
from pdf.barcode_generator import BarcodeGenerator
class ArticleRow:

    # Höhe einer kompletten Artikelzeile
    ROW_HEIGHT = 2.7 * cm

    def draw(self, pdf, artikel, x, y, page_width):

        # --------------------------------------------------
        # Produktbild (Platzhalter)
        # --------------------------------------------------
        image_loader = ImageLoader()
        image_path = image_loader.get_image(artikel)
        image_size = 2.2 * cm

        if image_path is not None:

            pdf.drawImage(
                str(image_path),
                x,
                y - image_size,
                width=image_size,
                height=image_size,
                preserveAspectRatio=True,
                mask="auto",
            )

        else:

            pdf.rect(
                x,
                y - image_size,
                width=image_size,
                height=image_size,
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
        # Barcode
        # --------------------------------------------------

        barcode = BarcodeGenerator()

        barcode_x = page_width - 4.6 * cm

        barcode.draw(
            pdf,
            artikel["EH GTIN"],
            barcode_x,
            y - 1.9 * cm,
        )