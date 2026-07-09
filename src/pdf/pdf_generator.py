from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


class PDFGenerator:

    def create_pdf(self, region: str):

        project_path = Path(__file__).resolve().parents[2]

        output_folder = project_path / "kataloge"
        output_folder.mkdir(exist_ok=True)

        pdf_path = output_folder / f"{region.replace(' ', '_')}.pdf"

        pdf = canvas.Canvas(str(pdf_path), pagesize=A4)

        page_width, page_height = A4

        self.draw_header(pdf, project_path, page_width, page_height, region)
        self.draw_sample_article(pdf, page_width, page_height)

        pdf.save()

        return pdf_path

    # ---------------------------------------------------------
    # Kopf
    # ---------------------------------------------------------

    def draw_header(self, pdf, project_path, page_width, page_height, region):

        logo = project_path / "assets" / "logo.png"

        if logo.exists():
            try:
                pdf.drawImage(
                    str(logo),
                    2 * cm,
                    page_height - 3.3 * cm,
                    width=2.5 * cm,
                    height=2.5 * cm,
                    preserveAspectRatio=True,
                    mask="auto",
                )
            except Exception:
                pass

        pdf.setFont("Helvetica-Bold", 18)

        pdf.drawString(
            5 * cm,
            page_height - 2 * cm,
            "Rhein-Main-Bio GmbH",
        )

        pdf.setFont("Helvetica", 12)

        pdf.drawString(
            5 * cm,
            page_height - 2.8 * cm,
            region,
        )

        pdf.setFont("Helvetica", 10)

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2.0 * cm,
            datetime.now().strftime("%d.%m.%Y"),
        )

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2.6 * cm,
            "Seite 1",
        )

        pdf.line(
            2 * cm,
            page_height - 3.6 * cm,
            page_width - 2 * cm,
            page_height - 3.6 * cm,
        )

    # ---------------------------------------------------------
    # Musterartikel
    # ---------------------------------------------------------

    def draw_sample_article(self, pdf, page_width, page_height):

        y = page_height - 5.2 * cm

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(2 * cm, y, "BAUCK")

        pdf.line(
            2 * cm,
            y - 0.2 * cm,
            page_width - 2 * cm,
            y - 0.2 * cm,
        )

        row_top = y - 1 * cm

        # Bild

        pdf.rect(
            2 * cm,
            row_top - 3 * cm,
            3 * cm,
            3 * cm,
        )

        pdf.setFont("Helvetica", 9)

        pdf.drawCentredString(
            3.5 * cm,
            row_top - 1.5 * cm,
            "Produktbild",
        )

        # Artikel

        pdf.setFont("Helvetica-Bold", 13)

        pdf.drawString(
            5.5 * cm,
            row_top - 0.4 * cm,
            "100% DINKEL CRUNCHY",
        )

        pdf.setFont("Helvetica", 11)

        pdf.drawString(
            5.5 * cm,
            row_top - 1.1 * cm,
            "BOHLSENER MÜHLE",
        )

        pdf.drawString(
            5.5 * cm,
            row_top - 1.8 * cm,
            "400 G PK",
        )

        # Preise

        pdf.setFont("Helvetica-Bold", 11)

        pdf.drawRightString(
            page_width - 6 * cm,
            row_top - 0.4 * cm,
            "LP: 3,49 €",
        )

        pdf.drawRightString(
            page_width - 6 * cm,
            row_top - 1.2 * cm,
            "UVP: 4,29 €",
        )

        # Barcode

        pdf.rect(
            page_width - 5 * cm,
            row_top - 2.6 * cm,
            3 * cm,
            2.2 * cm,
        )

        pdf.setFont("Helvetica", 8)

        pdf.drawCentredString(
            page_width - 3.5 * cm,
            row_top - 1.5 * cm,
            "Barcode",
        )

        pdf.drawCentredString(
            page_width - 3.5 * cm,
            row_top - 2.9 * cm,
            "4012345678901",
        )