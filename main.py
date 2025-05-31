import flet as ft
from loginIn import login_view
from users import users_view
from sensors import sensors_view
from settings import settings_view

def main(page: ft.Page):
    page.title = "MySignals App"
    page.theme_mode = ft.ThemeMode.LIGHT

    selected_index = 2  # Users tab default

    views = {
        0: None,
        1: sensors_view,
        2: users_view,
        3: settings_view,
    }

    def show_main_app():
        page.controls.clear()

        def on_nav_change(e):
            nonlocal selected_index
            selected_index = e.control.selected_index
            page.controls.clear()
            view_func = views.get(selected_index)
            if view_func:
                page.add(view_func(page, on_nav_change))
            page.update()

        view_func = views.get(selected_index)
        if view_func:
            page.add(view_func(page, on_nav_change))
        page.update()

    def on_login_success():
        show_main_app()

    # Start with login view
    page.add(login_view(page, on_login_success))

ft.app(target=main)
