from pydantic import BaseModel, PositiveInt, HttpUrl


#######################################################################
## 										Basic informations Schemas	    							 ##
#######################################################################
class ShortenerBase(BaseModel):
    domain: HttpUrl
    target_url: str = ''


#######################################################################
## 												Request Schemas														 ##
#######################################################################
class ShortenerCreateRequest(ShortenerBase):
    pass


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
    short: str

    class Config:
        from_attributes = True
