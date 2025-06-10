import httpx
from contextlib import asynccontextmanager
from typing import AsyncGenerator


base_url = 'http://localhost:8000/api/v1/'


@asynccontextmanager
async def get_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(base_url=base_url) as client:
        yield client


async def create_user(user: dict) -> None:
    async with get_client() as client:
        await client.post(url='users/', json=user)


async def get_users() -> list[str]:
    async with get_client() as client:
        response = await client.get(url='users/')
        users = response.json()
        pattern = (
            lambda user:
            f'{user['id']}. {user['first_name']} {user['last_name']} - {user['email']}'
        )
        return [pattern(user) for user in users]


async def create_location(location: dict) -> None:
    async with get_client() as client:
        await client.post(url='locations/', json=location)


async def get_locations() -> list[str]:
    async with get_client() as client:
        response = await client.get(url='locations/')
        locations = response.json()
        return [
            f'{index + 1}. {location['address']}'
            for index, location in enumerate(locations)
        ]


async def create_room(room: dict) -> None:
    async with get_client() as client:
        await client.post(url='rooms/', json=room)


async def get_rooms() -> list[str]:
    async with get_client() as client:
        response = await client.get(url='rooms/')
        rooms = response.json()
        return [
            f'{index + 1}. Зал {room['number']} ({room['location']['address']})'
            for index, room in enumerate(rooms)
        ]


async def create_equipment(equipment: dict) -> None:
    async with get_client() as client:
        await client.post(url='equipments/', json=equipment)


async def get_equipments() -> list[str]:
    async with get_client() as client:
        response = await client.get(url='equipments/')
        equipments = response.json()
        return [
            f'{index + 1}. {equipment['name']}'
            for index, equipment in enumerate(equipments)
        ]


async def add_equipments_to_room(data: dict) -> None:
    async with get_client() as client:
        await client.post(url='rooms/add-equipments', json=data)


async def get_user_bookings(user_id: int) -> list[str]:
    async with get_client() as client:
        response = await client.get(
            url=f'bookings/user-bookings?user_id={user_id}'
        )
        bookings = response.json()
        return [
            f'ID: {booking['id']}\nНомер зала: {booking['room']['number']}\nЦель бронирования: {booking['goal']}\nДата бронирования: {booking['booking_date']}\nВремя бронирования: {booking['booking_time']}' 
            for booking in bookings
        ]


async def delete_booking(booking_id: int) -> None:
    async with get_client() as client:
        response = await client.delete(url=f'bookings/{booking_id}')

        if response.status_code == 404:
            raise
