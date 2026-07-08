from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


class PDFGenerator:

    def create_pdf(self, region: str):

        # Projektpfad ermitteln
        project_path = Path(__file__).resolve().parents[2]

        # Ausgabeordner
        output_folder = project_path / "kataloge"
        output_folder.mkdir(exist_ok=True)

        # Dateiname
        filename = region.replace(" ", "_") + ".pdf"
        pdf_path = output_folder / filename

        # PDF erzeugen
        pdf = canvas.Canvas(str(pdf_path), pagesize=A4)

        page_width, page_height = A4

        # -----------------------------
        # Kopfbereich
        # -----------------------------

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(
            2 * cm,
            page_height - 2 * cm,
            "Rhein-Main-Bio GmbH"
        )

        pdf.setFont("Helvetica", 11)

        pdf.drawString(
            2 * cm,
            page_height - 2.8 * cm,
            region
        )

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2.8 * cm,
            datetime.now().strftime("%d.%m.%Y")
        )

        # Trennlinie

        pdf.line(
            2 * cm,
            page_height - 3.2 * cm,
            page_width - 2 * cm,
            page_height - 3.2 * cm
        )

        pdf.save()

        return pdf_path