from typing import Annotated
from pydantic import BaseModel
from annotated_types import MinLen, MaxLen, Gt


class BaseLocationSchema(BaseModel):
    address: Annotated[str, MinLen(5), MaxLen(255)]


class GetLocationSchema(BaseLocationSchema):
    id: Annotated[int, Gt(0)]


class CreateLocationSchema(BaseLocationSchema):
    pass
