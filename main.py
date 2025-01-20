import sys
import os
from encryption.aes import aes_encrypt, aes_decrypt
from encryption.rsa import rsa_encrypt, rsa_decrypt
from key_management.aes_key import save_key, load_key
from key_management.rsa_key import (
    generate_rsa_key_pair,
    save_private_key,
    save_public_key,
    load_private_key,
    load_public_key,
)

def main():
    if len(sys.argv) < 5:
        print("Usage: python main.py <aes/rsa> <encrypt/decrypt> <input_file> <output_file>")
        return

    method = sys.argv[1]  # aes or rsa
    operation = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]

    with open(input_file, "rb") as f:
        data = f.read()

    if method == "aes":
        if operation == "encrypt":
            key = os.urandom(16)  # Generate AES key
            save_key(key)  # Save the AES key
            encrypted_data = aes_encrypt(data, key)
            with open(output_file, "wb") as f:
                f.write(encrypted_data)
            print(f"File encrypted to {output_file} using AES and key saved to key.key")
        elif operation == "decrypt":
            key = load_key()  # Load AES key
            decrypted_data = aes_decrypt(data, key)
            with open(output_file, "wb") as f:
                f.write(decrypted_data)
            print(f"File decrypted to {output_file} using AES")
        else:
            print("Invalid operation for AES. Use 'encrypt' or 'decrypt'.")

    elif method == "rsa":
        if operation == "encrypt":
            private_key, public_key = generate_rsa_key_pair()
            save_private_key(private_key)
            save_public_key(public_key)
            encrypted_data = rsa_encrypt(data, public_key)
            with open(output_file, "wb") as f:
                f.write(encrypted_data)
            print(f"File encrypted to {output_file} using RSA and keys saved to private_key.pem/public_key.pem")
        elif operation == "decrypt":
            private_key = load_private_key()
            decrypted_data = rsa_decrypt(data, private_key)
            with open(output_file, "wb") as f:
                f.write(decrypted_data)
            print(f"File decrypted to {output_file} using RSA")
        else:
            print("Invalid operation for RSA. Use 'encrypt' or 'decrypt'.")

    else:
        print("Invalid method. Use 'aes' or 'rsa'.")

if __name__ == "__main__":
    main()
