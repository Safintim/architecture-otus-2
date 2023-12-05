from architecture_otus_2.exception_handler.handlers import (
    WriteLogHandler,
    RepeatCommandHandler,
)
from typing import Any


def test_write_log_handler(mocker: Any) -> None:
    queue: Any = mocker.Mock()
    command: Any = mocker.Mock()
    command_maker: Any = mocker.Mock(return_value=command)
    handler = WriteLogHandler(queue, command_maker)

    exception: Exception = Exception()
    handler(exception, mocker.Mock())

    command_maker.assert_called_once_with(exception)
    queue.put_nowait.assert_called_once_with(command)


def test_repeat_command_handler(mocker: Any) -> None:
    queue: Any = mocker.Mock()
    command_returned: Any = mocker.Mock()
    command_maker: Any = mocker.Mock(return_value=command_returned)
    handler = RepeatCommandHandler(queue, command_maker)

    command: Any = mocker.Mock()
    handler(Exception(), command)

    command_maker.assert_called_once_with(command)
    queue.put_nowait.assert_called_once_with(command_returned)
