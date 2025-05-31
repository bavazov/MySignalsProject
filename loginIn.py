# login_view.py
import flet as ft
import database

def login_view(page: ft.Page, on_login_success):
    database.create_users_table()
    database.add_user("admin", "password123", role="admin")

    username = ft.TextField(label="Username", border_color="black", border_radius=6)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, border_color="black", border_radius=6)

    def login_click(e):
        if database.verify_user(username.value, password.value):
            on_login_success()  # Notify main.py to switch view
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Login Failed"), content=ft.Text("Invalid username or password."))
            page.dialog.open = True
            page.update()

    login_button = ft.ElevatedButton(
        text="Login",
        bgcolor="#007AFF",
        color="white",
        on_click=login_click,
        style=ft.ButtonStyle(padding=ft.padding.symmetric(horizontal=10, vertical=15))
    )

    form = ft.Column([
        ft.Text("Login", size=24, weight="bold", color="#007AFF"),
        username,
        password,
        login_button
    ], spacing=15, alignment=ft.MainAxisAlignment.CENTER)

    return ft.Column(
        [
            form,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
