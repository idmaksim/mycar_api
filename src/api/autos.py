from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status, BackgroundTasks

from api.dependencies import documents_service
from schemas.documents import DocumentAddRequest
from services.documents import DocumentsService
from utils.error_handler import handle_route_error


router = APIRouter(
    prefix='/autos',
    tags=['Autos']
)


@router.get('/all')
async def get_all_autos(

):
    ...