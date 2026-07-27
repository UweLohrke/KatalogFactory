"""
Test für den CatalogService

Version:
0.9.1
"""

import sys
from pathlib import Path

project_path = Path(__file__).resolve().parent
src_path = project_path / "src"

sys.path.insert(0, str(src_path))

from services.catalog_service import CatalogService


def main():

    service = CatalogService()

    excel_folder = project_path / "excel"

    excel_files = list(excel_folder.glob("*.xlsx"))

    if not excel_files:

        print("Keine Excel-Datei gefunden.")
        return

    excel_file = excel_files[0]

    regionen = service.get_regions()

    if not regionen:

        print("Keine Regionen gefunden.")
        return

    region = regionen[0]

    output_folder = project_path / "kataloge"

    pdf = service.create_catalog(
        excel_file=excel_file,
        region=region,
        output_folder=output_folder,
    )

    print()
    print("PDF erstellt:")
    print(pdf)


if __name__ == "__main__":
    main()