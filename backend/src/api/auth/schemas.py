from typing import Annotated
from annotated_types import MaxLen, MinLen
from string import ascii_letters, digits
from pydantic import BaseModel, EmailStr, field_validator


class AuthUserSchema(BaseModel):
    email: Annotated[EmailStr, MaxLen(255)]
    password: Annotated[str, MinLen(8), MaxLen(30)]

    @classmethod
    @field_validator('password')
    def validate_password(cls, pwd: str) -> str:
        pwd = pwd.strip()

        if not pwd:
            raise ValueError('Введите пароль')

        if not (8 <= len(pwd) <= 30):
            raise ValueError(
                'Длина пароля должна быть от 8 до 30 (включительно) символов'
            )

        if pwd.isdigit():
            raise ValueError('Пароль не может состоять только из цифр')

        has_upper = False
        has_special_char = False

        special_chars = '!@#$%^&*()'
        allowed_letters = ascii_letters + digits + special_chars

        for char in pwd:
            if char.isupper() and has_upper is False:
                has_upper = True

            if char in special_chars and has_special_char is False:
                has_special_char = True

            if char not in allowed_letters:
                raise ValueError(
                    'Пароль должен содержать латинские символы, цифры и спец-символы'
                )

        if not has_upper:
            raise ValueError('Пароль должен содержать хотя бы одну заглавную букву')

        if not has_special_char:
            raise ValueError('Пароль должен содержать хотя бы один спец-символ')

        return pwd
