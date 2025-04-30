import uvicorn
from fastapi import FastAPI

from core import settings


def get_app() -> FastAPI:
    fastapi_app = FastAPI(
        title='NMK Rooms'
    )
    return fastapi_app


app = get_app()


if __name__ == '__main__':
    uvicorn.run(
        app=settings.server.app,
        reload=settings.server.reload,
        host=settings.server.host,
        port=settings.server.port,
    )
