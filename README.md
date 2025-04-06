# 🛡️ Secure Document Authentication System using Digital Signature Standard (DSS)

**Secure Document Authentication System (DSS)** is a Python-based desktop project that allows users to digitally sign text documents and verify their authenticity using the **Digital Signature Algorithm (DSA)**. This ensures that the document has not been tampered with and originates from a verified sender.

---

## 🎯 Objectives

- Implement a cryptographic signing and verification system using **Digital Signature Standard (DSS)**.
- Provide secure generation, storage, and use of **DSA key pairs**.
- Detect any modification in signed documents using robust hash-based validation.
- Maintain logs for auditing and verification purposes.

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

### 🔧 Prerequisites

- Install Python 3.x
- Install dependencies:
```bash
pip install pycryptodome
🛠️ Steps to Use:
1. Generate Keys:
bash
Copy
Edit
python keygen.py
Prompts for username and saves private/public keys in /keys.

2. Sign a Document:
bash
Copy
Edit
python sign.py
Select the document and user. The signature is saved to /signatures.

3. Verify a Document:
bash
Copy
Edit
python verify.py
Select the document, signature, and public key. Displays verification result.

🔐 Features
✔️ User-specific DSA key generation

✔️ SHA-256 based document hashing

✔️ Signature verification using public keys

✔️ Tamper detection through failed verification

✔️ Detailed logging of all cryptographic actions

🎥 Demo
📌 Add your demo link here once uploaded


📚 References
PyCryptodome Documentation

NIST DSS Standard (FIPS 186)

Wikipedia – Digital Signature Algorithm


## Demo

Insert gif or link to demo

