import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# --- UI CONFIGURATION ---
BG_LIGHT = 'white'
BG_DARK = '#1e1e1e'
TEXT_LIGHT = 'black'
TEXT_DARK = 'white'
MENU_BG = '#F8F8F8'

current_theme = 'light'
text_size = 12

image_refs = []

# --- COLORIZE ICON FUNCTION ---
def colorize_icon(image_path, color_hex, size):
    img = Image.open(image_path).convert("RGBA").resize(size, Image.LANCZOS)
    r, g, b, a = img.split()
    color_img = Image.new("RGBA", img.size, color_hex)
    colored_icon = Image.composite(color_img, Image.new("RGBA", img.size), a)
    return colored_icon

# --- THEME APPLY FUNCTION ---
def apply_theme(theme):
    global current_theme
    bg = BG_LIGHT if theme == 'light' else BG_DARK
    fg = TEXT_LIGHT if theme == 'light' else TEXT_DARK

    root.configure(bg=bg)
    settings_frame.configure(bg=bg)

    for frame in settings_frame.winfo_children():
        if isinstance(frame, tk.Frame):
            frame.configure(bg=bg)
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=bg, fg=fg)
            elif isinstance(widget, tk.Button):
                widget.configure(bg=bg, fg=fg)
            elif isinstance(widget, tk.Frame):
                widget.configure(bg=bg)

    # Apply styles to ttk widgets
    style.configure("TCombobox",
                    fieldbackground=bg,
                    background=bg,
                    foreground=fg)
    style.configure("TCheckbutton",
                    background=bg,
                    foreground=fg)

    current_theme = theme
    theme_var.set(theme == 'dark')

# --- THEME TOGGLE ---
def toggle_theme():
    if current_theme == 'light':
        apply_theme('dark')
    else:
        apply_theme('light')

# --- TEXT SIZE CONTROL ---
def increase_text():
    global text_size
    text_size += 1
    update_fonts()

def decrease_text():
    global text_size
    text_size = max(8, text_size - 1)
    update_fonts()

def update_fonts():
    for frame in settings_frame.winfo_children():
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(font=('Helvetica', text_size))

# --- UI SETUP ---
root = tk.Tk()
root.title("Settings")
root.geometry("400x600")
root.configure(bg=BG_LIGHT)

style = ttk.Style(root)
style.theme_use('default')

# Main content frame
settings_frame = tk.Frame(root, bg=BG_LIGHT)
settings_frame.pack(fill='both', expand=True, pady=20, padx=20)

# --- Setting Row Function ---
def add_setting_row(parent, label_text, widget):
    row = tk.Frame(parent, bg=parent['bg'])
    row.pack(fill='x', pady=10)

    label = tk.Label(row, text=label_text, font=('Helvetica', text_size), bg=parent['bg'], fg=TEXT_LIGHT, anchor='w')
    label.pack(side='left', fill='x', expand=True)

    widget.pack(side='right')

    return row

# --- Widgets ---
lang_selector = ttk.Combobox(settings_frame, values=["English", "Русский", "Deutsch"], state="readonly", width=15)
lang_selector.set("English")
add_setting_row(settings_frame, "Language", lang_selector)

theme_var = tk.BooleanVar(value=False)
theme_switch = ttk.Checkbutton(settings_frame, variable=theme_var, command=toggle_theme, style='Switch.TCheckbutton')
add_setting_row(settings_frame, "Dark Mode", theme_switch)

text_size_frame = tk.Frame(settings_frame, bg=BG_LIGHT)
btn_increase = tk.Button(text_size_frame, text="+", command=increase_text, width=3)
btn_decrease = tk.Button(text_size_frame, text="-", command=decrease_text, width=3)
btn_increase.pack(side='left', padx=5)
btn_decrease.pack(side='left')
add_setting_row(settings_frame, "Text Size", text_size_frame)

# --- Bottom Menu ---
bottom_menu = tk.Frame(root, bg=MENU_BG)
bottom_menu.pack(side='bottom', fill='x')

def add_menu_button(frame, text, icon_path):
    btn_frame = tk.Frame(frame, bg=MENU_BG)
    btn_frame.pack(side='left', fill='both', expand=True)

    if text == "Settings":
        icon_color = "#007AFF"
        text_color = "#007AFF"
    else:
        icon_color = "#A0A0A0"
        text_color = "#A0A0A0"

    img = colorize_icon(icon_path, icon_color, (24, 24))
    img_tk = ImageTk.PhotoImage(img)
    image_refs.append(img_tk)

    icon_label = tk.Label(btn_frame, image=img_tk, bg=MENU_BG)
    icon_label.pack()

    text_label = tk.Label(btn_frame, text=text, font=('Helvetica', 10), fg=text_color, bg=MENU_BG)
    text_label.pack()

menu_items = [
    ("Data", "icons/sens/data.png"),
    ("Sensors", "icons/sens/sensors.png"),
    ("Users", "icons/sens/users.png"),
    ("Settings", "icons/sens/settings.png"),
]

for text, icon in menu_items:
    add_menu_button(bottom_menu, text, icon)

# --- Style for switch ---
style.layout('Switch.TCheckbutton', [
    ('Checkbutton.padding', {
        'sticky': 'nswe',
        'children': [
            ('Checkbutton.indicator', {'side': 'left'}),
            ('Checkbutton.label', {'sticky': ''})
        ]
    })
])
style.configure('Switch.TCheckbutton', indicatorcolor='#007AFF', indicatorsize=40)

# --- Apply Light Theme Initially ---
apply_theme('light')

root.mainloop()
