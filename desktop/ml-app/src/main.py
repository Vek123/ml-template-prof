import logging

import flet as ft
from flet_route import path, Routing

from settings import settings
from views.home import HomeView
from views.settings import SettingsView


APP_ROUTES = [
    path("/", True, HomeView().view),
    path("/settings", True, SettingsView().view)
]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flet_core")
logger.setLevel(logging.INFO)


def main(page: ft.Page):
    page.title = settings.app_name
    page.window.height = 400
    page.window.width = 600
    page.window.min_height = 300
    page.window.min_width = 300

    Routing(page, app_routes=APP_ROUTES)
    page.go("/")


if __name__ == "__main__":
    try:
        ft.app(main)
    except (RuntimeError, KeyboardInterrupt) as e:
        logger.error(e)
