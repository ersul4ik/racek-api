from uuid import UUID

from fastapi import APIRouter

router = APIRouter()


@router.get("/tours/")
async def get_tours():
    return NotImplemented


@router.get("/tours/me/")
async def get_user_tours():
    return NotImplemented


@router.get("/tours/{uuid}/")
async def get_tour(uuid: UUID):
    return NotImplemented
