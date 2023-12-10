from typing import Final
from architecture_otus_2.vector import Vector
from architecture_otus_2.commands.interfaces import Movable


class Move:
    def __init__(self, movable: Movable) -> None:
        self.movable: Final[Movable] = movable

    def execute(self) -> None:
        new_location: Vector = Vector.plus(
            self.movable.get_location(),
            self.movable.get_velocity(),
        )
        self.movable.set_location(new_location)
