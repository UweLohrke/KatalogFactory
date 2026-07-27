"""
KatalogFactory by U.L.

Datei:
pdf_generator.py

Version:
0.9.1

Beschreibung:
Erzeugt den PDF-Katalog.
Unterstützt frei wählbare Ausgabeordner.
"""

from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from pdf.article_row import ArticleRow


class PDFGenerator:

    def __init__(self):

        self.page_number = 1
        self.region = ""

    # --------------------------------------------------
    # PDF erzeugen
    # --------------------------------------------------

    def create_pdf(
        self,
        region,
        katalog,
        output_folder=None,
    ):

        project_path = self.get_project_path()

        if output_folder is None:

            output_folder = project_path / "kataloge"

        output_folder = Path(output_folder)

        output_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        pdf_path = self.create_output_path(
            output_folder,
            region,
        )

        pdf = canvas.Canvas(
            str(pdf_path),
            pagesize=A4,
        )

        page_width, page_height = A4

        self.page_number = 1
        self.region = region

        self.draw_header(
            pdf,
            project_path,
            page_width,
            page_height,
            region,
        )

        self.draw_catalog(
            pdf,
            katalog,
            page_width,
            page_height,
        )

        pdf.save()

        return pdf_path

    # --------------------------------------------------
    # Projektpfad
    # --------------------------------------------------

    def get_project_path(self):

        return Path(__file__).resolve().parents[2]

    # --------------------------------------------------
    # Ausgabedatei
    # --------------------------------------------------

    def create_output_path(
        self,
        output_folder,
        region,
    ):

        filename = f"{region.replace(' ', '_')}.pdf"

        return Path(output_folder) / filename

    # --------------------------------------------------
    # Kopfbereich
    # --------------------------------------------------

    def draw_header(
        self,
        pdf,
        project_path,
        page_width,
        page_height,
        region,
    ):

        logo = project_path / "assets" / "logo.png"

        if logo.exists():

            pdf.drawImage(
                str(logo),
                2 * cm,
                page_height - 3.3 * cm,
                width=2.5 * cm,
                height=2.5 * cm,
                preserveAspectRatio=True,
                mask="auto",
            )

        pdf.setFont(
            "Helvetica-Bold",
            18,
        )

        pdf.drawString(
            5 * cm,
            page_height - 2 * cm,
            "Rhein-Main-Bio GmbH",
        )

        pdf.setFont(
            "Helvetica",
            12,
        )

        pdf.drawString(
            5 * cm,
            page_height - 2.8 * cm,
            region,
        )

        pdf.setFont(
            "Helvetica",
            10,
        )

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2 * cm,
            datetime.now().strftime("%d.%m.%Y"),
        )

        pdf.drawRightString(
            page_width - 2 * cm,
            page_height - 2.6 * cm,
            f"Seite {self.page_number}",
        )

        pdf.line(
            2 * cm,
            page_height - 3.6 * cm,
            page_width - 2 * cm,
            page_height - 3.6 * cm,
        )

    # --------------------------------------------------
    # Katalog
    # --------------------------------------------------

    def draw_catalog(
        self,
        pdf,
        katalog,
        page_width,
        page_height,
    ):

        article_row = ArticleRow()

        y = page_height - 5.2 * cm

        for hersteller, artikel_liste in katalog.items():
                        # Seitenwechsel vor Hersteller

            if y < 5 * cm:

                pdf.showPage()

                self.page_number += 1

                self.draw_header(
                    pdf,
                    self.get_project_path(),
                    page_width,
                    page_height,
                    self.region,
                )

                y = page_height - 5.2 * cm

            # ------------------------------------------
            # Hersteller
            # ------------------------------------------

            pdf.setFont(
                "Helvetica-Bold",
                16,
            )

            pdf.drawString(
                2 * cm,
                y,
                hersteller,
            )

            pdf.line(
                2 * cm,
                y - 0.2 * cm,
                page_width - 2 * cm,
                y - 0.2 * cm,
            )

            y -= 1 * cm

            # ------------------------------------------
            # Artikel
            # ------------------------------------------

            for artikel in artikel_liste:

                article_row.draw(
                    pdf,
                    artikel,
                    2 * cm,
                    y,
                    page_width,
                )

                y -= article_row.ROW_HEIGHT

                # Seitenwechsel innerhalb eines Herstellers

                if y < 5 * cm:

                    pdf.showPage()

                    self.page_number += 1

                    self.draw_header(
                        pdf,
                        self.get_project_path(),
                        page_width,
                        page_height,
                        self.region,
                    )

                    y = page_height - 5.2 * cm

            # Abstand zum nächsten Hersteller

            y -= 0.8 * cm