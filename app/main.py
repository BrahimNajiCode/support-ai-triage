from fastapi import FastAPI
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from app.api.router import router
from app.core.config import Settings, get_settings
from app.db.health import verify_database_connection


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    verify_database_connection()
    yield



def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()


    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
    )

    application.include_router(
        router,
        prefix=settings.api_v1_prefix,
    )
    return application


app = create_app()