import random
import pyperclip
import string
import tkinter as tk
from tkinter import ttk

# Function for generating a random password
def generate_password():
    password_length = var_length.get()
    password_strength = var_strength.get()

    if password_strength == 1:
        # Low strength (only lowercase letters)
        password_chars = string.ascii_lowercase
    elif password_strength == 2:
        # Medium strength (lowercase + uppercase letters)
        password_chars = string.ascii_letters
    elif password_strength == 3:
        # Strong strength (letters + digits + symbols)
        password_chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(password_chars) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function for copying the generated password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)

# Create GUI window
root = tk.Tk()
root.title("Password Generator")
root.iconbitmap("C:/Users/LENOVO/Downloads/iconn.ico")

# Label for displaying generated password
password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0, padx=10, pady=10)

# Entry widget to display the generated password
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Frame for strength selection
strength_frame = tk.Frame(root)
strength_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Strength selection radio buttons
var_strength = tk.IntVar(value=2)  # Default to medium strength
tk.Radiobutton(strength_frame, text="Low", variable=var_strength, value=1).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(strength_frame, text="Medium", variable=var_strength, value=2).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(strength_frame, text="Strong", variable=var_strength, value=3).pack(side=tk.LEFT, padx=5)

# Frame for password length selection
length_frame = tk.Frame(root)
length_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Label and Combobox for selecting password length
length_label = tk.Label(length_frame, text="Length:")
length_label.pack(side=tk.LEFT, padx=5)
var_length = tk.IntVar(value=8)  # Default length
length_combobox = ttk.Combobox(length_frame, textvariable=var_length, values=list(range(8, 33)), width=5)
length_combobox.pack(side=tk.LEFT, padx=5)

# Button for generating password
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=3, column=0, pady=10)

# Button for copying password to clipboard
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=3, column=1, pady=10, padx=10)

# Start the GUI event loop
root.mainloop()
