import os
from typing import Annotated
from fastapi import APIRouter
# from services import 

router = APIRouter(
    prefix="/images",
    tags=["Images"]
)


if not os.path.exists('images'):
    os.mkdir('images')


@router.get("")
async def get_image(
    image_id: int,
    # service: Annotated[]
):
    pass