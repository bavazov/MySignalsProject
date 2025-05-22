import flet as ft

translations = {
    "en": {
        "Data": "Data",
        "Sensors": "Sensors",
        "Users": "Users",
        "Settings": "Settings"
    }
}

current_language = "en"
selected_index = 1

sensor_items = [
    ("Body position", "icons/sens/position.png"),
    ("Body temperature", "icons/sens/temperature.png"),
    ("Electromyography", "icons/sens/muscle.png"),
    ("Electrocardiography", "icons/sens/ecg.png"),
    ("Airflow", "icons/sens/airflow.png"),
    ("Galvanic skin response", "icons/sens/skin.png"),
]

def main(page: ft.Page):
    def on_nav_change(e):
        print("Selected tab:", e.control.selected_index)

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

    sensor_list = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Text(label),
                ft.Image(src=icon_path, width=40, height=40),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(0.5, ft.Colors.GREY_300)
        )
        for label, icon_path in sensor_items
    ], expand=True)

    page.add(
        ft.Column([
            ft.Text("Sensors", size=24, weight=ft.FontWeight.BOLD),
            ft.Divider(height=1, color=ft.Colors.GREY_300),
            sensor_list,
            nav_bar
        ], expand=True)
    )

ft.app(target=main)
