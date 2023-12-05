import pytest
from loguru import logger
from typing import Any
from architecture_otus_2.exception_handler.commands import (
    LogExceptionCommand,
    RepeatCommand,
)


@pytest.fixture
def caplog(caplog):
    handler_id = logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove(handler_id)


def test_log_command(caplog: Any) -> None:
    text_exception: str = "Oops, error!"
    LogExceptionCommand(Exception(text_exception)).execute()
    assert text_exception in caplog.text


def test_repeat_command(mocker: Any) -> None:
    command: Any = mocker.Mock()
    repeat_command: RepeatCommand = RepeatCommand(command)

    repeat_command.execute()

    command.execute.assert_called_once()
