"""
KatalogFactory by U.L.

Datei:
base_provider.py

Version:
1.2.0

Beschreibung:
Basisklasse für alle Bildquellen.

Jeder Provider muss diese Schnittstelle
implementieren.
"""

from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):

    @property
    @abstractmethod
    def name(self):
        """
        Name des Providers.
        """

    @abstractmethod
    def get_image_url(
        self,
        gtin,
        artikel=None,
    ):
        """
        Liefert die URL des Produktbildes.

        Rückgabe:
            str | None
        """