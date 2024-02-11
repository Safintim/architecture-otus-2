from fastapi import APIRouter
from ioc import Ioc

from architecture_otus_2.operation_handler.models import (
    OperationRequest,
    OperationResponse,
)

router = APIRouter()


@router.post("/operations/", response_model=OperationResponse)
async def handle_operations(request: OperationRequest) -> OperationResponse:
    cmd = Ioc.resolve("InterpretCommand", request)
    Ioc.resolve("Put to queue", cmd)
    return OperationResponse()
