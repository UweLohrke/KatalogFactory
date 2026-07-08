from importer.excel_importer import ExcelImporter


def main():

    print("=" * 50)
    print("KatalogFactory")
    print("=" * 50)

    importer = ExcelImporter()

    excel_file, dataframe = importer.load_excel()

    print()
    print("Excel-Datei:")
    print(excel_file.name)

    print()
    print("Artikel:", len(dataframe))

    print()
    print("Gefundene Regionen")
    print("-" * 30)

    for nummer, region in enumerate(importer.get_regions(), start=1):
        print(f"{nummer}. {region}")


if __name__ == "__main__":
    main()