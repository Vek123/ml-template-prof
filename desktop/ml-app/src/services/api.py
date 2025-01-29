import contextlib
from io import TextIOWrapper

import aiohttp

from settings import settings


class APIService(object):
    def __init__(self, session: aiohttp.ClientSession, host: str, port: int):
        self.session = session
        self.base_url = f"http://{host}:{port}"

    def get_predict(self, file: TextIOWrapper) -> dict:
        with self.session.post(
            url=self.base_url + "/api/v1/predictions/base",
            data={"file": file},
        ) as response:
            return response.text()

    @staticmethod
    @contextlib.contextmanager
    def get_session() -> aiohttp.ClientSession:
        with aiohttp.ClientSession() as session:
            yield session


def get_api_service(session: aiohttp.ClientSession) -> APIService:
    return APIService(session, settings.api_host, settings.api_port)
