from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from logger.logger import logger
from src.modules.info.router import router as info_router


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    logger.info("init lifespan")
    # await create_db_and_tables()
    yield
    logger.info("clean up lifespan")


def create_api() -> FastAPI:
    _app = FastAPI(
        title=settings.API_TITLE,
        description=settings.API_DESCRIPTION,
        summary=settings.API_SUMMARY,
        version=settings.API_VERSION,
        terms_of_service=settings.API_TERMS_OF_SERVICE,
        contact={
            "name": settings.API_CONTACT_NAME,
            "url": settings.API_CONTACT_URL,
            "email": settings.API_CONTACT_EMAIL,
        },
        license_info={
            "name": settings.API_LICENCE_NAME,
            "url": settings.API_LICENCE_URL,
        },
        docs_url=settings.API_DOCS_URL,
        # docs_url="",  # deactivate this link
        redoc_url=settings.API_REDOC_URL,
        openapi_url=settings.API_OPENAPI_URL,
        debug=settings.API_DEBUG,
        lifespan=app_lifespan,
        # prefix=settings.API_PREFIX,
    )

    # CORS middleware
    logger.debug("Configuring CORS middleware")
    origins = [settings.origins]
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(info_router)

    return _app


api = create_api()
