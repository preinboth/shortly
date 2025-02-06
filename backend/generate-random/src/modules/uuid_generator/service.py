from src.modules.uuid_generator import schema, utils
from src.utils import converter


class UuidService:
	def __init__(self):
		pass
	
	async def create(self, uuid_data: schema.UuidCreateRequest):
		match uuid_data.type.value:
			case 'A':
				return await self._uuid_v1(model=uuid_data)
			case 'B':
				return await self._uuid_v3(model=uuid_data)
			case 'C':
				return await self._uuid_v4(model=uuid_data)
			case 'D':
				return await self._uuid_vc(model=uuid_data)
	
	async def _uuid_v1(self, model: schema.UuidCreateRequest) -> schema.UuidResponse:
		# "Version 1: Time-based"
		int_uuid = await utils.build_uuid1()
		uuid_base64 = await converter.str_to_base64(i=str(int_uuid))
		uuid_sha256 = await converter.str_to_sha256(i=str(int_uuid))
		uuid_sha512 = await converter.str_to_sha512(i=str(int_uuid))
		uuid_md5hash = await converter.str_to_md5hash(i=str(int_uuid))
		resp = schema.UuidResponse(
			uuid=str(int_uuid),
			base64=str(uuid_base64),
			sha256=str(uuid_sha256),
			sha512=str(uuid_sha512),
			md5hash=str(uuid_md5hash)
		)
		return resp
	
	async def _uuid_v3(self, model: schema.UuidCreateRequest) -> schema.UuidResponse:
		# "Version 3 UUIDs based on the MD5 hash of some data."
		int_uuid = await utils.build_uuid3()
		uuid_base64 = await converter.str_to_base64(i=str(int_uuid))
		uuid_sha256 = await converter.str_to_sha256(i=str(int_uuid))
		uuid_sha512 = await converter.str_to_sha512(i=str(int_uuid))
		uuid_md5hash = await converter.str_to_md5hash(i=str(int_uuid))
		resp = schema.UuidResponse(
			uuid=str(int_uuid),
			base64=str(uuid_base64),
			sha256=str(uuid_sha256),
			sha512=str(uuid_sha512),
			md5hash=str(uuid_md5hash)
		)
		return resp
	
	async def _uuid_v4(self, model: schema.UuidCreateRequest) -> schema.UuidResponse:
		# "Version 4: Random (Recommanded)"
		int_uuid = await utils.build_uuid1()
		uuid_base64 = await converter.str_to_base64(i=str(int_uuid))
		uuid_sha256 = await converter.str_to_sha256(i=str(int_uuid))
		uuid_sha512 = await converter.str_to_sha512(i=str(int_uuid))
		uuid_md5hash = await converter.str_to_md5hash(i=str(int_uuid))
		resp = schema.UuidResponse(
			uuid=str(int_uuid),
			base64=str(uuid_base64),
			sha256=str(uuid_sha256),
			sha512=str(uuid_sha512),
			md5hash=str(uuid_md5hash)
		)
		return resp
	
	async def _uuid_vc(self, model: schema.UuidCreateRequest) -> schema.UuidResponse:
		# "Custom: Version 4 & 5 md5 of UNIX microtime"
		int_uuid = await utils.build_uuid1()
		uuid_base64 = await converter.str_to_base64(i=str(int_uuid))
		uuid_sha256 = await converter.str_to_sha256(i=str(int_uuid))
		uuid_sha512 = await converter.str_to_sha512(i=str(int_uuid))
		uuid_md5hash = await converter.str_to_md5hash(i=str(int_uuid))
		resp = schema.UuidResponse(
			uuid=str(int_uuid),
			base64=str(uuid_base64),
			sha256=str(uuid_sha256),
			sha512=str(uuid_sha512),
			md5hash=str(uuid_md5hash)
		)
		return resp


uuid_service = UuidService()
