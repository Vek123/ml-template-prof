from fastapi import APIRouter, UploadFile
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/predict",
    tags=["Predictions"],
)


@router.post("/")
async def get_predict(file: UploadFile) -> JSONResponse:
    """
    Получить прогноз относительно поступаемой информации.
    """
    return JSONResponse(content={"status": "ok"}, status_code=200)
