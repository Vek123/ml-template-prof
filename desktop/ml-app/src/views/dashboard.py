import flet as ft
from flet_route import Params, Basket


class DashboardView(object):
    def view(
            self,
            page: ft.Page,
            params: Params,
            basket: Basket,
    ) -> ft.View:
        return ft.View(
            route="/dashboard",
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Text("Dashboard", size=32),
                                ft.Column(
                                    controls=[
                                        ft.IconButton(
                                            ft.Icons.HOME,
                                            on_click=lambda x: page.go("/"),
                                        ),
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
            ]
        )
