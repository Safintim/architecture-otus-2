from architecture_otus_2.exception_handler import (
    ExceptionHandler,
    RepeatCommandHandler,
    WriteLogHandler,
    RepeatCommand,
    SecondRepeatCommand,
)
from typing import Any


def test_exception_strategy1(mocker: Any) -> None:
    """при первом выбросе исключения повторить команду, при повторном выбросе исключения записать информацию в лог."""
    command: Any = mocker.Mock()
    repeat_command: RepeatCommand = RepeatCommand(command)
    make_repeat_command: Any = mocker.Mock(return_value=repeat_command)

    log_command: Any = mocker.Mock()
    make_log_exception_command: Any = mocker.Mock(return_value=log_command)

    queue: Any = mocker.Mock()

    exception_handler: ExceptionHandler = ExceptionHandler()
    exception_handler.register_default_handler(
        RepeatCommandHandler(queue, make_repeat_command)
    )
    exception_handler.register_handler(
        RepeatCommand, Exception, WriteLogHandler(queue, make_log_exception_command)
    )

    exception_handler.handle(Exception("Oops"), command)
    assert queue.put_nowait.mock_calls[0] == mocker.call(repeat_command)

    exception_handler.handle(Exception("Oops"), repeat_command)
    assert queue.put_nowait.mock_calls[1] == mocker.call(log_command)


def test_exception_strategy2(mocker: Any) -> None:
    """повторить два раза, потом записать в лог"""

    command: Any = mocker.Mock()
    repeat_command: RepeatCommand = RepeatCommand(command)
    make_repeat_command: Any = mocker.Mock(return_value=repeat_command)

    second_repeat_command: SecondRepeatCommand = SecondRepeatCommand(repeat_command)
    make_second_repeat_command: Any = mocker.Mock(return_value=second_repeat_command)

    log_command: Any = mocker.Mock()
    make_log_exception_command: Any = mocker.Mock(return_value=log_command)

    queue: Any = mocker.Mock()

    exception_handler: ExceptionHandler = ExceptionHandler()
    exception_handler.register_default_handler(
        RepeatCommandHandler(queue, make_repeat_command)
    )
    exception_handler.register_handler(
        RepeatCommand,
        Exception,
        RepeatCommandHandler(queue, make_second_repeat_command),
    )
    exception_handler.register_handler(
        SecondRepeatCommand,
        Exception,
        WriteLogHandler(queue, make_log_exception_command),
    )

    exception_handler.handle(Exception("Oops"), command)
    assert queue.put_nowait.mock_calls[0] == mocker.call(repeat_command)

    exception_handler.handle(Exception("Oops"), repeat_command)
    assert queue.put_nowait.mock_calls[1] == mocker.call(second_repeat_command)

    exception_handler.handle(Exception("Oops"), second_repeat_command)
    assert queue.put_nowait.mock_calls[2] == mocker.call(log_command)
