from pydantic import BaseModel, field_validator
from ioc import Ioc


class OperationRequest(BaseModel):
    game_id: str
    game_object_id: str
    operation_id: str
    operation_args: dict

    @field_validator("game_id")
    @classmethod
    def game_exists(cls, game_id: str) -> str:
        game = Ioc.resolve("games", game_id)
        if game is None:
            raise ValueError("game not exists")
        return game_id


class OperationResponse(BaseModel):
    ...
