from typing import Final
from architecture_otus_2.commands.interfaces import IFuelTank


class CheckFuelCommandException(Exception):
    ...


class CheckFuelComamnd:
    def __init__(self, fuel_tank: IFuelTank) -> None:
        self.fuel_tank: Final[IFuelTank] = fuel_tank

    def execute(self) -> None:
        if self.fuel_tank.get_fuel() < self.fuel_tank.get_fuel_burn_speed():
            raise CheckFuelCommandException()
