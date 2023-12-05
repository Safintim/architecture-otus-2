from typing import Protocol, Final
from queue import Queue


class ICommand(Protocol):
    def execute(self) -> None:
        ...


class ExceptionHandler(Protocol):
    def handle(self, exception: Exception, command: ICommand) -> ICommand:
        ...


class EventLoop:
    def __init__(self, queue: Queue, exception_handler: ExceptionHandler) -> None:
        self.queue: Final[Queue] = queue
        self.exception_handler: Final[ExceptionHandler] = exception_handler

    def run(self) -> None:
        while not self.queue.empty():
            command: ICommand = self.queue.get_nowait()
            try:
                command.execute()
            except Exception as exception:
                self.exception_handler.handle(exception, command)
