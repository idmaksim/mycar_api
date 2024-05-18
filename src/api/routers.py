from fastapi import APIRouter
from api import users, documents, autos


main_api_router = APIRouter(
    prefix='/api'
)

routers = [
    users.router,
    documents.router,
    autos.router
]

[main_api_router.include_router(router) for router in routers]
