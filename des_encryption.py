# des_encryption.py
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    pad_len = 8 - len(text) % 8
    return text + chr(pad_len) * pad_len

def unpad(text):
    return text[:-ord(text[-1])]

def des_encrypt(plain_text, key):
    key = key.ljust(8)[:8].encode()
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(plain_text).encode())
    return base64.b64encode(iv + encrypted).decode()

def des_decrypt(cipher_text, key):
    raw = base64.b64decode(cipher_text)
    key = key.ljust(8)[:8].encode()
    iv = raw[:8]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = cipher.decrypt(raw[8:])
    return unpad(decrypted.decode())
