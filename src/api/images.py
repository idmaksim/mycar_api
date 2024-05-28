import os
from fastapi import APIRouter

router = APIRouter(
    prefix="/images",
    tags=["Images"]
)


if not os.path.exists('images'):
    os.mkdir('images')


@router.get("")
async def get_image(

):
    pass