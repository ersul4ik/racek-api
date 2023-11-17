from uuid import UUID

from fastapi import APIRouter

router = APIRouter(
    prefix="/guide",
    tags=["guides"],
    responses={404: {"description": "Not found"}},
)


@router.get("/tours/")
async def get_tours():
    raise NotImplemented


@router.get("/tours/{_uuid}/")
async def get_tour(_uuid: UUID):
    raise NotImplemented
