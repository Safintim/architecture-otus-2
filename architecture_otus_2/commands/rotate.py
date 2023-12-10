from typing import Final

from architecture_otus_2.commands.interfaces import Rotable


class Rotate:
    def __init__(self, rotable: Rotable) -> None:
        self.rotable: Final[Rotable] = rotable

    def execute(self) -> None:
        new_direction: int = (
            self.rotable.get_direction() + self.rotable.get_angle_velocity()
        ) % self.rotable.get_directions_number()
        self.rotable.set_direction(new_direction)
