from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='User not found',
            status_code=status.HTTP_404_NOT_FOUND
        )


class UserAlreadyExistsException(HTTPException):
    def __init__(self, field: str) -> None:
        super().__init__(
            detail=f'User with this {field} already exists',
            status_code=status.HTTP_400_BAD_REQUEST
        )
