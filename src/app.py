from importer.rewe_importer import ReweImporter
from catalog.catalog_builder import CatalogBuilder
from pdf.pdf_generator import PDFGenerator


def main():

    print("=" * 60)
    print("KatalogFactory")
    print("=" * 60)

    importer = ReweImporter()
    builder = CatalogBuilder()
    pdf_generator = PDFGenerator()

    # Regionen ermitteln
    regionen = importer.get_regions()

    print("\nVerfügbare Regionen")
    print("-" * 30)

    for nummer, region in enumerate(regionen, start=1):
        print(f"{nummer}. {region}")

    # Region auswählen
    while True:

        try:
            auswahl = int(input("\nRegion auswählen: "))

            if 1 <= auswahl <= len(regionen):
                break

            print("Ungültige Auswahl.")

        except ValueError:
            print("Bitte eine Zahl eingeben.")

    region = regionen[auswahl - 1]

    print(f"\nRegion: {region}")

    # Artikel laden
    dataframe = importer.get_articles_for_region(region)

    print(f"Gelistete Artikel: {len(dataframe)}")

    # Katalog erzeugen
    katalog = builder.build(dataframe)

    print("\nPDF wird erstellt ...")

    pdf_datei = pdf_generator.create_pdf(region)

    print("\nFertig.")

    print(f"\nPDF gespeichert unter:\n{pdf_datei}")


if __name__ == "__main__":
    main()