from typing import Final, Protocol


class Rotable(Protocol):
    def get_direction(self) -> int:
        ...

    def set_direction(self, direction: int) -> None:
        ...

    def get_angle_velocity(self) -> int:
        ...

    def get_directions_number(self) -> int:
        ...


class Rotate:
    def __init__(self, rotable: Rotable) -> None:
        self.rotable: Final[Rotable] = rotable

    def execute(self) -> None:
        new_direction: int = (
            self.rotable.get_direction() + self.rotable.get_angle_velocity()
        ) % self.rotable.get_directions_number()
        self.rotable.set_direction(new_direction)
