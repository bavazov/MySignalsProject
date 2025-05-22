import flet as ft

VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def main(page: ft.Page):
    page.title = "Login"
    page.window_width = 600
    page.window_height = 300
    page.bgcolor = "white"
    page.theme = ft.Theme(font_family="Roboto")

    username = ft.TextField(label="Username", border_color="black", border_radius=6)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, border_color="black", border_radius=6)

    def login_click(e):
        if username.value == VALID_USERNAME and password.value == VALID_PASSWORD:
            page.dialog = ft.AlertDialog(title=ft.Text("Login Successful"), content=ft.Text("Welcome!"))
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

    # Right image logo
    logo = ft.Image(
        src="icons/menu/logo_mysignals.png",
        width=200,
        fit=ft.ImageFit.CONTAIN
    )

    logo_container = ft.Container(
        content=logo,
        width=220,
        padding=20,
        alignment=ft.alignment.center
    )

    page.add(
        ft.Row([
            ft.Container(form, expand=True, padding=20),
            logo_container
        ], expand=True)
    )

ft.app(target=main)
