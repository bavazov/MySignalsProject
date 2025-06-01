import flet as ft
import random

def data_view(page: ft.Page, on_nav_change):
    selected_index = 0  # Data tab

    MODULES = [
        "Body Position",
        "Body Temperature",
        "Electrocardiography",
        "Airflow",
        "Galvanic Skin Response"
    ]

    PERIODS = [
        "Live",
        "Day",
        "Week",
        "Month"
    ]

    selected_module = MODULES[0]
    selected_period = PERIODS[0]

    chart_row = ft.Row(alignment=ft.MainAxisAlignment.END, spacing=5)

    def generate_random_data():
        return [random.randint(10, 100) for _ in range(10)]

    def update_chart(data):
        chart_row.controls.clear()
        max_height = 150
        for v in data:
            bar = ft.Container(
                width=15,
                height=int(max_height * v / 100),
                bgcolor="#3f51b5",
                border_radius=3,
            )
            chart_row.controls.append(bar)
        page.update()

    # Создадим функции для генерации кнопок с учетом выбранных значений
    def create_module_buttons():
        return [
            ft.ElevatedButton(
                text=module,
                on_click=lambda e, m=module: on_module_click(e, m),
                bgcolor=ft.Colors.BLUE_200 if module == selected_module else None,
                color=ft.Colors.WHITE if module == selected_module else None,
            )
            for module in MODULES
        ]

    def create_period_buttons():
        return [
            ft.ElevatedButton(
                text=period,
                on_click=lambda e, p=period: on_period_click(e, p),
                bgcolor=ft.Colors.BLUE_200 if period == selected_period else None,
                color=ft.Colors.WHITE if period == selected_period else None,
            )
            for period in PERIODS
        ]

    def on_module_click(e, m):
        nonlocal selected_module
        selected_module = m
        update_chart(generate_random_data())
        # Обновляем кнопки и страницу
        module_row.controls.clear()
        module_row.controls.extend(create_module_buttons())
        page.update()

    def on_period_click(e, p):
        nonlocal selected_period
        selected_period = p
        update_chart(generate_random_data())
        # Обновляем кнопки и страницу
        period_row.controls.clear()
        period_row.controls.extend(create_period_buttons())
        page.update()

    update_chart(generate_random_data())

    module_row = ft.Row(create_module_buttons(), spacing=10)
    period_row = ft.Row(create_period_buttons(), spacing=10)

    main_content = ft.Column(
        [
            ft.Container(content=ft.Text("Select Module:", size=18, color=ft.Colors.BLACK)),
            module_row,
            ft.Container(content=ft.Text("Select Period:", size=18, color=ft.Colors.BLACK), margin=10),
            period_row,
            ft.Container(
                content=chart_row,
                alignment=ft.alignment.center,
                expand=True,
                margin=20,
                padding=20,
                bgcolor="#f0f0f0",
                border_radius=10,
                height=200,
            ),
        ],
        spacing=15,
        expand=True,
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

    return ft.Column(
        [
            main_content,
            nav_bar,
        ],
        expand=True,
    )
