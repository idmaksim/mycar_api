from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status

from api.dependencies import users_service
from schemas.users import UserAddRequest
from services.users import UsersService
from utils.error_handler import handle_route_error


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('', status_code=status.HTTP_201_CREATED)
async def add_user(
    user: UserAddRequest,
    user_service: Annotated[UsersService, Depends(users_service)],
):
    try:
        print(user.email)

        new_user = await user_service.add_user(user)
        return new_user

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)


@router.get('', status_code=status.HTTP_200_OK)
async def get_user(
    user_service: Annotated[UsersService, Depends(users_service)],
    email: str,
    password: str
):
    try:
        user = await user_service.get_one(email=email, password=password)
        if user:
            return user

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='user not found'
        )

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)
