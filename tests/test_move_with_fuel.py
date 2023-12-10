import pytest
from typing import Any
from architecture_otus_2.commands.macro_command import MacroCommand


def test_move_with_fuel_command_ok(mocker: Any) -> None:
    check_fuel_command: Any = mocker.Mock()
    move_command: Any = mocker.Mock()
    burn_fuel_command: Any = mocker.Mock()

    macro_command: MacroCommand = MacroCommand(
        [check_fuel_command, move_command, burn_fuel_command]
    )

    macro_command.execute()

    check_fuel_command.execute.assert_called_once()
    move_command.execute.assert_called_once()
    burn_fuel_command.execute.assert_called_once()


def test_move_with_fuel_command_bad_check_fuel_command(mocker: Any) -> None:
    check_fuel_command: Any = mocker.Mock(**{"execute.side_effect": [Exception]})
    move_command: Any = mocker.Mock()
    burn_fuel_command: Any = mocker.Mock()

    macro_command: MacroCommand = MacroCommand(
        [check_fuel_command, move_command, burn_fuel_command]
    )

    with pytest.raises(Exception):
        macro_command.execute()

    check_fuel_command.execute.assert_called_once()
    move_command.execute.assert_not_called()
    burn_fuel_command.execute.assert_not_called()


def test_move_with_fuel_command_bad_move_command(mocker: Any) -> None:
    check_fuel_command: Any = mocker.Mock()
    move_command: Any = mocker.Mock(**{"execute.side_effect": [Exception]})
    burn_fuel_command: Any = mocker.Mock()

    macro_command: MacroCommand = MacroCommand(
        [check_fuel_command, move_command, burn_fuel_command]
    )

    with pytest.raises(Exception):
        macro_command.execute()

    check_fuel_command.execute.assert_called_once()
    move_command.execute.assert_called_once()
    burn_fuel_command.execute.assert_not_called()


def test_move_with_fuel_command_bad_burn_fuel_command(mocker: Any) -> None:
    check_fuel_command: Any = mocker.Mock()
    move_command: Any = mocker.Mock()
    burn_fuel_command: Any = mocker.Mock(**{"execute.side_effect": [Exception]})

    macro_command: MacroCommand = MacroCommand(
        [check_fuel_command, move_command, burn_fuel_command]
    )

    with pytest.raises(Exception):
        macro_command.execute()

    check_fuel_command.execute.assert_called_once()
    move_command.execute.assert_called_once()
    burn_fuel_command.execute.assert_called_once()
