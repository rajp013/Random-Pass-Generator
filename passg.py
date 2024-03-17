import string
import secrets
import tkinter as tk
from tkinter import ttk, messagebox


def generate_strongest_password(length=20):
    if length < 12:
        messagebox.showerror("Error", "Password length should be at least 12 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    strong_characters = string.ascii_letters + string.digits + "!@#$%^&*()_-+=<>?/{}[]~"

    password = [secrets.choice(string.ascii_lowercase),
                secrets.choice(string.ascii_uppercase),
                secrets.choice(string.digits),
                secrets.choice(string.punctuation)]

    password += [secrets.choice(strong_characters) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)

    final_password = ''.join(password)
    return final_password


def generate_password_button():
    password_length = int(password_length_entry.get())
    generated_password = generate_strongest_password(password_length)
    generated_password_label.config(text="Generated Password: " + generated_password)
    copy_button.config(state=tk.NORMAL)  # Enable the "Copy" button


def copy_password():
    generated_password = generated_password_label.cget("text")[19:]  # Extract password from label text
    window.clipboard_clear()  # Clear clipboard contents
    window.clipboard_append(generated_password)  # Append password to clipboard
    window.update()  # Update clipboard


# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Styling
style = ttk.Style()
style.theme_use("default")  # Change the theme to "radiance"

# Create widgets
password_length_label = ttk.Label(window, text="Enter Password Length:")
password_length_entry = ttk.Entry(window)
generate_button = ttk.Button(window, text="Generate Password", command=generate_password_button)
generated_password_label = ttk.Label(window, text="Generated Password: ")
copy_button = ttk.Button(window, text="Copy", state=tk.DISABLED, command=copy_password)

# Organize widgets using grid layout
password_length_label.grid(row=0, column=0, padx=10, pady=10)
password_length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
generated_password_label.grid(row=2, columnspan=2, padx=10, pady=10)
copy_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
