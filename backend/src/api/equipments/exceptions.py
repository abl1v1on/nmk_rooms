from fastapi import HTTPException, status


class EquipmentNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Equipment not found',
            status_code=status.HTTP_404_NOT_FOUND
        )


class EquipmentAlreadyExistsException(HTTPException):
    def __init__(self, field: str) -> None:
        super().__init__(
            detail=f'Equipment with this {field} already exists',
            status_code=status.HTTP_400_BAD_REQUEST
        )
