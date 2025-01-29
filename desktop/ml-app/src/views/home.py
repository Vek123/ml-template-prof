import flet as ft
from dependency_injector.wiring import inject, Provide
from flet_route import Params, Basket

from dependencies.containers import Application
from services.api import APIService


class HomeView(object):
    @inject
    def view(
            self,
            page: ft.Page,
            params: Params,
            basket: Basket,
            api_service: APIService = Provide[Application.services.api_service]
    ):
        return ft.View(
            route="/",
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text("ML Application", size=32),
                                ft.IconButton(
                                    ft.Icons.SETTINGS,
                                    on_click=lambda x: page.go("/settings"),
                                ),
                            ]
                        )
                    ]
                )
            ]
        )
