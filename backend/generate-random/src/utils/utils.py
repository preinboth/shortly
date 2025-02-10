import datetime
import secrets
import string
import time

from fastapi import HTTPException
from fastapi import status as http_status

digits = '0123456789'
symbols = '&#@=+-$*!?%*/_.'
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
exclude_similar = 'I, I, L, 1, L, O, 0, O '


def check_quantity(min: int, max: int, value: int):
	# TODO: check max quantity
	"""
	Überprüft, ob der Wert `value` zwischen `min` und `max` liegt.

	Args:
		min: Der minimale Wert.
		max: Der maximale Wert.
		value: Der zu überprüfende Wert.

	Raises:
		ValueError: Wenn `value` nicht zwischen `min` und `max` liegt.

	"""
	if value < 1 or not value:
		raise HTTPException(
			status_code=http_status.HTTP_400_BAD_REQUEST,
			detail="Quantity must not be less than 1 or empty",
		)
	
	if value < min or value > max:
		raise ValueError(f"Der Wert {value} liegt nicht zwischen {min} und {max}.")
	
	if value == min or value == max:
		return True


async def get_mixed_letters_numbers(length: int) -> str:
	letters = digits + lowercase + uppercase
	random_letters = []
	for _ in range(length):
		random_letter = secrets.choice(letters)
		random_letters.append(random_letter)
	result = random_string = "".join(random_letters)
	return result


async def get_mixed_letters_numbers_symbols(length: int) -> str:
	letters = digits + lowercase + uppercase + symbols
	random_letters = []
	for _ in range(length):
		random_letter = secrets.choice(letters)
		random_letters.append(random_letter)
	result = random_string = "".join(random_letters)
	return result


async def get_lowercase_letters(length: int) -> str:
	letters = lowercase
	random_letters = []
	for _ in range(length):
		random_letter = secrets.choice(letters)
		random_letters.append(random_letter)
	result = random_string = "".join(random_letters)
	return result


async def get_uppercase_letters(length: int) -> str:
	letters = uppercase
	random_letters = []
	for _ in range(length):
		random_letter = secrets.choice(letters)
		random_letters.append(random_letter)
	result = random_string = "".join(random_letters)
	return result


async def get_mixed_letters(length: int) -> str:
	letters = uppercase + lowercase
	random_letters = []
	for _ in range(length):
		random_letter = secrets.choice(letters)
		random_letters.append(random_letter)
	result = random_string = "".join(random_letters)
	return str(result)


async def get_numbers_letters(length: int) -> str:
	letters = digits
	random_letters = []
	for _ in range(length):
		random_letter = secrets.choice(letters)
		random_letters.append(random_letter)
	result = random_string = "".join(random_letters)
	return result


async def get_current_timestamp() -> int:
	current_timestamp = int(time.time())
	return current_timestamp


async def get_now_datetime():
	now = datetime.datetime.now()
	return now


async def conversion_bit(length) -> int:
	if length.name == 'A':
		return 64
	elif length.name == 'B':
		return 128
	elif length.name == 'C':
		return 256
	elif length.name == 'D':
		return 512
	elif length.name == 'E':
		return 1024
	elif length.name == 'F':
		return 2048


async def get_letter(type_, length):
	if type_.name == 'A':
		letter = await get_mixed_letters_numbers(length=length)
	elif type_.name == 'B':
		letter = await get_mixed_letters_numbers_symbols(length=length)
	elif type_.name == 'C':
		letter = await get_numbers_letters(length=length)
	elif type_.name == 'D':
		letter = await get_mixed_letters(length=length)
	elif type_.name == 'E':
		letter = await get_lowercase_letters(length=length)
	elif type_.name == 'F':
		letter = await get_uppercase_letters(length=length)
	else:
		return None
	
	return letter
