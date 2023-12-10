import pytest
from typing import Any
from architecture_otus_2.commands.burn_fuel import BurnFuelCommand


def test_burn_fuel_command_ok(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{
            "get_fuel.return_value": 10,
            "get_fuel_burn_speed.return_value": 5,
            "set_fuel.return_value": None,
        }
    )
    burn_fuel: BurnFuelCommand = BurnFuelCommand(fuel_tank)

    burn_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_called_once()
    fuel_tank.set_fuel.assert_called_once_with(5)


def test_burn_fuel_command_bad_get_fuel(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{
            "get_fuel.side_effect": [Exception],
            "get_fuel_burn_speed.return_value": 5,
            "set_fuel.return_value": None,
        }
    )
    burn_fuel: BurnFuelCommand = BurnFuelCommand(fuel_tank)

    with pytest.raises(Exception):
        burn_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_not_called()
    fuel_tank.set_fuel.assert_not_called()


def test_burn_fuel_command_bad_get_fuel_burn_speed(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{
            "get_fuel.return_value": 10,
            "get_fuel_burn_speed.side_effect": [Exception],
            "set_fuel.return_value": None,
        }
    )
    burn_fuel: BurnFuelCommand = BurnFuelCommand(fuel_tank)

    with pytest.raises(Exception):
        burn_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_called_once()
    fuel_tank.set_fuel.assert_not_called()


def test_burn_fuel_command_bad_set_fuel(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{
            "get_fuel.return_value": 10,
            "get_fuel_burn_speed.return_value": 5,
            "set_fuel.return_value": [Exception],
        }
    )
    burn_fuel: BurnFuelCommand = BurnFuelCommand(fuel_tank)

    burn_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_called_once()
    fuel_tank.set_fuel.assert_called_once_with(5)
