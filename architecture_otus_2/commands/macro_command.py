from architecture_otus_2.commands.interfaces import ICommand
from typing import Final


class MacroCommand:
    def __init__(self, commands: list[ICommand]) -> None:
        self.commands: Final[list[ICommand]] = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()
