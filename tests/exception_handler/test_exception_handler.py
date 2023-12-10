from architecture_otus_2.exception_handler import ExceptionHandler
from typing import Any, Callable
import pytest


class Command1Test:
    def execute(self) -> None:
        ...


class Command2Test:
    def execute(self) -> None:
        ...


class ExceptionTest(Exception):
    ...


def test_register_handler_ok() -> None:
    handler: Callable = lambda x, y: ...  # noqa: E731 lambda
    exception_handler: ExceptionHandler = ExceptionHandler()
    exception_handler.register_handler(Command1Test, ExceptionTest, handler)
    exception_handler.register_handler(Command1Test, ExceptionTest, handler)
    exception_handler.register_handler(Command2Test, ExceptionTest, handler)

    assert exception_handler.handlers == {
        Command1Test: {ExceptionTest: handler},
        Command2Test: {ExceptionTest: handler},
    }


def test_handle_ok(mocker: Any) -> None:
    handler: Any = mocker.Mock()
    exception_handler: ExceptionHandler = ExceptionHandler()
    exception_handler.register_handler(Command1Test, ExceptionTest, handler)
    exception_handler.register_handler(Command2Test, ExceptionTest, handler)

    exception: ExceptionTest = ExceptionTest()
    command: Command1Test = Command1Test()

    exception_handler.handle(exception, command)

    handler.assert_called_once_with(exception, command)


def test_handle_default(mocker: Any) -> None:
    default_handler: Any = mocker.Mock()
    handler: Any = mocker.Mock()
    exception_handler: ExceptionHandler = ExceptionHandler()
    exception_handler.register_default_handler(default_handler)
    exception_handler.register_handler(Command2Test, ExceptionTest, handler)

    exception: ExceptionTest = ExceptionTest()
    command1: Command1Test = Command1Test()
    command2: Command2Test = Command2Test()

    exception_handler.handle(exception, command1)
    exception_handler.handle(exception, command2)

    default_handler.assert_called_once_with(exception, command1)
    handler.assert_called_once_with(exception, command2)


def test_handle_default_not_set(mocker: Any) -> None:
    exception_handler: ExceptionHandler = ExceptionHandler()

    with pytest.raises(Exception):
        exception_handler.handle(ExceptionTest(), Command1Test())
