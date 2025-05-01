from fastapi import HTTPException, status


class LocationNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Location not found',
            status_code=status.HTTP_404_NOT_FOUND
        )


class LocationAlreadyExistsException(HTTPException):
    def __init__(self, field: str) -> None:
        super().__init__(
            detail=f'Location with this {field} already exists',
            status_code=status.HTTP_400_BAD_REQUEST
        )
