from io import BytesIO

import qrcode
import qrcode.image.pil
import qrcode.image.svg
from fastapi import HTTPException, status

from src.config.settings import settings


class QrCodeService:

    def __init__(self):
        pass

    async def create(
        self,
        represent: str,
        box_size: int,
        border: int,
        image_format: str,
        fill_color: str,
        back_color: str,
    ):

        try:
            if not represent:
                raise HTTPException(
                    status_code=status.HTTP_204_NO_CONTENT, detail="represent is empty"
                )

            if len(represent) > settings.QRCODE_MAX_STRING:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"represent is too long (maximum {settings.QRCODE_MAX_STRING} characters allowed)",
                )

            # Generate QR code
            _qr = qrcode.QRCode(
                version=1,
                box_size=box_size,
                border=border,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
            )
            _qr.add_data(represent)
            _qr.make()
            img = _qr.make_image(fill_color=fill_color, back_color=back_color)

            # Save the image based on the specified format
            _bytes = BytesIO()

            if image_format == "jpg":
                img.save(_bytes, format="jpeg")
            elif image_format == "svg":
                img.save(_bytes, format="svg")
            # elif image_format == "eps":
            # 	img.save(bytes, format="eps")
            else:
                # Default to PNG if format is not recognized
                img.save(_bytes, format="png")

            retval = _bytes.getvalue()
            return retval

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error while generating QR code: " + str(e),
            )


qrCodeService = QrCodeService()
