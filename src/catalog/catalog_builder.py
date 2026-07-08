from collections import defaultdict


class CatalogBuilder:

    def build(self, dataframe):
        katalog = defaultdict(list)

        for _, zeile in dataframe.iterrows():
            hersteller = str(zeile["Zusatztext"]).strip()
            katalog[hersteller].append(zeile)

        return dict(sorted(katalog.items()))