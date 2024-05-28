import os
from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import FileResponse
from api.dependencies import images_service
from services.images import ImagesService
from utils.error_handler import handle_route_error 

router = APIRouter(
    prefix="/images",
    tags=["Images"]
)


if not os.path.exists('images'):
    os.mkdir('images')


@router.get("")
async def get_image(
    image_id: int,
    service: Annotated[ImagesService, Depends(images_service)]
):
    try:
        image_path = await service.get_image_path_by_id(image_id)
        return FileResponse(image_path)
    
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)