from dataclasses import dataclass, field
from itertools import groupby

from sheet import Sheet
from surface import Surface


@dataclass
class Room:
    """A collection of surfaces, also a group of sheets"""
    surfaces: dict[str, Surface] = field(default_factory=dict)

    def sheet_areas(self) -> dict[Sheet, float]:
        sheet_areas = [
            sheet_area
            for surface in self.surfaces.values()
            for sheet_area in surface.sheet_areas().items()
        ]

        return {
            sheet: sum(sheet_area[1] for sheet_area in sheet_group)
            for sheet, sheet_group in groupby(sheet_areas, lambda sheet_area: sheet_area[0])
        }

    def __str__ (self):
        return "\n".join(f"{name}\n{surface}\n---" for name, surface in self.surfaces.items())