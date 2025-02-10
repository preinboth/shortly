from black import Enum
from pydantic import BaseModel, Field, PositiveInt


class ImageFormat(Enum):
	A = "JPG" ## Joint Photographers Expert Group
	B = "PNG" ## Portable Networks Graphics
	C = "SVG" ## Scalable Vector Graphics
	


#######################################################################
## 										Basic informations Schemas	    							 ##
#######################################################################
class QrCodeBase(BaseModel):
	pass


#######################################################################
## 												Request Schemas														 ##
#######################################################################
class QrCodeCreateRequest(QrCodeBase):
	represent: str = Field(default="https://example.com", description="Inhalt des QR-Codes")
	box_size: PositiveInt = Field(default=10, ge=1, le=50, description="Größe der Boxen")
	border: int = Field(default=4, ge=0, le=10, description="Rand des QR-Codes")
	image_format: ImageFormat
	fill_color: str = Field(default='#000000', description="Farbe der QR-Code-Elemente")
	back_color: str = Field(default='#FFFFFF', description="Hintergrundfarbe des QR-Codes")
	class Config:
		from_attributes = True

class QrCodeUpdateRequest(QrCodeBase):
	pass


#######################################################################
## 												Response Schemas  												 ##
#######################################################################
class QrCodeResponse(QrCodeBase):
	"""
    QrCode data Response
    """
	
	resp: bytes
	
	class Config:
		from_attributes = True
