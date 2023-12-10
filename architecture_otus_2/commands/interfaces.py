from typing import Protocol
from architecture_otus_2.vector import Vector


class Movable(Protocol):
    def set_location(self, v: Vector) -> None:
        ...

    def get_location(self) -> Vector:
        ...

    def get_velocity(self) -> Vector:
        ...


class Rotable(Protocol):
    def get_direction(self) -> int:
        ...

    def set_direction(self, direction: int) -> None:
        ...

    def get_angle_velocity(self) -> int:
        ...

    def get_directions_number(self) -> int:
        ...
