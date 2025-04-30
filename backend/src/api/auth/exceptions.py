from fastapi import HTTPException, status


class InvalidCredentialsException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Invalid email or password',
            status_code=status.HTTP_401_UNAUTHORIZED
        )
