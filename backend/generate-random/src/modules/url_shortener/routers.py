from fastapi import APIRouter

from src.modules.url_shortener.schema import ShortenerCreateRequest
from src.modules.url_shortener.service import urlShortenerService

router = APIRouter(
    tags=["Url-Shortener"],
    prefix="/shortener",
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/create",
    summary="create a urlshort",
    description="description",
    # tags=['UrlShort'],
    response_description="the creates Urlshorts",
)
async def create(req: ShortenerCreateRequest):
    return await urlShortenerService.create(req)
