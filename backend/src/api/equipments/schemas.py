from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen, Gt


class BaseEquipmentSchema(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(100)]


class GetEquipmentSchema(BaseEquipmentSchema):
    id: Annotated[int, Gt(0)]


class CreateEquipmentSchema(BaseEquipmentSchema):
    pass
