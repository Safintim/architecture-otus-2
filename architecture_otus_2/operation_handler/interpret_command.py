from architecture_otus_2.operation_handler.models import OperationRequest
from ioc import Ioc


class InterpretCommand:
    def __init__(self, operation: OperationRequest) -> None:
        self.operation = operation

    def execute(self) -> None:
        game = Ioc.resolve("games", self.operation.game_id)

        game_object = Ioc.resolve("games objects", game, self.operation.game_object_id)
        operation_name = Ioc.resolve("operations", self.operation.operation_id)
        command = Ioc.resolve(
            operation_name, game_object, **self.operation.operation_args
        )
        Ioc.resolve("Put to queue", command).execute()
