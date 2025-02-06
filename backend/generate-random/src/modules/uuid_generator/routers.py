from typing import List
from markdown import markdown
from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.config.settings import settings
from src.modules.uuid_generator import descr, schema
from src.modules.uuid_generator.service import uuid_service
from src.utils.utils import check_quantity

router = APIRouter(tags=["UUID"], prefix="/uuid")

@router.post('/generate', summary=descr.router_summary, description=descr.router_descr, tags=[descr.router_tag])
async def uuid(model: schema.UuidCreateRequest) -> List[schema.UuidResponse]:
	check_quantity(min=settings.UUID_QUANTITY_MIN, max=settings.UUID_QUANTITY_MAX, value=model.quantity)
	result: List[schema.UuidResponse] = []
	for i in range(model.quantity):
		l_uuid = await uuid_service.create(uuid_data=model)
		result.append(l_uuid)
	return result