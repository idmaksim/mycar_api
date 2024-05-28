from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

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
    service: Annotated[DocumentsService, Depends(documents_service)],
):
    try:
        new_document = await service.add_document(document)
        return new_document

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)


@router.get('')
async def get_document_by_user_email(
    service: Annotated[DocumentsService, Depends(documents_service)],
    user_email: str
):
    try:
        document = await service.get_by_user_email(user_email)
        if document:
            return document

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='document not found'
        )

    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_404_NOT_FOUND)


@router.put('')
async def update_document_by_id(
    id: int,
    new_document: DocumentAddRequest,
    service: Annotated[DocumentsService, Depends(documents_service)],
):
    try:
        new_doc = await service.update_by_id(id, new_document)
        return new_doc
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_304_NOT_MODIFIED)
