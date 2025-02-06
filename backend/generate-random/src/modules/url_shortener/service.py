import random
import string

from src.modules.url_shortener.schema import ShortenerResponse, ShortenerCreateRequest


class UrlShortenerService:
	def __init__(self):
		self._characters = string.ascii_letters + string.digits
	

	async def create(self, data: ShortenerCreateRequest) -> ShortenerResponse:
		# Implementierung folgt hier
		_short_code = ''.join(random.choices(self._characters, k=6))
		_short = data.domain + _short_code
		
		response_data = {
			'shortened_url': _short,
			'target_url': data.target_url,
		}
		
		return ShortenerResponse.model_validate(response_data)
	
urlShortenerService = UrlShortenerService()