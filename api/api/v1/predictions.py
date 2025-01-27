from fastapi import APIRouter, UploadFile
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.post("/base")
async def get_base_predict(file: UploadFile) -> JSONResponse:
    """
    Получить прогноз относительно поступаемой информации.
    """
    return JSONResponse(content={"status": "ok"}, status_code=200)
