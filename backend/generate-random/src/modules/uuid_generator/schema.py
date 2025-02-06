from enum import Enum

from pydantic import BaseModel, PositiveInt
class Type(str, Enum):
	A = 'A'  # "Version 1: Time-based"
	B = 'B'  # "Version 2: DCE Security"
	C = 'C'  # "Version 4: Random (Recommanded)"
	D = 'D'  # "Custom: Version 4 & 5 md5 of UNIX microtime"

#######################################################################
## 										Basic informations Schemas	    							 ##
#######################################################################
class UuidBase(BaseModel):
	pass


#######################################################################
## 												Request Schemas														 ##
#######################################################################
class UuidCreateRequest(UuidBase):
	quantity: PositiveInt = 1
	type: Type


class UuidUpdateRequest(UuidBase):
	pass


#######################################################################
## 												Response Schemas  												 ##
#######################################################################
class UuidResponse(UuidBase):
	"""
	Uuid data Response
	"""
	uuid: str
	base64: str
	sha256: str
	sha512: str
	md5hash: str
	
	class Config:
		# orm_mode = True  # Konvertiert direkt aus ORM-Objekten
		from_attributes = True


class UuidsResponse(UuidBase):
	"""
	List of Uuids data Response
	"""
	
	data: list[UuidResponse]
	count: int