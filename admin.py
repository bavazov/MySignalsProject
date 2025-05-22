import os
import tkinter as tk
from PIL import Image, ImageTk

# Функция для окрашивания иконок в нужный цвет
def colorize_icon(image_path, color_hex, size):
    img = Image.open(image_path).convert("RGBA").resize(size, Image.LANCZOS)
    r, g, b, a = img.split()
    color_img = Image.new("RGBA", img.size, color_hex)
    colored_icon = Image.composite(color_img, Image.new("RGBA", img.size), a)
    return colored_icon

# Функция для добавления строки сенсора (текст слева, иконка справа)
def add_sensor(frame, image_path, text):
    item_frame = tk.Frame(frame, bg='white', padx=5, pady=5)
    item_frame.pack(fill='x', padx=10, pady=0)

    content_frame = tk.Frame(item_frame, bg='white')
    content_frame.pack(fill='x')

    # Текст слева (bold)
    text_label = tk.Label(content_frame, text=text, font=('Helvetica', 14, 'bold'), bg='white', fg='black', anchor='w')
    text_label.grid(row=0, column=0, sticky='w', padx=(0, 10))

    # Иконка справа
    img = colorize_icon(image_path, "#007AFF", (40, 40))
    img_tk = ImageTk.PhotoImage(img)
    image_refs.append(img_tk)

    icon_label = tk.Label(content_frame, image=img_tk, bg='white')
    icon_label.grid(row=0, column=1, sticky='e')

    content_frame.grid_columnconfigure(0, weight=1)

    # Разделитель под сенсором
    separator = tk.Frame(frame, bg='#D3D3D3', height=1)
    separator.pack(fill='x', padx=10)

# Основное окно
root = tk.Tk()
root.title("Sensors")
root.configure(bg='white')
root.geometry('400x600')
root.minsize(300, 400)

root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Верхняя панель с фоном как у нижнего меню
top_bar = tk.Frame(root, bg='#F8F8F8')
top_bar.grid(row=0, column=0, sticky='ew')

# Заголовок на этой панели
title_label = tk.Label(top_bar, text="Sensors", font=('Helvetica', 18, 'bold'), bg='#F8F8F8', fg='#A0A0A0')
title_label.pack(pady=10)

# Линия-разделитель под заголовком
separator_top = tk.Frame(root, bg='#D3D3D3', height=1)
separator_top.grid(row=1, column=0, sticky='ew')

# Прокручиваемая область
container = tk.Frame(root, bg='white')
container.grid(row=2, column=0, sticky='nsew')

canvas = tk.Canvas(container, bg='white', highlightthickness=0)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg='white')
scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Прокрутка
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(event):
    canvas.itemconfig(scrollable_window, width=event.width)

scrollable_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_configure)
canvas.configure(yscrollcommand=scrollbar.set)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Сенсоры
sensors = [
    ("Body position", "icons/sens/position.png"),
    ("Body temperature", "icons/sens/temperature.png"),
    ("Electromyography", "icons/sens/muscle.png"),
    ("Electrocardiography", "icons/sens/ecg.png"),
    ("Airflow", "icons/sens/airflow.png"),
    ("Galvanic skin response", "icons/sens/skin.png"),
]

# Для хранения изображений
image_refs = []

# Добавляем сенсоры
for text, img_path in sensors:
    add_sensor(scrollable_frame, img_path, text)

# Разделитель перед нижним меню
separator_bottom = tk.Frame(root, bg='#D3D3D3', height=1)
separator_bottom.grid(row=3, column=0, sticky='ew')

# Нижнее меню
bottom_frame = tk.Frame(root, bg='#F8F8F8')
bottom_frame.grid(row=4, column=0, sticky='ew')

# Кнопки нижнего меню
menu_items = [
    ("Data", "icons/sens/data.png"),
    ("Sensors", "icons/sens/sensors.png"),
    ("Users", "icons/sens/users.png"),
    ("Settings", "icons/sens/settings.png"),
]

# Кнопки меню
def add_menu_button(frame, text, icon_path):
    btn_frame = tk.Frame(frame, bg='#F8F8F8')
    btn_frame.pack(side='left', fill='both', expand=True)

    # Sensors — иконка синяя, текст серый
    if text == "Sensors":
        icon_color = "#007AFF"
        text_color = "#A0A0A0"
    else:
        icon_color = "#A0A0A0"
        text_color = "#A0A0A0"

    img = colorize_icon(icon_path, icon_color, (24, 24))
    img_tk = ImageTk.PhotoImage(img)
    image_refs.append(img_tk)

    icon_label = tk.Label(btn_frame, image=img_tk, bg='#F8F8F8')
    icon_label.pack()

    text_label = tk.Label(btn_frame, text=text, font=('Helvetica', 10), fg=text_color, bg='#F8F8F8')
    text_label.pack()

for text, icon_path in menu_items:
    add_menu_button(bottom_frame, text, icon_path)

root.mainloop()
