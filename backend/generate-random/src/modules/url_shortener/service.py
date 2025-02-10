import random
import string
from fastapi import status, HTTPException

from src.modules.url_shortener.schema import ShortenerCreateRequest, ShortenerResponse
from src.modules.url_shortener.settings import settings as shortner_settings
from src.utils.utils import get_mixed_letters


class UrlShortenerService:
    def __init__(self):
        self._characters = string.ascii_letters + string.digits

    async def create(self, data: ShortenerCreateRequest) -> ShortenerResponse:
        # Implementierung folgt hier
        await self._check_data(data=data)
        
        #TODO: data.domain auf Ende "/" prüfen, wenn nicht vorhanden, anhängen
        
        #TODO: data.target_url auf URL prüfen, http oder www, oder beides
        
        _short = await self._new_short(length=shortner_settings.SHORT_LENGTH_DEFAULT)

        resp = ShortenerResponse(
            domain=data.domain,
            target_url=data.target_url,
            shortened_url=str (str(data.domain) + str(_short)),
            short=_short
        )
        return resp
    
    async def _check_data(self, data: ShortenerCreateRequest):
        # TODO: klassenbasierte Exceptions verwenden
        if not data.domain:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Domain must be specified")
    
        if not data.target_url:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Target-URL must be specified")


    async def _new_short(self, length: int) -> str:
        return await get_mixed_letters(length=length)

urlShortenerService = UrlShortenerService()
