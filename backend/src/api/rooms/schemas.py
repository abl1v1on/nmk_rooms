from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen, Gt

from api.locations.schemas import GetLocationSchema


class BaseRoomSchema(BaseModel):
    number: Annotated[int, Gt(0)]
    capacity: Annotated[int, Gt(0)]
    description: Annotated[str, MinLen(5), MaxLen(100)]
    image: Annotated[str | None, MaxLen(10000)] = None


class GetRoomSchema(BaseRoomSchema):
    id: Annotated[int, Gt(0)]
    location: GetLocationSchema


class CreateRoomSchema(BaseRoomSchema):
    location_id: Annotated[int, Gt(0)]
