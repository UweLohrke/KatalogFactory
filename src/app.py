from importer.excel_importer import ExcelImporter


def main():
    print("=" * 50)
    print("KatalogFactory")
    print("=" * 50)

    importer = ExcelImporter()

    excel_file = importer.find_excel_file()

    print(f"Excel-Datei gefunden:\n{excel_file}")


if __name__ == "__main__":
    main()