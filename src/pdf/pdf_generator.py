from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from pdf.article_row import ArticleRow


class PDFGenerator:

    def create_pdf(self, region: str, katalog):

        project_path = Path(__file__).resolve().parents[2]

        output_folder = project_path / "kataloge"
        output_folder.mkdir(exist_ok=True)

        pdf_path = output_folder / f"{region.replace(' ', '_')}.pdf"

        pdf = canvas.Canvas(
            str(pdf_path),
            pagesize=A4,
        )

        page_width, page_height = A4

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
            "Seite 1",
        )

        pdf.line(
            2 * cm,
            page_height - 3.6 * cm,
            page_width - 2 * cm,
            page_height - 3.6 * cm,
        )
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

            # Prüfen, ob noch Platz auf der Seite ist
            if y < 5 * cm:

                pdf.showPage()

                self.draw_header(
                    pdf,
                    Path(__file__).resolve().parents[2],
                    page_width,
                    page_height,
                    "",
                )

                y = page_height - 5.2 * cm

            # Herstellerüberschrift

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

            # Alle Artikel des Herstellers

            for artikel in artikel_liste:

                article_row.draw(
                    pdf,
                    artikel,
                    2 * cm,
                    y,
                    page_width,
                )

                y -= 3.6 * cm

                # Seitenumbruch innerhalb eines Herstellers

                if y < 5 * cm:

                    pdf.showPage()

                    self.draw_header(
                        pdf,
                        Path(__file__).resolve().parents[2],
                        page_width,
                        page_height,
                        "",
                    )

                    y = page_height - 5.2 * cm

            # Abstand zum nächsten Hersteller

            y -= 0.8 * cm
            