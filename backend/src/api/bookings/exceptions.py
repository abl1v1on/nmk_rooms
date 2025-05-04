from fastapi import HTTPException, status


class BookingNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            detail='Booking not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
