from fastapi import APIRouter, status

from src.modules.qr_code.schema import QrCodeCreateRequest
from src.modules.qr_code.service import qrCodeService

router = APIRouter(tags=["QR-Code"], prefix="/qrcode")


@router.post(
    "/create",
    summary="create a QrCode",
    description="description",
    response_description="the creates QrCode",
    status_code=status.HTTP_200_OK,
)
async def create(req: QrCodeCreateRequest):
    return await qrCodeService.create(req)
