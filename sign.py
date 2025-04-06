import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
import os
import datetime

def sign_file():
    username = entry.get()
    if not username:
        messagebox.showwarning("Input Error", "Enter a username.")
        return

    filepath = filedialog.askopenfilename(title="Select File to Sign")
    if not filepath:
        return

    try:
        with open(f"keys/{username}_private.pem", "rb") as f:
            private_key = DSA.import_key(f.read())
    except FileNotFoundError:
        messagebox.showerror("Error", "Private key not found.")
        return

    with open(filepath, "rb") as f:
        data = f.read()

    hash_obj = SHA256.new(data)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)

    os.makedirs("signatures", exist_ok=True)
    sig_path = f"signatures/{username}_{os.path.basename(filepath)}.sig"
    with open(sig_path, "wb") as f:
        f.write(signature)

    with open("metadata.csv", "a") as log:
        log.write(f"{username},{filepath},{hash_obj.hexdigest()},{sig_path},{datetime.datetime.now()}\n")

    messagebox.showinfo("Success", f"File signed and saved at:\n{sig_path}")

root = tk.Tk()
root.title("Sign File")

tk.Label(root, text="Username:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Sign File", command=sign_file).pack()
root.mainloop()
