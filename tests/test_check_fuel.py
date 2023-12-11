import pytest
from typing import Any
from architecture_otus_2.commands.check_fuel import (
    CheckFuelComamnd,
    CheckFuelCommandException,
)


def test_check_fuel_command_ok(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{"get_fuel.return_value": 10, "get_fuel_burn_speed.return_value": 1}
    )
    check_fuel: CheckFuelComamnd = CheckFuelComamnd(fuel_tank)

    check_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_called_once()


def test_check_fuel_command_bad(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{"get_fuel.return_value": 3, "get_fuel_burn_speed.return_value": 5}
    )
    check_fuel: CheckFuelComamnd = CheckFuelComamnd(fuel_tank)

    with pytest.raises(CheckFuelCommandException):
        check_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_called_once()


def test_check_fuel_command_bad_get_fuel(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{"get_fuel.side_effect": [Exception], "get_fuel_burn_speed.return_value": 5}
    )
    check_fuel: CheckFuelComamnd = CheckFuelComamnd(fuel_tank)

    with pytest.raises(Exception):
        check_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_not_called()


def test_check_fuel_command_bad_get_fuel_burn_speed(mocker: Any) -> None:
    fuel_tank: Any = mocker.Mock(
        **{"get_fuel.return_value": 3, "get_fuel_burn_speed.side_effect": [Exception]}
    )
    check_fuel: CheckFuelComamnd = CheckFuelComamnd(fuel_tank)

    with pytest.raises(Exception):
        check_fuel.execute()

    fuel_tank.get_fuel.assert_called_once()
    fuel_tank.get_fuel_burn_speed.assert_called_once()
