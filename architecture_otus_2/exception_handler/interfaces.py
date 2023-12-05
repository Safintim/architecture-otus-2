from typing import Protocol


class ICommand(Protocol):
    def execute(self) -> None:
        ...
