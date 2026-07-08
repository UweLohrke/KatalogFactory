from collections import defaultdict


class CatalogBuilder:

    def group_by_manufacturer(self, articles):
        katalog = defaultdict(list)

        for article in articles:
            katalog[article.hersteller].append(article)

        for hersteller in katalog:
            katalog[hersteller].sort(
                key=lambda artikel: artikel.bezeichnung
            )

        return dict(sorted(katalog.items()))