import flet as ft
from flet_route import Params, Basket


class HomeView(object):
    def view(
            self,
            page: ft.Page,
            params: Params,
            basket: Basket,
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
