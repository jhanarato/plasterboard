from dataclasses import dataclass, field
from typing import Protocol


class Shape(Protocol):
    """Generic shape that defines a way to computes its area"""
    def area(self) -> float:
        ...


@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{self.width}x{self.height}mm^2"
