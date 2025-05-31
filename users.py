import flet as ft

def users_view(page: ft.Page, on_nav_change):
    selected_index = 2  # Assuming "Users" tab is index 2 in your NavigationBar

    title = ft.Text("Users Panel", size=24, weight=ft.FontWeight.BOLD)

    user_controls = ft.Container(
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("Manage users, roles, and permissions."),
                ft.ElevatedButton("Add User", icon=ft.Icons.PERSON_ADD),
                ft.ElevatedButton("Manage Roles", icon=ft.Icons.ADMIN_PANEL_SETTINGS),
            ],
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.Colors.GREY_100 if page.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.GREY_800,
    )

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.DATA_OBJECT, label="Data"),
            ft.NavigationBarDestination(icon=ft.Icons.SENSORS, label="Sensors"),
            ft.NavigationBarDestination(icon=ft.Icons.PEOPLE, label="Users"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
        ],
        selected_index=selected_index,
        on_change=on_nav_change,
    )

    return ft.Column([
        title,
        ft.Divider(thickness=1),
        user_controls,
        nav_bar,
    ])
