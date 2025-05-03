from fastapi import APIRouter
from pydantic import PositiveInt

from .service import SERVICE_DEP
from .schemas import GetEquipmentSchema, CreateEquipmentSchema


router = APIRouter(prefix='/equipments', tags=['Оборудование'])


@router.get('/', response_model=list[GetEquipmentSchema])
async def get_equipments(service: SERVICE_DEP):
    return await service.get_equipments()


@router.get('/{equipment_id}', response_model=GetEquipmentSchema | None)
async def get_equipment_by_id(service: SERVICE_DEP, equipment_id: PositiveInt):
    return await service.get_equipment(id=equipment_id)


@router.post('/', response_model=GetEquipmentSchema)
async def create_equipment(service: SERVICE_DEP, equipment: CreateEquipmentSchema):
    return await service.create_equipment(equipment)
