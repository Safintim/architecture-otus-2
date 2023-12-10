from typing import Final, Protocol
from queue import Queue
from architecture_otus_2.exception_handler.interfaces import ICommand


class LogExceptionCommandMaker(Protocol):
    def __call__(self, exception: Exception) -> ICommand:
        ...


class RepeatCommandMaker(Protocol):
    def __call__(self, command: ICommand) -> ICommand:
        ...


class WriteLogHandler:
    def __init__(
        self, queue: Queue, log_command_maker: LogExceptionCommandMaker
    ) -> None:
        self.queue: Final[Queue] = queue
        self.log_command_maker: Final[LogExceptionCommandMaker] = log_command_maker

    def __call__(self, exception: Exception, command: ICommand) -> None:
        self.queue.put_nowait(self.log_command_maker(exception))


class RepeatCommandHandler:
    def __init__(self, queue: Queue, repeat_command_maker: RepeatCommandMaker) -> None:
        self.queue: Final[Queue] = queue
        self.repeat_command_maker: Final[RepeatCommandMaker] = repeat_command_maker

    def __call__(self, exception: Exception, command: ICommand) -> None:
        self.queue.put_nowait(self.repeat_command_maker(command))
