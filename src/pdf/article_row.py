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

        frame_size = 2.4 * cm
        padding = 0.15 * cm
        image_size = frame_size - (2 * padding)

        # ----------------------------------------------
        # Bildrahmen
        # ----------------------------------------------

        pdf.setStrokeColorRGB(0.75, 0.75, 0.75)
        pdf.setLineWidth(0.5)

        pdf.rect(
            x,
            y - frame_size,
            frame_size,
            frame_size,
            fill=0,
        )

        if image_path is not None:

            pdf.drawImage(
                str(image_path),
                x + padding,
                y - frame_size + padding,
                width=image_size,
                height=image_size,
                preserveAspectRatio=True,
                anchor="c",
                mask="auto",
            )

        else:

            pdf.setFont("Helvetica", 7)

            pdf.drawCentredString(
                x + frame_size / 2,
                y - frame_size / 2,
                "Bild",
            )

        pdf.setStrokeColorRGB(0, 0, 0)

        # --------------------------------------------------
        # Artikelinformationen
        # --------------------------------------------------

        text_x = x + frame_size + 0.4 * cm

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