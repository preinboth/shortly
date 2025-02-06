from fastapi import APIRouter, __version__
from fastapi.responses import HTMLResponse

from src.config.settings import settings

router = APIRouter(tags=["Information"])

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>{settings.API_TITLE}</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from {settings.API_TITLE}@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </div>
    </body>
</html>
"""


@router.get("/")
async def root():
    return HTMLResponse(html)


@router.get("/health")
async def health():
    return {"message": "API is running"}


@router.post("/ping")
async def ping():
    return {"message": "pong"}


@router.get("/version")
async def version():
    return {"version": settings.API_VERSION}
