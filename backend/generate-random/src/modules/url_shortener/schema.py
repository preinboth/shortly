from pydantic import BaseModel, Field


#######################################################################
## 										Basic informations Schemas	    							 ##
#######################################################################
class ShortenerBase(BaseModel):
	target_url: str



#######################################################################
## 												Request Schemas														 ##
#######################################################################
class ShortenerCreateRequest(ShortenerBase):
	# destination: str
	# self_short: str
	# title: str
	domain: str
	# custom_back: str


class ShortenerUpdateRequest(ShortenerBase):
	pass


#######################################################################
## 												Response Schemas  												 ##
#######################################################################
class ShortenerResponse(ShortenerBase):
	"""
	Shortener data Response
	"""
	shortened_url: str

	
	class Config:
		from_attributes = True

