from importer.excel_importer import ExcelImporter


def main():

    importer = ExcelImporter()

    regionen = importer.get_regions()

    print("=" * 50)
    print("KatalogFactory")
    print("=" * 50)

    print()
    print("Verfügbare Regionen")
    print("-" * 30)

    for nummer, region in enumerate(regionen, start=1):
        print(f"{nummer}. {region}")

    print()

    auswahl = int(input("Region auswählen: "))

    region = regionen[auswahl - 1]

    artikel = importer.get_articles_for_region(region)

    print()
    print("=" * 50)
    print(region)
    print("=" * 50)

    print(f"Gelistete Artikel: {len(artikel)}")

    print()
    print("Erste 10 Artikel")
    print("-" * 50)

    for _, zeile in artikel.head(10).iterrows():
        print(
            f"{zeile['Artikel']} | {zeile['Zusatztext']} | {zeile['Mengentext']}"
        )


if __name__ == "__main__":
    main()