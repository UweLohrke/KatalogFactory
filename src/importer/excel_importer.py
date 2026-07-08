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