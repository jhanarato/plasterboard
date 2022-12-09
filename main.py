import math

from house import House
from room import Room
from shape import Rectangle
from sheet import SheetGroup, SheetCatalog
from surface import Surface


def get_bill_of_material(group: SheetGroup):
    return {
        sheet: math.ceil(area / sheet.area())
        for sheet, area in group.sheet_areas().items()
    }


def main():
    """Building houses can be templated"""

    granny_flat = House(
        rooms={
            "Abbot Bedroom": Room(
                surfaces={
                    "west wall": Surface(
                        layers=[
                            SheetCatalog.GTEK_51.value
                        ],
                        shape=Rectangle(2000, 2500)
                    )
                }),
            "No. 2 Bedroom": Room(
                surfaces={
                    "south wall": Surface(
                        layers=[
                            SheetCatalog.GTEK_52.value
                        ],
                        shape=Rectangle(2500, 2500)
                    )
                }),
            "Office": Room(
                surfaces={
                    "north wall": Surface(
                        layers=[
                            SheetCatalog.GTEK_52.value
                        ],
                        shape=Rectangle(2000, 2000)
                    )
                }),
            "Abbot Bathroom": Room(
                surfaces={
                    "north wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "east wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "south wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "west wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "ceiling": Surface(
                        layers=[
                            SheetCatalog.GTEK_51.value,
                            SheetCatalog.GTEK_51.value
                        ],
                        shape=Rectangle(3000, 4000)
                    )
                }),
            "No. 2 Bathroom": Room(
                surfaces={
                    "north wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "east wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "south wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "west wall": Surface(
                        layers=[
                            SheetCatalog.Duraliner_31.value
                        ],
                        shape=Rectangle(3000, 2500)
                    ),
                    "ceiling": Surface(
                        layers=[
                            SheetCatalog.GTEK_51.value
                        ],
                        shape=Rectangle(3000, 4000)
                    )
                }),
        }
    )

    bom = get_bill_of_material(granny_flat)

    print(f"{'Sheet':40}\t{'No.':6}{'Cost':8}")
    print("\n".join(f"{str(sheet):40}{num:6}{sheet.price * num:8}$" for sheet, num in bom.items()))

    # print(str(granny_flat))


if __name__ == "__main__":
    main()