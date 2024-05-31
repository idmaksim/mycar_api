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


@router.get("{image_name}")
async def get_image(
    image_name: str,
    service: Annotated[ImagesService, Depends(images_service)]
):
    try:
        image_path = await service.get_image_path_by_name(image_name)
        if os.path.exists(image_path):
            return FileResponse(image_path)
        raise FileNotFoundError(f"Image with id {image_name} not found")
    
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)