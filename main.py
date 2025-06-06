# main.py
from aes_encryption import aes_encrypt, aes_decrypt
from des_encryption import des_encrypt, des_decrypt
from rsa_encryption import rsa_encrypt, rsa_decrypt

def menu():
    print("\nChoose Encryption Algorithm:")
    print("1. AES\n2. DES\n3. RSA")
    choice = input("Enter choice: ")
    text = input("Enter text: ")

    if choice == '1':
        key = input("Enter key (any string): ")
        enc = aes_encrypt(text, key)
        dec = aes_decrypt(enc, key)
    elif choice == '2':
        key = input("Enter key (any string): ")
        enc = des_encrypt(text, key)
        dec = des_decrypt(enc, key)
    elif choice == '3':
        enc = rsa_encrypt(text)
        dec = rsa_decrypt(enc)
    else:
        print("Invalid choice.")
        return

    print(f"\nEncrypted: {enc}")
    print(f"Decrypted: {dec}")

if __name__ == '__main__':
    menu()
