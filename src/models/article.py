from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Article:
    nan: str

    eh_gtin: str
    gebinde_gtin: str

    bezeichnung: str
    hersteller: str
    mengentext: str

    listenpreis: Decimal
    uvp: Decimal

    status: str

    regionen: list[str] = field(default_factory=list)

    def __str__(self):
        return (
            f"{self.hersteller} | "
            f"{self.bezeichnung} | "
            f"{self.mengentext}"
        )