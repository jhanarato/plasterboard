import pytest
from plasterboard import Surface, Room, Quantity
from plasterboard import quantities, sheet_types, quantity_of_sheet_type, combine_quantities, total_quantities
from plasterboard import plasterboard_3600_1350, plasterboard_3600_1200, cement_2400_1200, cement_3600_1350

@pytest.fixture
def room():
    plaster_wall = Surface(
        layers=2,
        sheet_type=plasterboard_3600_1350,
        sheets_per_layer=2.5
    )

    cement_wall = Surface(
        layers=1,
        sheet_type=cement_2400_1200,
        sheets_per_layer=1
    )

    room = Room(
        name="Two Wall Room",
        locations={
            "North": plaster_wall,
            "South": cement_wall
        }
    )

    return room

def test_one_location_one_layer():
    surface = Surface(layers=1,
                      sheet_type=plasterboard_3600_1350,
                      sheets_per_layer=2.5)

    assert surface.sheets == 2.5

def test_one_location_two_layers():
    surface = Surface(layers=2,
                      sheet_type=cement_2400_1200,
                      sheets_per_layer=2.5)

    assert surface.sheets == 5.0

def test_add_surface_to_room():
    surface = Surface(
        layers=2,
        sheet_type=cement_2400_1200,
        sheets_per_layer=2.5
    )

    bedroom = Room(
        name="Bedroom",
        locations={"north": surface}
    )

    assert bedroom.locations["north"] == surface

def test_sheet_types(room):
    types = sheet_types(room)
    assert plasterboard_3600_1350 in types
    assert cement_2400_1200 in types

def test_quantity_of_sheet_type(room):
    assert quantity_of_sheet_type(plasterboard_3600_1350, room) == 5
    assert quantity_of_sheet_type(cement_2400_1200, room) == 1

def test_quantity_two_of_same_type():
    plaster_wall_one = Surface(
        layers=1,
        sheet_type=plasterboard_3600_1350,
        sheets_per_layer=3.0
    )

    plaster_wall_two = Surface(
        layers=1,
        sheet_type=plasterboard_3600_1350,
        sheets_per_layer=2.5
    )

    two_wall_same_room = Room(
        name="Bedroom",
        locations={"north": plaster_wall_one, "south": plaster_wall_two }
    )

    assert quantity_of_sheet_type(plasterboard_3600_1350, two_wall_same_room) == 5.5

def test_quantity_in_list(room):
    sheets = quantities(room)
    assert Quantity(plasterboard_3600_1350, 5.0) in sheets
    assert Quantity(cement_2400_1200, 1.0) in sheets

def test_combine_quantities():
    quants = [
        Quantity(plasterboard_3600_1200, 1.0),
        Quantity(plasterboard_3600_1350, 2.0),
        Quantity(cement_2400_1200, 3.0),
        Quantity(cement_3600_1350, 4.0),
        Quantity(plasterboard_3600_1200, 10.0),
        Quantity(plasterboard_3600_1350, 20.0),
        Quantity(cement_2400_1200, 30.0),
        Quantity(cement_3600_1350, 40.0)
    ]

    combined = combine_quantities(quants)

    assert Quantity(plasterboard_3600_1200, 11.0) in combined
    assert Quantity(plasterboard_3600_1350, 22.0) in combined
    assert Quantity(cement_2400_1200, 33.0) in combined
    assert Quantity(cement_3600_1350, 44.0) in combined

def test_total_quantities():
    room_one = Room(
        name="room_one",
        locations={
            "wall one": Surface(
                layers=2,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=3.5
            ),
            "wall two": Surface(
                layers=1,
                sheet_type=cement_2400_1200,
                sheets_per_layer=4.0
            )
        }
    )

    room_two = Room(
        name="room_two",
        locations={
            "wall one": Surface(
                layers=1,
                sheet_type=plasterboard_3600_1350,
                sheets_per_layer=2.0
            ),
            "wall two": Surface(
                layers=2,
                sheet_type=cement_2400_1200,
                sheets_per_layer=2.0
            )
        }
    )

    quants = total_quantities([room_one, room_two])

    assert Quantity(plasterboard_3600_1350, 9.0) in quants
    assert Quantity(cement_2400_1200, 8.0) in quants