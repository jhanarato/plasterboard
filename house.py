from dataclasses import dataclass, field
from itertools import groupby

from room import Room


@dataclass
class House:
    """A collection of rooms, also a group of sheets"""
    rooms: dict[str, Room] = field(default_factory=dict)

    def sheet_areas(self):
        sheet_areas = [
            sheet_area
            for room in self.rooms.values()
            for sheet_area in room.sheet_areas().items()
        ]

        return {
            sheet: sum(sheet_area[1] for sheet_area in sheet_group)
            for sheet, sheet_group in groupby(sheet_areas, lambda sheet_area: sheet_area[0])
        }

    def __str__ (self):
        return "\n".join(f"*** {name} ***\n{str(room)}\n" for name, room in self.rooms.items())



