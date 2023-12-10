import pytest
from typing import Any

from architecture_otus_2.event_loop import EventLoop


@pytest.fixture
def command(mocker: Any) -> Any:
    return mocker.Mock(**{"execute"})


def test_event_loop_run_ok(mocker: Any) -> None:
    command1: Any = mocker.Mock()
    command2: Any = mocker.Mock()
    queue: Any = mocker.Mock(
        **{
            "get_nowait.side_effect": [command1, command2],
            "empty.side_effect": [False, False, True],
        }
    )
    exception_handler: Any = mocker.Mock()

    event_loop: EventLoop = EventLoop(queue=queue, exception_handler=exception_handler)

    event_loop.run()

    assert queue.get_nowait.call_count == 2
    assert queue.empty.call_count == 3

    command1.execute.assert_called_once()
    command2.execute.assert_called_once()
    exception_handler.handle.assert_not_called()


class Command1Exception(Exception):
    ...


class Command2Exception(Exception):
    ...


def test_event_loop_run_exception(mocker: Any) -> None:
    command1: Any = mocker.Mock(**{"execute.side_effect": [Command1Exception]})
    command2: Any = mocker.Mock(**{"execute.side_effect": [Command2Exception]})
    queue: Any = mocker.Mock(
        **{
            "get_nowait.side_effect": [command1, command2],
            "empty.side_effect": [False, False, True],
        }
    )
    exception_handler: Any = mocker.Mock()

    event_loop: EventLoop = EventLoop(queue=queue, exception_handler=exception_handler)

    event_loop.run()

    assert queue.get_nowait.call_count == 2
    assert queue.empty.call_count == 3

    command1.execute.assert_called_once()
    command2.execute.assert_called_once()

    assert exception_handler.handle.call_count == 2

    exception_handler_calls: Any = exception_handler.handle.mock_calls
    assert (
        type(exception_handler_calls[0].args[0]),
        exception_handler_calls[0].args[1],
    ) == (Command1Exception, command1)
    assert (
        type(exception_handler_calls[1].args[0]),
        exception_handler_calls[1].args[1],
    ) == (Command2Exception, command2)
