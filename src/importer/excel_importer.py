from pathlib import Path
import pandas as pd


class ExcelImporter:

    def __init__(self):
        self.project_path = Path(__file__).resolve().parents[2]
        self.excel_path = self.project_path / "excel"

    def find_excel_file(self):
        files = list(self.excel_path.glob("*.xlsx"))

        if not files:
            raise FileNotFoundError(
                "Keine Excel-Datei im Ordner 'excel' gefunden."
            )

        return files[0]

    def load_excel(self):
        excel_file = self.find_excel_file()
        dataframe = pd.read_excel(excel_file)
        return excel_file, dataframe

    def get_regions(self):
        _, dataframe = self.load_excel()

        regions = []

        for column in dataframe.columns:
            if isinstance(column, str) and column.startswith("REWE"):
                regions.append(column)

        return regions