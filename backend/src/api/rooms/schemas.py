from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen, Gt


class BaseRoomSchema(BaseModel):
    number: Annotated[int, Gt(0)]
    capacity: Annotated[int, Gt(0)]
    description: Annotated[str, MinLen(5), MaxLen(100)]
    image: Annotated[str | None, MaxLen(10000)] = None
    location_id: Annotated[int, Gt(0)]


class GetRoomSchema(BaseRoomSchema):
    id: Annotated[int, Gt(0)]


class CreateRoomSchema(BaseRoomSchema):
    pass
