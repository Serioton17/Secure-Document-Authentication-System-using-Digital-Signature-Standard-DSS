import tkinter as tk
from tkinter import messagebox
from Crypto.PublicKey import DSA # type: ignore
import os

def generate_keys():
    username = entry.get()
    if not username:
        messagebox.showwarning("Input Error", "Enter a username.")
        return
    
    key = DSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    os.makedirs("keys", exist_ok=True)

    with open(f"keys/{username}_private.pem", "wb") as f:
        f.write(private_key)
    with open(f"keys/{username}_public.pem", "wb") as f:
        f.write(public_key)

    messagebox.showinfo("Success", f"Keys generated for {username}!")

root = tk.Tk()
root.title("Key Generator")

tk.Label(root, text="Username:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate Keys", command=generate_keys).pack()
root.mainloop()