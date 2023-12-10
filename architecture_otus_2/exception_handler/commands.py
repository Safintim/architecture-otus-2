from loguru import logger
from typing import Final
from architecture_otus_2.exception_handler.interfaces import ICommand


class LogExceptionCommand:
    def __init__(self, exception: Exception) -> None:
        self.exception: Final[Exception] = exception

    def execute(self) -> None:
        logger.error(repr(self.exception))


class RepeatCommand:
    def __init__(self, command: ICommand) -> None:
        self.command: Final[ICommand] = command

    def execute(self) -> None:
        self.command.execute()


class SecondRepeatCommand:
    def __init__(self, command: ICommand) -> None:
        self.command: Final[ICommand] = command

    def execute(self) -> None:
        self.command.execute()


def log_exception_command_maker(exception: Exception) -> LogExceptionCommand:
    return LogExceptionCommand(exception)


def repeat_command_maker(command: ICommand) -> RepeatCommand:
    return RepeatCommand(command)


def second_repeat_command_maker(command: ICommand) -> SecondRepeatCommand:
    return SecondRepeatCommand(command)
