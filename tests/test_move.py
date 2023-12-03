import pytest
from typing import Any
from architecture_otus_2.move import Move
from architecture_otus_2.vector import Vector
from unittest.mock import Mock


def test_move_ok(mocker: Any) -> None:
    movable: Mock = mocker.Mock(
        **{
            "get_location.return_value": Vector(12, 5),
            "get_velocity.return_value": Vector(-7, 3),
        }
    )

    mover: Move = Move(movable)

    mover.execute()

    movable.get_location.assert_called_once()
    movable.get_velocity.assert_called_once()
    movable.set_location.assert_called_once_with(Vector(5, 8))


def test_get_location_fail(mocker: Any) -> None:
    movable: Mock = mocker.Mock(
        **{
            "get_location.side_effect": [Exception("Cant get location")],
        }
    )

    mover: Move = Move(movable)

    with pytest.raises(Exception):
        mover.execute()

    movable.get_location.assert_called_once()
    movable.get_velocity.assert_not_called()
    movable.set_location.assert_not_called()


def test_get_velocity_fail(mocker: Any) -> None:
    movable: Mock = mocker.Mock(
        **{
            "get_velocity.side_effect": [Exception("Cant get velocity")],
        }
    )

    mover: Move = Move(movable)

    with pytest.raises(Exception):
        mover.execute()

    movable.get_location.assert_called_once()
    movable.get_velocity.assert_called_once()
    movable.set_location.assert_not_called()


def test_set_location_fail(mocker: Any) -> None:
    movable: Mock = mocker.Mock(
        **{
            "get_location.return_value": Vector(12, 5),
            "get_velocity.return_value": Vector(-7, 3),
            "set_location.side_effect": [Exception("Cant set location")],
        }
    )

    mover: Move = Move(movable)

    with pytest.raises(Exception):
        mover.execute()

    movable.get_location.assert_called_once()
    movable.get_velocity.assert_called_once()
    movable.set_location.assert_called_once_with(Vector(5, 8))
