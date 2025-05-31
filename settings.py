import flet as ft

def settings_view(page: ft.Page, on_nav_change):
    current_language = "English"
    text_size = 16
    selected_index = 3  # Settings tab

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

    label_language = ft.Text("", size=text_size, color=get_text_color())
    label_dark_mode = ft.Text("", size=text_size, color=get_text_color())
    label_text_size = ft.Text("", size=text_size, color=get_text_color())

    lang_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("English"),
            ft.dropdown.Option("Русский"),
            ft.dropdown.Option("Deutsch"),
        ],
        value=current_language,
        width=160,
    )

    theme_switch = ft.Switch(value=page.theme_mode == ft.ThemeMode.DARK)

    def change_language(e):
        nonlocal current_language
        current_language = e.control.value
        update_texts()

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        update_texts()

    def increase_text(e):
        nonlocal text_size
        text_size += 1
        update_texts()

    def decrease_text(e):
        nonlocal text_size
        text_size = max(8, text_size - 1)
        update_texts()

    lang_dropdown.on_change = change_language
    theme_switch.on_change = toggle_theme

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

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.DATA_OBJECT, label=""),
            ft.NavigationBarDestination(icon=ft.Icons.SENSORS, label=""),
            ft.NavigationBarDestination(icon=ft.Icons.PEOPLE, label=""),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label=""),
        ],
        selected_index=selected_index,
        on_change=on_nav_change,
    )

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

        nav_bar.destinations[0].label = translations[current_language]["Data"]
        nav_bar.destinations[1].label = translations[current_language]["Sensors"]
        nav_bar.destinations[2].label = translations[current_language]["Users"]
        nav_bar.destinations[3].label = translations[current_language]["Settings"]

        page.update()

    update_texts()

    return ft.Column([
        ft.Text(translations[current_language]["Settings"], size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(thickness=1),
        settings_panel,
        nav_bar
    ])
