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
            lambda index, user:
            f'{index + 1}. {user['first_name']} {user['last_name']} - {user['email']}'
        )
        return [pattern(index, user) for index, user in enumerate(users)]


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
