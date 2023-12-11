from typing import Final
from architecture_otus_2.commands.interfaces import Movable
from architecture_otus_2.vector import Vector


class ChangeVelocityCommand:
    def __init__(self, movable: Movable) -> None:
        self.movable: Final[Movable] = movable

    def execute(self) -> None:
        current_velocity: Vector = self.movable.get_velocity()
        if current_velocity == Vector(0, 0):
            return None

        self.movable.set_velocity(
            Vector.minus(current_velocity, self.movable.get_velocity_rotate_factor())
        )
