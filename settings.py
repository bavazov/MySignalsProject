import flet as ft

def main(page: ft.Page):
    current_language = "English"
    text_size = 16
    selected_index = 0

    translations = {
        "English": {
            "Language": "Language",
            "Dark Mode": "Dark Mode",
            "Text Size": "Text Size",
            "Settings": "Settings",
            "Users": "Users",
            "Sensors": "Sensors",
            "Data": "Data"
        },
        "Русский": {
            "Language": "Язык",
            "Dark Mode": "Тёмная тема",
            "Text Size": "Размер текста",
            "Settings": "Настройки",
            "Users": "Пользователи",
            "Sensors": "Сенсоры",
            "Data": "Данные"
        },
        "Deutsch": {
            "Language": "Sprache",
            "Dark Mode": "Dunkles Thema",
            "Text Size": "Textgröße",
            "Settings": "Einstellungen",
            "Users": "Benutzer",
            "Sensors": "Sensoren",
            "Data": "Daten"
        }
    }

    def get_text_color():
        return ft.Colors.BLACK if page.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.WHITE

    def get_bg_color():
        return ft.Colors.GREY_200 if page.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.GREY_800

    label_language = ft.Text(translations[current_language]["Language"], size=text_size, color=get_text_color())
    label_dark_mode = ft.Text(translations[current_language]["Dark Mode"], size=text_size, color=get_text_color())
    label_text_size = ft.Text(translations[current_language]["Text Size"], size=text_size, color=get_text_color())

    lang_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("English"),
            ft.dropdown.Option("Русский"),
            ft.dropdown.Option("Deutsch"),
        ],
        value="English",
        width=160,
        on_change=lambda e: change_language(e.control.value),
    )

    theme_switch = ft.Switch(
        label="",
        on_change=lambda e: toggle_theme(),
        value=False,
    )

    def update_nav_bar():
        nav_bar.destinations = [
            ft.NavigationBarDestination(icon=ft.Icons.DATA_OBJECT, label=translations[current_language]["Data"]),
            ft.NavigationBarDestination(icon=ft.Icons.SENSORS, label=translations[current_language]["Sensors"]),
            ft.NavigationBarDestination(icon=ft.Icons.PEOPLE, label=translations[current_language]["Users"]),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label=translations[current_language]["Settings"])
        ]
        nav_bar.selected_index = selected_index

    def change_language(selected):
        nonlocal current_language
        current_language = selected
        update_texts()

    def toggle_theme():
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        update_texts()

    def increase_text(e):
        nonlocal text_size
        text_size += 1
        update_texts()

    def decrease_text(e):
        nonlocal text_size
        text_size = max(8, text_size - 1)
        update_texts()

    def update_texts():
        label_language.value = translations[current_language]["Language"]
        label_dark_mode.value = translations[current_language]["Dark Mode"]
        label_text_size.value = translations[current_language]["Text Size"]

        label_language.size = text_size
        label_dark_mode.size = text_size
        label_text_size.size = text_size

        label_language.color = get_text_color()
        label_dark_mode.color = get_text_color()
        label_text_size.color = get_text_color()

        settings_panel.bgcolor = get_bg_color()
        update_nav_bar()
        page.update()

    btn_increase = ft.ElevatedButton("+", on_click=increase_text)
    btn_decrease = ft.ElevatedButton("-", on_click=decrease_text)

    settings_panel = ft.Container(
        content=ft.Column(
            spacing=25,
            controls=[
                ft.Row([label_language, lang_dropdown], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(thickness=1),
                ft.Row([label_dark_mode, theme_switch], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(thickness=1),
                ft.Row([
                    label_text_size,
                    ft.Row([btn_decrease, btn_increase], spacing=10)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ],
        ),
        padding=20,
        border_radius=10,
        bgcolor=get_bg_color(),
    )

    def on_nav_change(e):
        nonlocal selected_index
        selected_index = e.control.selected_index
        page.snack_bar = ft.SnackBar(ft.Text(f"You selected: {translations[current_language]['Settings' if selected_index == 0 else 'Users' if selected_index == 1 else 'Sensors' if selected_index == 2 else 'Data']}"))
        page.snack_bar.open = True
        page.update()

    nav_bar = ft.NavigationBar(
        destinations=[],  # заполним позже
        selected_index=selected_index,
        on_change=on_nav_change,
    )

    update_nav_bar()

    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Settings UI"
    page.padding = 20
    page.window_width = 420
    page.window_height = 600

    page.add(settings_panel)
    page.add(nav_bar)

ft.app(target=main)
