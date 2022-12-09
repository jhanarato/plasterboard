from dataclasses import dataclass
from itertools import groupby

from shape import Shape
from sheet import Sheet


@dataclass
class Surface:
    layers: list[Sheet]
    shape: Shape

    def sheet_areas(self) -> dict[Sheet, float]:
        return {
            sheet: len(list(sheet_group)) * self.shape.area()
            for sheet, sheet_group in groupby(self.layers)
        }

    def __str__(self):
        return "\n".join(f"Layer {i+1}: {sheet}" for i, sheet in enumerate(self.layers))
