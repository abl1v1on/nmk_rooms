from fastapi import APIRouter

from .users import users_router
from .auth import auth_router
from .rooms import rooms_router
from .locations import locations_router


main_api_router = APIRouter(prefix='/api/v1')
main_api_router.include_router(users_router)
main_api_router.include_router(auth_router)
main_api_router.include_router(rooms_router)
main_api_router.include_router(locations_router)
