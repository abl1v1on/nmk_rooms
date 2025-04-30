from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        self.allowed_ids = [796397589]

    async def __call__(self, obj: Message | CallbackQuery) -> bool:
        user_id = obj.from_user.id
        return user_id in self.allowed_ids
