from importer.rewe_importer import ReweImporter


def main():
    importer = ReweImporter()

    regionen = importer.get_regions()

    print("=" * 50)
    print("KatalogFactory")
    print("=" * 50)

    print("\nVerfügbare Regionen")
    print("-" * 30)

    for nummer, region in enumerate(regionen, start=1):
        print(f"{nummer}. {region}")

    print()

    while True:
        try:
            auswahl = int(input("Region auswählen: "))

            if 1 <= auswahl <= len(regionen):
                break

            print("Bitte eine gültige Nummer eingeben.")

        except ValueError:
            print("Bitte eine Zahl eingeben.")

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
            f"{zeile['Artikel']} | "
            f"{zeile['Zusatztext']} | "
            f"{zeile['Mengentext']}"
        )


if __name__ == "__main__":
    main()