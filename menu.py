import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Dummy credentials for validation
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Main window
root = tk.Tk()
root.title("Login")
root.geometry("600x300")
root.configure(bg='white')
root.resizable(False, False)

# Main frame
main_frame = tk.Frame(root, bg='white')
main_frame.pack(fill='both', expand=True, padx=20, pady=20)

# Left frame for login form
form_frame = tk.Frame(main_frame, bg='white')
form_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

# Right frame for image
image_frame = tk.Frame(main_frame, bg='white', width=220)
image_frame.grid(row=0, column=1, sticky="nsew")

# Configure grid weights so form_frame expands, image_frame stays fixed width
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=0)
main_frame.rowconfigure(0, weight=1)

# Title
title = tk.Label(form_frame, text="Login", font=("Helvetica", 20, "bold"), bg='white', fg='#007AFF')
title.pack(pady=(0, 20))

# Username
username_label = tk.Label(form_frame, text="Username", font=("Helvetica", 12), bg='white')
username_label.pack(anchor='w')
username_entry = tk.Entry(
    form_frame, font=("Helvetica", 12), bd=0,
    highlightthickness=1, highlightbackground="black", highlightcolor="black",
    bg="white", fg="black", relief="flat"
)
username_entry.pack(fill='x', pady=(0, 10))

# Password
password_label = tk.Label(form_frame, text="Password", font=("Helvetica", 12), bg='white')
password_label.pack(anchor='w')
password_entry = tk.Entry(
    form_frame, show="*", font=("Helvetica", 12), bd=0,
    highlightthickness=1, highlightbackground="black", highlightcolor="black",
    bg="white", fg="black", relief="flat"
)
password_entry.pack(fill='x', pady=(0, 20))

# Login validation
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Login button
login_button = tk.Button(
    form_frame, text="Login", font=("Helvetica", 12),
    bg="#007AFF", fg="white", activebackground="#005BBB", relief="flat", command=validate_login
)
login_button.pack(fill='x')

# Load and place the image
try:
    img = Image.open("icons/menu/logo_mysignals.png").resize((200, 200), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(image_frame, image=img_tk, bg='white')
    img_label.image = img_tk
    img_label.pack(expand=True)
except FileNotFoundError:
    img_label = tk.Label(image_frame, text="Image\nNot Found", bg='white', fg='red', font=('Helvetica', 12, 'bold'))
    img_label.pack(expand=True)

root.mainloop()
