from typing import Protocol
from architecture_otus_2.vector import Vector


class ICommand(Protocol):
    def execute(self) -> None:
        ...


class Movable(Protocol):
    def set_location(self, v: Vector) -> None:
        ...

    def get_location(self) -> Vector:
        ...

    def get_velocity(self) -> Vector:
        ...

    def set_velocity(self, v: Vector) -> Vector:
        ...

    def get_velocity_rotate_factor(self) -> Vector:
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


class IFuelTank(Protocol):
    def get_fuel(self) -> int:
        ...

    def get_fuel_burn_speed(self) -> int:
        ...

    def set_fuel(self, fuel: int) -> None:
        ...
