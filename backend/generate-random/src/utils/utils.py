from fastapi import HTTPException
from fastapi import status as http_status


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
