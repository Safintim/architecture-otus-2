from typing import Any
import pytest
from architecture_otus_2.commands.change_velocity import ChangeVelocityCommand
from architecture_otus_2.vector import Vector


def test_change_velocity_command_ok(mocker: Any) -> None:
    movable: Any = mocker.Mock(
        **{
            "get_velocity.return_value": Vector(10, 10),
            "get_velocity_rotate_factor.return_value": Vector(2, 2),
        }
    )
    command: ChangeVelocityCommand = ChangeVelocityCommand(movable)

    command.execute()

    movable.get_velocity.assert_called_once()
    movable.get_velocity_rotate_factor.assert_called_once()
    movable.set_velocity.assert_called_once_with(Vector(8, 8))


def test_change_velocity_command_if_stop(mocker: Any) -> None:
    movable: Any = mocker.Mock(
        **{
            "get_velocity.return_value": Vector(0, 0),
            "get_velocity_rotate_factor.return_value": Vector(2, 2),
        }
    )
    command: ChangeVelocityCommand = ChangeVelocityCommand(movable)

    command.execute()

    movable.get_velocity.assert_called_once()
    movable.get_velocity_rotate_factor.assert_not_called()
    movable.set_velocity.assert_not_called()


def test_change_velocity_command_bad_get_velocity(mocker: Any) -> None:
    movable: Any = mocker.Mock(
        **{
            "get_velocity.side_effect": [Exception],
            "get_velocity_rotate_factor.return_value": Vector(2, 2),
        }
    )
    command: ChangeVelocityCommand = ChangeVelocityCommand(movable)

    with pytest.raises(Exception):
        command.execute()

    movable.get_velocity.assert_called_once()
    movable.get_velocity_rotate_factor.assert_not_called()
    movable.set_velocity.assert_not_called()


def test_change_velocity_command_bad_get_velocity_rotate_factor(mocker: Any) -> None:
    movable: Any = mocker.Mock(
        **{
            "get_velocity.return_value": Vector(10, 10),
            "get_velocity_rotate_factor.side_effect": [Exception],
        }
    )
    command: ChangeVelocityCommand = ChangeVelocityCommand(movable)

    with pytest.raises(Exception):
        command.execute()

    movable.get_velocity.assert_called_once()
    movable.get_velocity_rotate_factor.assert_called_once()
    movable.set_velocity.assert_not_called()


def test_change_velocity_command_bad_set_velocity(mocker: Any) -> None:
    movable: Any = mocker.Mock(
        **{
            "get_velocity.return_value": Vector(10, 10),
            "get_velocity_rotate_factor.return_value": Vector(2, 2),
            "set_velocity.side_effect": [Exception],
        }
    )
    command: ChangeVelocityCommand = ChangeVelocityCommand(movable)

    with pytest.raises(Exception):
        command.execute()

    movable.get_velocity.assert_called_once()
    movable.get_velocity_rotate_factor.assert_called_once()
    movable.set_velocity.assert_called_once_with(Vector(8, 8))
