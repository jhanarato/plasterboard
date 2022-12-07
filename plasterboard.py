from dataclasses import dataclass
from typing import Set, Dict, List
from itertools import chain

@dataclass(frozen=True)
class SheetType:
    brand: str
    material: str
    length: int
    width: int
    thickness: int

    def __str__(self):
        return f"{self.brand} {self.material} {self.thickness}mm {self.width}x{self.length}"

@dataclass
class Surface:
    layers: int
    sheet_type: SheetType
    sheets_per_layer: float

    def quantity(self) -> float:
        return self.sheets_per_layer * self.layers

    def __post_init__(self):
        self.sheets = self.sheets_per_layer * self.layers

    def __str__(self):
        return f"{self.sheet_type} x {self.sheets_per_layer} x {self.layers} layers"

@dataclass
class Room:
    name: str
    locations: Dict[str, Surface]

@dataclass(frozen=True)
class Quantity:
    sheet_type: SheetType
    qty: float

    def __str__(self):
        return f"{self.qty} of {self.sheet_type}"

def sheet_types(room: Room) -> Set[SheetType]:
    types = set()
    for _, surface in room.locations.items():
        types.add(surface.sheet_type)
    return types

def quantity_of_sheet_type(sheet_type: SheetType, room: Room) -> float:
    quantity = 0
    for _, surface in room.locations.items():
        if sheet_type == surface.sheet_type:
            quantity += surface.sheets

    return quantity

def quantities(room: Room) -> List[Quantity]:
    quants = []
    for sheet_type in sheet_types(room):
        quants.append(Quantity(sheet_type, quantity_of_sheet_type(sheet_type, room)))

    return quants

def combine_quantities(quants: List[Quantity]) -> List[Quantity]:
    combined = []
    sheet_types_ = { quant.sheet_type for quant in quants }
    for sheet_type in sheet_types_:
        combined_quantity = sum([quantity_.qty for quantity_ in quants if quantity_.sheet_type == sheet_type])
        combined.append(Quantity(sheet_type, combined_quantity))

    return combined

def total_quantities(rooms: List[Room]) -> List[Quantity]:
    quants = []

    for room in rooms:
        quants.extend(quantities(room))

    return combine_quantities(quants)


plasterboard_3600_1350 = SheetType(
    brand="GTEK",
    material="Fire",
    length=3600,
    width=1350,
    thickness=13
)

plasterboard_3600 = SheetType(
    brand="GTEK",
    material="Fire",
    length=3600,
    width=1200,
    thickness=13
)

cement_2400 = SheetType(
    brand="GTEK",
    material="Duraliner",
    length=2400,
    width=1200,
    thickness=6
)

cement_3600 = SheetType(
    brand="GTEK",
    material="Duraliner",
    length=3600,
    width=1200,
    thickness=6
)

def bedroom(name):
    return Room(
        name=name,
        locations={
            "north wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2.0
            ),
            "south wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2.0
            ),
            "east wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(2/3)
            ),
            "west wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(2/3)
            ),
            "ceiling": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(1/2)
            )
        }
    )

def office():
    return Room(
        name="Office",
        locations={
            "north wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(1/6)
            ),
            "south wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(1/3)
            ),
            "east wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(2/3)
            ),
            "west wall": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2+(2/3),
            ),
            "ceiling": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=3+(1/8)
            )
        }
    )

def bathroom(name, ceiling_layers):
    return Room(
        name=name,
        locations={
            "north wall": Surface(
                layers=1,
                sheet_type=cement_3600,
                sheets_per_layer=1.5
            ),
            "south wall": Surface(
                layers=1,
                sheet_type=cement_3600,
                sheets_per_layer=1.5
            ),
            "east wall": Surface(
                layers=1,
                sheet_type=cement_2400,
                sheets_per_layer=5,
            ),
            "west wall": Surface(
                layers=1,
                sheet_type=cement_2400,
                sheets_per_layer=5,
            ),
            "ceiling": Surface(
                layers=ceiling_layers,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2
            )
        }
    )

def display_room_quantities(room):
    quants = quantities(room)
    for quant in quants:
        print(f"{quant}")

def display_room_surfaces(room):
    for location, surface in room.locations.items():
        print(f"{location}: {surface}")

def display_total_quantities(rooms):
    quants = total_quantities(rooms)
    for quant in quants:
        print(quant)

def main():
    granny_flat = [
        bedroom("Abbot Bedroom"),
        bedroom("No. 2 Bedroom"),
        office(),
        bathroom("Abbot Bathroom", ceiling_layers=2),
        bathroom("No. 2 Bathroom", ceiling_layers=1)
    ]

    for room in granny_flat:
        print(f"***** {room.name} *****")
        print("")
        print("Surfaces")
        print("========")
        display_room_surfaces(room)
        print("")
        print("Quantities")
        print("==========")
        display_room_quantities(room)
        print("")

    print("***** Total Quantities *****")
    print("")
    display_total_quantities(granny_flat)


if __name__ == "__main__":
    main()