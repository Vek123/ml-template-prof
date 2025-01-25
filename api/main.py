import uvicorn
from fastapi import FastAPI

from api import router as api_router
from settings import settings


app = FastAPI(
    title="ML",
)
app.include_router(api_router)


if __name__ == "__main__":
    try:
        uvicorn.run(
            "main:app",
            host=settings.app_host,
            port=settings.app_port,
            reload=True,
            app_dir=settings.project_root,
        )
    except (RuntimeError, KeyboardInterrupt):
        pass
