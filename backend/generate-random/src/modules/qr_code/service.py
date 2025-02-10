from io import BytesIO
from fastapi import HTTPException, status, Response
import qrcode
import qrcode.image.pil
import qrcode.image.svg
from qrcode.image.svg import SvgPathImage
from qrcode.image.styles.moduledrawers.svg import SvgPathCircleDrawer
from qrcode.image.styles.moduledrawers.svg import SvgPathSquareDrawer


from src.config.settings import settings
from src.modules.qr_code.schema import QrCodeCreateRequest, QrCodeResponse


class QrCodeService:

    def __init__(self):
        pass

    async def create(self, data: QrCodeCreateRequest):

        try:
            if not data.represent:
                raise HTTPException(
                    status_code=status.HTTP_204_NO_CONTENT, detail="represent must be specified"
                )

            if len(data.represent) > settings.QRCODE_MAX_STRING:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"represent is too long (maximum {settings.QRCODE_MAX_STRING} characters allowed)",
                )

            # Generate QR code
            _qr = qrcode.QRCode(
                version=1,
                box_size=data.box_size,
                border=data.border,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
            )
            _qr.add_data(data.represent)
            _qr.make()
            img = _qr.make_image(fill_color=data.fill_color, back_color=data.back_color)

            # Save the image based on the specified format
            _bytes = BytesIO()
            img_format = data.image_format.value
            img_format.lower()

            if data.image_format == "jpg":
                img.save(_bytes, format="jpeg")
                media_type = "image/jpeg"
            elif data.image_format == "svg":
                img.save(_bytes, format="svg")
                media_type = "image/svg+xml"
            # elif image_format == "eps":
            # 	img.save(bytes, format="eps")
            else:
                # Default to PNG if format is not recognized
                img.save(_bytes, format="png")
                media_type = "image/png"
            
            _bytes.seek(0)
            return Response(content=_bytes.getvalue(), media_type=media_type)
            # retval = _bytes.getvalue()
            #
            # resp = QrCodeResponse(
            #     resp=retval
            # )
            # return resp

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error while generating QR code: " + str(e),
            )


qrCodeService = QrCodeService()
