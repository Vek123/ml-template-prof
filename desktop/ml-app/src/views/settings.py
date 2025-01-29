import flet as ft
from flet_route import Params, Basket

from settings import settings


class SettingsView(object):
    def save_settings(
            self,
            api_host: ft.TextField,
            api_port: ft.TextField,
            error: ft.Text
    ):
        try:
            api_host = api_host.value
            api_port = int(api_port.value)
            error.value = ""
        except ValueError:
            error.value = "Введённые данные некорректны"
            return
        finally:
            error.update()

        settings.config["api_host"] = api_host
        settings.config["api_port"] = api_port
        settings.save_config()

    def view(
            self,
            page: ft.Page,
            params: Params,
            basket: Basket,
    ):
        api_host_input = ft.TextField(
            label="API Host",
            value=settings.api_host,
        )
        api_port_input = ft.TextField(
            label="API Port",
            value=settings.api_port,
        )
        error_text = ft.Text(color=ft.Colors.RED, size=18)

        return ft.View(
            route="/settings",
            controls=[
                ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text("Настройки", size=32),
                                        ft.IconButton(
                                            ft.Icons.HOME,
                                            on_click=lambda x: page.go("/"),
                                        ),
                                    ],
                                ),
                                ft.Column(
                                    spacing=10,
                                    width=300,
                                    expand=True,
                                    controls=[
                                        api_host_input,
                                        api_port_input,
                                    ],
                                ),
                            ]
                        ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                error_text,
                                ft.ElevatedButton(
                                    text="Сохранить",
                                    width=200,
                                    on_click=lambda _: self.save_settings(
                                        api_host_input,
                                        api_port_input,
                                        error_text,
                                    )
                                ),
                            ],
                        )
                    ],
                )
            ]
        )
