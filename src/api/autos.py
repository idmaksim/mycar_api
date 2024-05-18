from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies import autos_service
from schemas.autos import AutoAddRequest
from services.autos import AutosService
from utils.error_handler import handle_route_error


router = APIRouter(
    prefix='/autos',
    tags=['Autos']
)


@router.get('/all')
async def get_all_autos(
    auto_service: Annotated[AutosService, Depends(autos_service)],
    limit: Annotated[int, 3]
):
    try:

        autos = await auto_service.get_all(limit)
        if autos:
            return autos
        raise HTTPException(
            detail='autos not found',
            status_code=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        await handle_route_error(e, status.HTTP_404_NOT_FOUND)


@router.post('', status_code=status.HTTP_201_CREATED)
async def add_auto(
    auto: AutoAddRequest,
    auto_service: Annotated[AutosService, Depends(autos_service)],
):
    try:
        new_auto = await auto_service.add_one(auto)
        return new_auto

    except Exception as e:
        await handle_route_error(e, status.HTTP_400_BAD_REQUEST)
