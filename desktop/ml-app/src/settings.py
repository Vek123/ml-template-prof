import json
import logging
from pathlib import Path


logger = logging.getLogger("flet")
logger.setLevel(logging.INFO)


class Settings(object):
    project_root: Path = Path("C:\\repos\\ml-template-prof\\desktop\\ml-app\\src")

    def __init__(self):
        self.config = self.read_config()

    def read_config(self) -> dict:
        try:
            with open(self.project_root / "config.json", "rb") as file:
                return json.load(file)
        except FileNotFoundError as e:
            logger.error(e)
            return dict()

    def save_config(self) -> None:
        try:
            with open(self.project_root / "config.json", "w") as file:
                json.dump(self.config, file)
        except FileNotFoundError as e:
            logger.error(e)
            return


settings = Settings()
