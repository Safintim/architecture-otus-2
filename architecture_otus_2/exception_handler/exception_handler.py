from typing import Protocol, DefaultDict
from collections import defaultdict

from architecture_otus_2.exception_handler.interfaces import ICommand


class Handler(Protocol):
    def __call__(self, exception: Exception, command: ICommand) -> None:
        ...


class ExceptionHandler:
    def __init__(self) -> None:
        self.handlers: DefaultDict[
            type[ICommand], dict[type[Exception], Handler]
        ] = defaultdict(dict)
        self.default_handler: Handler | None = None

    def register_handler(
        self, command: type[ICommand], exception: type[Exception], handler: Handler
    ) -> None:
        self.handlers[command].update({exception: handler})

    def register_default_handler(self, handler: Handler) -> None:
        self.default_handler = handler

    def handle(self, exception: Exception, command: ICommand) -> None:
        exception_type: type = exception.__class__
        command_type: type = command.__class__

        if not self.handlers.get(command_type):
            if self.default_handler is None:
                raise Exception("Default handler not set.")
            return self.default_handler(exception, command)

        handler: Handler = self.handlers[command_type][exception_type]

        handler(exception, command)
