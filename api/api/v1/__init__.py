from fastapi import APIRouter

from api.v1.predictions import router as predictions_router


router = APIRouter(
    prefix="/v1",
)
router.include_router(predictions_router)
