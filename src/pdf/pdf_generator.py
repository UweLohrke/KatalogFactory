from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


class PDFGenerator:

    def create_pdf(self, region: str):

        # Projektordner
        project_path = Path(__file__).resolve().parents[2]

        # Ausgabeordner erzeugen
        output_folder = project_path / "kataloge"
        output_folder.mkdir(exist_ok=True)

        pdf_path = output_folder / f"{region.replace(' ', '_')}.pdf"

        # PDF erzeugen
        pdf = canvas.Canvas(str(pdf_path), pagesize=A4)

        page_width, page_height = A4

        # =====================================================
        # LOGO
        # =====================================================

        logo_path = project_path / "assets" / "logo.png"

        if logo_path.exists():
            try:
                pdf.drawImage(
                    str(logo_path),
                    x=2 * cm,
                    y=page_height - 3.3 * cm,
                    width=2.5 * cm,
                    height=2.5 * cm,
                    preserveAspectRatio=True,
                    mask="auto"
                )
            except Exception:
                pass

        # =====================================================
        # Firmenname
        # =====================================================

        pdf.setFont("Helvetica-Bold", 18)

        pdf.drawString(
            5.0 * cm,
            page_height - 2.0 * cm,
            "Rhein-Main-Bio GmbH"
        )

        # =====================================================
        # Region
        # =====================================================

        pdf.setFont("Helvetica", 12)

        pdf.drawString(
            5.0 * cm,
            page_height - 2.8 * cm,
            region
        )

        # =====================================================
        # Datum
        # =====================================================

        pdf.setFont("Helvetica", 10)

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2.0 * cm,
            datetime.now().strftime("%d.%m.%Y")
        )

        # =====================================================
        # Seitenzahl
        # =====================================================

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2.6 * cm,
            "Seite 1"
        )

        # =====================================================
        # Trennlinie
        # =====================================================

        pdf.line(
            2 * cm,
            page_height - 3.6 * cm,
            page_width - 2 * cm,
            page_height - 3.6 * cm
        )

        # =====================================================
        # Platzhalter
        # =====================================================

        pdf.setFont("Helvetica-Bold", 16)

        pdf.drawString(
            2 * cm,
            page_height - 5 * cm,
            "HERSTELLER"
        )

        pdf.line(
            2 * cm,
            page_height - 5.3 * cm,
            page_width - 2 * cm,
            page_height - 5.3 * cm
        )

        pdf.save()

        return pdf_path