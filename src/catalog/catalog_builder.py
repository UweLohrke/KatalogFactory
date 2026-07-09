"""
KatalogFactory

Datei:
catalog_builder.py

Version:
0.5.0

Beschreibung:
Erzeugt einen nach Herstellern gruppierten Katalog.
Die Artikel bleiben zunächst als Pandas-Zeilen erhalten.
Die Umstellung auf Article-Objekte erfolgt in einer späteren Version.
"""

from collections import defaultdict


class CatalogBuilder:

    def build(self, dataframe):
        """
        Erstellt einen Katalog nach Herstellern.

        Rückgabe:
        {
            "BAUCK": [Artikel1, Artikel2, ...],
            "BIOVEGAN": [Artikel1, Artikel2, ...]
        }
        """

        katalog = defaultdict(list)

        for _, zeile in dataframe.iterrows():

            hersteller = str(zeile["Zusatztext"]).strip()

            if not hersteller:
                hersteller = "Ohne Hersteller"

            katalog[hersteller].append(zeile)

        return dict(sorted(katalog.items()))