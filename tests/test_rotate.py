import pytest
from typing import Any
from architecture_otus_2.commands.rotate import Rotate
from unittest.mock import Mock


def test_rotate_ok(mocker: Any) -> None:
    rotable: Mock = mocker.Mock(
        **{
            "get_direction.return_value": 1,
            "get_angle_velocity.return_value": 5,
            "get_directions_number.return_value": 8,
        }
    )

    rotater: Rotate = Rotate(rotable)

    rotater.execute()

    rotable.get_direction.assert_called_once()
    rotable.get_angle_velocity.assert_called_once()
    rotable.get_directions_number.assert_called_once()
    rotable.set_direction.assert_called_once_with(6)


def test_get_direction_fail(mocker: Any) -> None:
    rotable: Mock = mocker.Mock(
        **{
            "get_direction.side_effect": [Exception("Cant get direction")],
        }
    )

    rotater: Rotate = Rotate(rotable)

    with pytest.raises(Exception):
        rotater.execute()

    rotable.get_direction.assert_called_once()
    rotable.get_angle_velocity.assert_not_called()
    rotable.set_direction.assert_not_called()
    rotable.get_directions_number.assert_not_called()


def test_get_angle_velocity_fail(mocker: Any) -> None:
    rotable: Mock = mocker.Mock(
        **{
            "get_angle_velocity.side_effect": [Exception("Cant get angle velocity")],
        }
    )

    rotater: Rotate = Rotate(rotable)

    with pytest.raises(Exception):
        rotater.execute()

    rotable.get_direction.assert_called_once()
    rotable.get_angle_velocity.assert_called_once()
    rotable.set_direction.assert_not_called()
    rotable.get_directions_number.assert_not_called()


def test_set_direction_fail(mocker: Any) -> None:
    rotable: Mock = mocker.Mock(
        **{
            "get_direction.return_value": 1,
            "get_angle_velocity.return_value": 5,
            "get_directions_number.return_value": 8,
            "set_direction.side_effect": [Exception("Cant get angle velocity")],
        }
    )

    rotater: Rotate = Rotate(rotable)

    with pytest.raises(Exception):
        rotater.execute()

    rotable.get_direction.assert_called_once()
    rotable.get_angle_velocity.assert_called_once()
    rotable.get_directions_number.assert_called_once()
    rotable.set_direction.assert_called_once_with(6)


def test_get_directions_number_fail(mocker: Any) -> None:
    rotable: Mock = mocker.Mock(
        **{
            "get_direction.return_value": 1,
            "get_angle_velocity.return_value": 5,
            "get_directions_number.side_effect": [Exception("Cant get angle velocity")],
        }
    )

    rotater: Rotate = Rotate(rotable)

    with pytest.raises(Exception):
        rotater.execute()

    rotable.get_direction.assert_called_once()
    rotable.get_angle_velocity.assert_called_once()
    rotable.get_directions_number.assert_called_once()
    rotable.set_direction.assert_not_called()
