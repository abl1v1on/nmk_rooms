from fastapi import APIRouter
from pydantic import PositiveInt

from .service import SERVICE_DEP
from .schemas import GetLocationSchema, CreateLocationSchema


router = APIRouter(prefix='/locations', tags=['Местоположения'])


@router.get('/', response_model=list[GetLocationSchema])
async def get_location(service: SERVICE_DEP):
    return await service.get_locations()


@router.get('/{location_id}', response_model=GetLocationSchema | None)
async def get_location_by_id(service: SERVICE_DEP, location_id: PositiveInt):
    return await service.get_location(location_id)


@router.post('/', response_model=GetLocationSchema)
async def create_location(service: SERVICE_DEP, location: CreateLocationSchema):
    return await service.create_location(location)
