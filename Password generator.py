import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

app = tk.Tk()
app.title("Password Generator")
app.geometry("300x200")

tk.Label(app, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

tk.Button(app, text="Generate Password", command=generate_password).pack(pady=5)
result_label = tk.Label(app, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

app.mainloop()
