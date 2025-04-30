from aiogram import Router

from .admin import admin_router


main_router = Router(name='main_router')
main_router.include_router(admin_router)
