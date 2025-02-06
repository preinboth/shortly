import hashlib
from base64 import b64encode

################
# loc = locale #
################


async def encode_as_bytes(i: str) -> bytes:
    """
    Encode a string as bytes
    Args:
            i: str to encode

    Returns: bytes

    """
    loc_bytes = i.encode("utf-8")
    return loc_bytes


async def str_to_base64(i: str):
    """
    convert string to base64
    Args:
            i: str to convert

    Returns: base64 encoded string

    """
    loc_bytes = await encode_as_bytes(i)
    loc_base64 = b64encode(loc_bytes)
    return loc_base64


async def str_to_sha256(i: str):
    """
    convert string to sha256
    Args:
            i: str to convert

    Returns: sha256 encoded string

    """
    loc_bytes = await encode_as_bytes(i)
    # Use SHA-256 hash function to create a hash object
    loc_hash_object = hashlib.sha256(loc_bytes)
    # Get the hexadecimal representation of the hash
    loc_hash = loc_hash_object.hexdigest()
    return loc_hash


async def str_to_sha512(i: str):
    """
    convert string to sha512
    Args:
            i: string to convert

    Returns: sha512 encoded string

    """
    loc_bytes = await encode_as_bytes(i)
    # Use SHA-256 hash function to create a hash object
    loc_hash_object = hashlib.sha512(loc_bytes)
    # Get the hexadecimal representation of the hash
    loc_hash = loc_hash_object.hexdigest()
    return loc_hash


async def str_to_md5hash(i: str):
    """
    convert string to md5hash
    Args:
            i: string to convert

    Returns: md5hash encoded string

    """
    loc_bytes = await encode_as_bytes(i)
    # Use MD5 hash function to create a hash object
    loc_hash_object = hashlib.md5(loc_bytes)
    # Get the hexadecimal representation of the hash
    loc_hash = loc_hash_object.hexdigest()
    return loc_hash
