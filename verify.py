import os
from tkinter import Tk, Label, Button, filedialog, messagebox
from Crypto.Signature import DSS
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256

def verify_signature():
    file_path = filedialog.askopenfilename(title="Select the ORIGINAL file")
    if not file_path:
        return

    sig_path = filedialog.askopenfilename(title="Select the SIGNATURE file")
    if not sig_path:
        return

    pub_key_path = filedialog.askopenfilename(title="Select the PUBLIC KEY (.pem) file")
    if not pub_key_path:
        return

    try:
        with open(pub_key_path, "rb") as f:
            public_key = DSA.import_key(f.read())

        with open(file_path, "rb") as f:
            data = f.read()

        with open(sig_path, "rb") as f:
            signature = f.read()

        hash_obj = SHA256.new(data)
        verifier = DSS.new(public_key, 'fips-186-3')
        verifier.verify(hash_obj, signature)

        messagebox.showinfo("Result", "✔️ Signature is VALID. File is authentic.")
    except ValueError:
        messagebox.showerror("Result", "❌ Signature is INVALID. File may be tampered.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = Tk()
root.title("Verify Digital Signature")

Label(root, text="🔍 Select files to verify the signature").pack(pady=10)
Button(root, text="Verify Signature", command=verify_signature).pack(pady=5)

root.mainloop()
