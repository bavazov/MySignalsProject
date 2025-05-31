import flet as ft

def sensors_view(page: ft.Page, on_nav_change):
    current_language = "en"
    selected_index = 1  # Sensors tab

    translations = {
        "en": {
            "Data": "Data",
            "Sensors": "Sensors",
            "Users": "Users",
            "Settings": "Settings"
        }
    }

    sensor_items = [
        ("Body position", "icons/sens/position.png"),
        ("Body temperature", "icons/sens/temperature.png"),
        ("Electrocardiography", "icons/sens/muscle.png"),
        ("Electrocardiography", "icons/sens/ecg.png"),
        ("Airflow", "icons/sens/airflow.png"),
        ("Galvanic skin response", "icons/sens/skin.png"),
    ]

    sensor_list = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Text(label, color=ft.Colors.BLACK),
                ft.Image(src=icon_path, width=40, height=40),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(0.5, ft.Colors.GREY_300)
        )
        for label, icon_path in sensor_items
    ], expand=True)

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.DATA_OBJECT, label=translations[current_language]["Data"]),
            ft.NavigationBarDestination(icon=ft.Icons.SENSORS, label=translations[current_language]["Sensors"]),
            ft.NavigationBarDestination(icon=ft.Icons.PEOPLE, label=translations[current_language]["Users"]),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label=translations[current_language]["Settings"])
        ],
        selected_index=selected_index,
        on_change=on_nav_change
    )

    return ft.Column([
        ft.Text("Sensors", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
        ft.Divider(height=1, color=ft.Colors.GREY_300),
        sensor_list,
        nav_bar
    ])
