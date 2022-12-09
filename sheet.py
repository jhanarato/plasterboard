from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from shape import Shape, Rectangle


@dataclass(frozen=True)
class SheetType:
    brand: str
    material: str

    def __str__(self):
        return f"{self.brand}'s {self.material}"


@dataclass(frozen=True)
class Sheet:
    sheet_type: SheetType
    shape: Shape
    price: float

    def area(self):
        return self.shape.area()

    def __str__(self):
        return f"{self.shape} of {self.sheet_type}"


class SheetGroup(Protocol):
    def sheet_areas(self) -> dict[Sheet, float]:
        ...


class SheetSize(Enum):
    S1 = 1200
    S2 = 1350
    S3 = 1800
    S4 = 2400
    S5 = 3600


class SheetTypeCatalog(Enum):
    GTEK = SheetType(brand="GTEK", material="Fire")
    Duraliner = SheetType(brand="Duraliner", material="Fibre cement")


class SheetCatalog(Enum):
    GTEK_51 = Sheet(
        sheet_type=SheetTypeCatalog.GTEK.value,
        shape=Rectangle(
            width=SheetSize.S5.value,
            height=SheetSize.S1.value
        ),
        price=120
    )
    GTEK_52 = Sheet(
        sheet_type=SheetTypeCatalog.GTEK.value,
        shape=Rectangle(
            width=SheetSize.S5.value,
            height=SheetSize.S2.value
        ),
        price=150
    )
    Duraliner_31 = Sheet(
        sheet_type=SheetTypeCatalog.Duraliner.value,
        shape=Rectangle(
            width=SheetSize.S3.value,
            height=SheetSize.S1.value
        ),
        price=200
    )
    Duraliner_41 = Sheet(
        sheet_type=SheetTypeCatalog.Duraliner.value,
        shape=Rectangle(
            width=SheetSize.S4.value,
            height=SheetSize.S1.value
        ),
        price=250
    )
    Duraliner_51 = Sheet(
        sheet_type=SheetTypeCatalog.Duraliner.value,
        shape=Rectangle(
            width=SheetSize.S5.value,
            height=SheetSize.S1.value
        ),
        price=300
    )
    Duraliner_52 = Sheet(
        sheet_type=SheetTypeCatalog.Duraliner.value,
        shape=Rectangle(
            width=SheetSize.S5.value,
            height=SheetSize.S2.value
        ),
        price=350
    )
