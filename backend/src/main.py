import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import settings
from api import main_api_router


def get_app() -> FastAPI:
    fastapi_app = FastAPI(
        title='NMK Rooms'
    )
    fastapi_app.include_router(main_api_router)
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
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
