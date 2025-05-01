from fastapi import HTTPException, status


class RoomNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Room not found',
            status_code=status.HTTP_404_NOT_FOUND
        )


class RoomAlreadyExistsException(HTTPException):
    def __init__(self, field: str) -> None:
        super().__init__(
            detail=f'Room with this {field} already exists',
            status_code=status.HTTP_400_BAD_REQUEST
        )
