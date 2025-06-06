# Text-Encryption-Tools
This project is a Python-based Text Encryption Tool that enables secure encryption and decryption of messages using three popular cryptographic algorithms: 1. AES (Advanced Encryption Standard) 2. DES (Data Encryption Standard)  3. RSA (Rivest-Shamir-Adleman)


# 🔐 Text Encryption Tool using AES, DES, and RSA

## 📘 Overview

This project is a Python-based **Text Encryption Tool** that enables secure encryption and decryption of messages using three popular cryptographic algorithms:

* **AES (Advanced Encryption Standard)**
* **DES (Data Encryption Standard)**
* **RSA (Rivest-Shamir-Adleman)**

It helps users understand and practice data protection with both **symmetric** and **asymmetric** encryption methods.

---

## ⚙️ Features

* Encrypt and decrypt text using AES, DES, or RSA
* CLI-based interaction
* Secure base64 encoding for safe transport/storage
* Modular Python structure

---

## 🛠️ Technologies Used

* Python 3.x
* [PyCryptodome](https://pypi.org/project/pycryptodome/) (for AES and DES)
* [rsa](https://pypi.org/project/rsa/) library (for RSA)

---

## 📂 Project Structure

```
text_encryption_tool/
├── aes_encryption.py     # AES functions
├── des_encryption.py     # DES functions
├── rsa_encryption.py     # RSA functions
├── main.py               # CLI Interface
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/text-encryption-tool.git
cd text-encryption-tool
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the application:**

```bash
python main.py
```

---

## 📌 Usage Example

```
=== Text Encryption Tool ===
Select Algorithm:
1. AES
2. DES
3. RSA
Enter choice (1/2/3): 1
Encrypt or Decrypt (e/d): e
Enter key: mysecretkey
Enter text to encrypt: hello world

Result: XyzBase64EncryptedString==
```

---

## 🧠 Concepts Covered

* Symmetric vs Asymmetric encryption
* Padding in block ciphers
* Secure key handling
* Base64 encoding for binary data

---

## 🧩 Future Enhancements

* GUI with Tkinter
* File encryption support
* Key generation/export interface
* Add hashing (SHA-256) for integrity

---
