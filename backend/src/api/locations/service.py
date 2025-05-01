from typing import Annotated
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.base_api_service import BaseAPIService
from core.models import Location, SESSION_DEP
from .schemas import CreateLocationSchema
from . import exceptions


class LocationAPIService(BaseAPIService[Location]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, model=Location)

    async def get_locations(self) -> list[Location]:
        query = select(self.model)
        locations = (await self.session.execute(query)).scalars().all()
        return locations

    async def get_location(self, location_id: int) -> Location | None:
        query = select(Location).filter(Location.id == location_id)
        location = (await self.session.execute(query)).scalar_one_or_none()

        if not location:
            raise exceptions.LocationNotFoundException()

        return location

    async def create_location(self, location: CreateLocationSchema) -> Location:
        if await self._is_exists(address=location.address):
            raise exceptions.LocationAlreadyExistsException('address')

        new_location = Location(**location.model_dump())
        self.session.add(new_location)
        await self.session.commit()
        return new_location


def get_service(session: SESSION_DEP) -> LocationAPIService:
    return LocationAPIService(session=session)


SERVICE_DEP = Annotated[
    LocationAPIService,
    Depends(get_service)
]
