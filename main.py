import flet as ft
from users import users_view
from sensors import sensors_view
from settings import settings_view

def main(page: ft.Page):
    page.title = "Multi-View App"
    page.theme_mode = ft.ThemeMode.LIGHT  # ✅ Set light theme as default

    selected_index = 2  # Start on Users tab which is index 2 in NavigationBar

    views = {
        0: None,            # Data view not implemented yet
        1: sensors_view,
        2: users_view,
        3: settings_view,
    }

    def on_nav_change(e):
        nonlocal selected_index
        selected_index = e.control.selected_index
        page.controls.clear()
        view_func = views.get(selected_index)
        if view_func:
            page.add(view_func(page, on_nav_change))
        page.update()

    # Load initial view
    view_func = views.get(selected_index)
    if view_func:
        page.add(view_func(page, on_nav_change))

ft.app(target=main)
