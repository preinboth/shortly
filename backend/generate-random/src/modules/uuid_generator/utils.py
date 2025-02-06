import binascii
import hashlib
import uuid
from base64 import b64encode
from uuid import UUID


async def build_uuid1() -> UUID:
	return uuid.uuid1(node=None, clock_seq=0x1234)


async def build_uuid3() -> UUID:
	pass


async def build_uuid2() -> str:
	# Holen Sie die MAC-Adresse des Systems
	mac_address = uuid.getnode()
	
	# Definieren Sie die lokale Domänenkennung (z. B. Benutzer-ID)
	domain = uuid.UUID('123e4567-e89b-12d3-a456-426655440000')
	
	# Generieren Sie den Zeitstempel (100-Nanosekunden-Präzision)
	time_stamp = uuid.uuid1().time
	
	# Berechnen Sie die UUID Version 2
	uuid2_bytes = uuid.uuid2(domain=domain, time=time_stamp, node=mac_address)
	
	# Konvertieren Sie die Bytes in eine UUID-Zeichenfolge
	int_uuid = uuid2_bytes.hex
	return str(int_uuid)


async def uuid_to_base64(uuid):
	uuid_bytes = str(uuid).encode('utf-8')
	uuid_base64 = b64encode(uuid_bytes)
	return uuid_base64


async def uuid_to_sha256(uuid):
	sha256 = hashlib.sha256()
	sha256.update(uuid.bytes)
	sha256_digest = sha256.digest()
	return binascii.hexlify(sha256_digest)


async def uuid_to_sha512(uuid):
	sha512 = hashlib.sha512()
	sha512.update(uuid.bytes)
	sha512_digest = sha512.digest()
	return binascii.hexlify(sha512_digest)


async def uuid_to_md5hash(uuid):
	uuid_bytes = uuid.bytes
	uuid_hash = hashlib.md5(uuid_bytes).hexdigest()
	return uuid_hash
