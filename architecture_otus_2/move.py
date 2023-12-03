from typing import Protocol, Final
from .vector import Vector


class Movable(Protocol):
    def set_location(self, v: Vector) -> None:
        ...

    def get_location(self) -> Vector:
        ...

    def get_velocity(self) -> Vector:
        ...


class Move:
    def __init__(self, movable: Movable) -> None:
        self.movable: Final[Movable] = movable

    def execute(self) -> None:
        new_location: Vector = Vector.plus(
            self.movable.get_location(),
            self.movable.get_velocity(),
        )
        self.movable.set_location(new_location)
