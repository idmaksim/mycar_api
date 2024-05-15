from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status, BackgroundTasks

from api.dependencies import documents_service
from schemas.documents import DocumentAddRequest
from services.documents import DocumentsService
from utils.error_handler import handle_route_error


router = APIRouter(
    prefix='/documents',
    tags=['Documents']
)


@router.post('', status_code=status.HTTP_201_CREATED)
async def add_document(
    document: DocumentAddRequest,
    document_service: Annotated[DocumentsService, Depends(documents_service)],
):
    try:

        new_document = await document_service.add_user(document)
        return new_document
    
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)

