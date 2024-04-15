# ALL CODE COPYRIGHT SING DEVELOPMENTS. PLEASE ASK THE OWNER TO DISTRUBUTE!

import random
import string
import tkinter as tk
from tkinter import ttk

length = 10
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

root = tk.Tk()
root.title("Password Generator")

options_frame = tk.Frame(root)
options_frame.pack(padx=10, pady=10)

lower_var = tk.BooleanVar()
lower_var.set(True)
lower_check = tk.Checkbutton(options_frame, text="Lowercase Letters", variable=lower_var)
lower_check.grid(row=0, column=0, sticky="w")

upper_var = tk.BooleanVar()
upper_var.set(True)
upper_check = tk.Checkbutton(options_frame, text="Uppercase Letters", variable=upper_var)
upper_check.grid(row=1, column=0, sticky="w")

digit_var = tk.BooleanVar()
digit_var.set(True)
digit_check = tk.Checkbutton(options_frame, text="Numbers", variable=digit_var)
digit_check.grid(row=2, column=0, sticky="w")

symbol_var = tk.BooleanVar()
symbol_var.set(True)
symbol_check = tk.Checkbutton(options_frame, text="Punctuation", variable=symbol_var)
symbol_check.grid(row=3, column=0, sticky="w")

length_label = tk.Label(options_frame, text="Length:")
length_label.grid(row=4, column=0, sticky="w")

length_entry = tk.Entry(options_frame)
length_entry.insert(0, str(length))
length_entry.grid(row=4, column=1)

def generate_password():
    lower = lower_var.get()
    upper = upper_var.get()
    digit = digit_var.get()
    symbol = symbol_var.get()
    length = int(length_entry.get())

    pool = ""

    if lower:
        pool += lowercase
    if upper:
        pool += uppercase
    if digit:
        pool += digits
    if symbol:
        pool += symbols

    if pool == "":
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        error_window.geometry("200x100")

        error_label = tk.Label(error_window, text="ERROR", fg="red", font=("Arial", 20))
        error_label.pack(padx=10, pady=10)

        close_button = tk.Button(error_window, text="Close", command=error_window.destroy)
        close_button.pack(pady=10)

    else:
        password = "".join(random.choices(pool, k=length))
        password_window = tk.Toplevel(root)
        password_window.title("Your Password")
        
        width = max(200, 10 * length)
        height = 100 
        password_window.geometry(f"{width}x{height}")

        password_label = tk.Label(password_window, text=password, font=("Arial", 20))
        password_label.pack(padx=10, pady=10)

        def copy_password():
            root.clipboard_clear()
            root.clipboard_append(password)

        copy_button = tk.Button(password_window, text="Copy Text", command=copy_password)
        copy_button.pack(side="left", padx=10, pady=10)

        close_button = tk.Button(password_window, text="Close", command=password_window.destroy)
        close_button.pack(side="right", padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=("Arial", 15), foreground="green")

root.mainloop()
