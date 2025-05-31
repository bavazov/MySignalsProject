import flet as ft
from database import (
    create_users_table,
    add_user,
    get_all_users,
    update_user_role,
    delete_user,
)

def users_view(page: ft.Page, on_nav_change):
    selected_index = 2  # Users tab index

    # Ensure users table exists
    create_users_table()

    user_list = ft.Column(spacing=10, expand=True)

    def refresh_user_list():
        user_list.controls.clear()
        for user in get_all_users():
            user_id, username, role = user
            user_list.controls.append(
                ft.Row([
                    ft.Text(username, width=150),
                    ft.Dropdown(
                        width=150,
                        value=role,
                        options=[
                            ft.dropdown.Option("admin"),
                            ft.dropdown.Option("user"),
                            ft.dropdown.Option("guest"),
                        ],
                        on_change=lambda e, uid=user_id: on_role_change(e, uid),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        tooltip="Delete User",
                        on_click=lambda e, uid=user_id: on_delete_user(uid),
                    )
                ])
            )
        page.update()

    def on_role_change(e, user_id):
        new_role = e.control.value
        update_user_role(user_id, new_role)
        page.snack_bar = ft.SnackBar(ft.Text(f"Role updated to {new_role}"))
        page.snack_bar.open = True
        page.update()

    def on_delete_user(user_id):
        delete_user(user_id)
        refresh_user_list()
        page.snack_bar = ft.SnackBar(ft.Text("User deleted"))
        page.snack_bar.open = True
        page.update()

    def on_add_user_click(e):
        username_input = ft.TextField(label="Username")
        password_input = ft.TextField(label="Password", password=True, can_reveal_password=True)
        role_dropdown = ft.Dropdown(
            label="Role",
            value="user",
            options=[
                ft.dropdown.Option("admin"),
                ft.dropdown.Option("user"),
                ft.dropdown.Option("guest"),
            ]
        )

        def add_user_action(e):
            username = username_input.value.strip()
            password = password_input.value.strip()
            role = role_dropdown.value

            if not username or not password:
                dialog.content = ft.Text("Username and password are required.")
                dialog.update()
                return

            add_user(username, password, role)
            refresh_user_list()
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Add New User"),
            content=ft.Column([
                username_input,
                password_input,
                role_dropdown,
            ], spacing=10),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: close_dialog()),
                ft.ElevatedButton("Add", on_click=add_user_action),
            ],
            on_dismiss=lambda e: close_dialog(),
        )

        def close_dialog():
            dialog.open = False
            page.update()

        page.dialog = dialog
        dialog.open = True
        page.update()

    # --- Layout ---
    title = ft.Text("Users Panel", size=24, weight=ft.FontWeight.BOLD)

    add_user_btn = ft.ElevatedButton(
        "Add User", icon=ft.Icons.PERSON_ADD, on_click=on_add_user_click
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

    content = ft.Column(
        [
            title,
            ft.Divider(),
            add_user_btn,
            user_list,
            nav_bar
        ],
        spacing=20,
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    )

    refresh_user_list()
    return content
