# 🛡️ Secure Document Authentication System using Digital Signature Standard (DSS)

**Secure Document Authentication System (DSS)** is a Python-based desktop project that allows users to digitally sign text documents and verify their authenticity using the **Digital Signature Algorithm (DSA)**. This ensures that the document has not been tampered with and originates from a verified sender.

---
## 🎥 Demo

🎥 Watch the demo video here: [Google Drive Link](https://drive.google.com/file/d/1Y2JNtuY1MUS3MA4T4DIIg04BNX-TfC1n/view?usp=sharing)


📁 The demo video has also been uploaded in the [`video`](./video) folder of this repository and is available for [download here](video/mini_project_demo.mp4).

---
## 🎯 Objectives

- To implement the Digital Signature Standard (DSS) using the Digital
Signature Algorithm (DSA).
- To enable secure generation of public and private key pairs for individual
users.
- To provide functionality for signing and verifying files.
- To ensure detection of tampered or modified documents.

---
## 🧰 🔐 Features
✔️ User-specific DSA key generation

✔️ SHA-256 based document hashing

✔️ Signature verification using public keys

✔️ Tamper detection through failed verification

---
## 📁 File Structure

| Path / File             | Description                                         |
|-------------------------|-----------------------------------------------------|
| `keys/`                 | Stores generated public/private key pairs           |
| `docs/`                 | Input documents to be signed or verified            |
| `signatures/`           | Stores generated digital signature files            |
| `metadata.csv`          | Logs signing and verification activity              |
|                         |                                                     |
| `keygen.py`             | Script to generate DSA key pairs                    |
| `sign.py`               | Script to digitally sign text documents             |
| `verify.py`             | Script to verify signatures of text documents       |
| `README.md`             | Project documentation file                          |


---

## 🧰 Tools & Technologies Used

- **Python 3**
- **PyCryptodome** – For cryptographic operations (DSA, SHA-256)
- **hashlib** – For cryptographic hashing
- **CSV** – To log metadata and activity trails
- **OS/Pathlib** – File handling and path operations


---


## 💻 How to Run
## 🔧 Prerequisites
Install Python 3.x

Install dependencies using pip:
pip install pycryptodome

## 🛠️ Steps to Use :
## 1️⃣ Generate Keys

Command to run :
 **python keygen.py**

What it does : Runs the keygen.py script.

Purpose: Prompts the user to enter a username and generates a DSA private/public key pair.

Output:

Saves the keys into the /keys directory as:

username_private.pem (Private Key)

username_public.pem (Public Key)

## 2️⃣ Sign a Document
Command to run:
**python sign.py**

What it does: Runs the sign.py script.

Purpose: Allows the user to select a document and sign it using their private key.

Process:
Hashes the document with SHA-256.
Encrypts the hash with the private key to create a digital signature.

Output:

Stores the signature in the /signatures folder as a .sig file.

## 3️⃣ Verify a Document
Command to run:
**python verify.py**

What it does: Runs the verify.py script.

Purpose: Verifies the authenticity and integrity of the document.

Process: User selects the document, signature file, and the corresponding public key. The script decrypts the signature using the public key and compares it with a new hash of the document.

Output:

✅ If hashes match: "Signature Verified"

❌ If not: "Signature Invalid or Document Tampered"

---
## 📚 References
•	Python hashlib Library

•	NIST Digital Signature Standard (DSS)

•	DSA – Digital Signature Algorithm

•	Digital Signature Standard: Overview – Smid & Branstad (1993)

•	Book: Digital Signature Standard (DSS), FIPS Publication 186-5, NIST
