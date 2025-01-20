# Encryption Tool

A Python-based encryption and decryption tool that supports both AES (Advanced Encryption Standard) and RSA (Rivest-Shamir-Adleman) algorithms. This project provides a simple command-line interface for securing files.

## Features
- **AES Encryption and Decryption**: Symmetric encryption with key management.
- **RSA Encryption and Decryption**: Asymmetric encryption with public-private key management.
- **Key Storage**: Keys are securely saved and loaded from files.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
    - [AES Encryption and Decryption](#aes-encryption-and-decryption)
    - [RSA Encryption and Decryption](#rsa-encryption-and-decryption)
3. [Project Structure](#project-structure)
4. [Contributing](#contributing)
5. [License](#license)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MakniAmeen/encryption-tool.git
   cd encryption-tool
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### General Syntax
```bash
python main.py <aes/rsa> <encrypt/decrypt> <input_file> <output_file>
```

### AES Encryption and Decryption

- **Encrypt a File**:
  ```bash
  python main.py aes encrypt input.txt encrypted_aes.enc
  ```
  The AES key will be saved in `key.key`.

- **Decrypt a File**:
  ```bash
  python main.py aes decrypt encrypted_aes.enc decrypted_aes.txt
  ```
  The key from `key.key` will be used.

### RSA Encryption and Decryption

- **Encrypt a File**:
  ```bash
  python main.py rsa encrypt input.txt encrypted_rsa.enc
  ```
  RSA keys will be saved in `private_key.pem` and `public_key.pem`.

- **Decrypt a File**:
  ```bash
  python main.py rsa decrypt encrypted_rsa.enc decrypted_rsa.txt
  ```
  The private key from `private_key.pem` will be used.

---

## Project Structure

```
encryption-tool/
│
├── encryption/
│   ├── aes.py        # AES encryption and decryption
│   ├── rsa.py        # RSA encryption and decryption
│
├── key_management/
│   ├── aes_key.py    # Manage AES keys
│   ├── rsa_key.py    # Manage RSA keys
│
├── main.py           # Main script for CLI
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, feel free to reach out:
- **GitHub**: [MakniAmeen](https://github.com/MakniAmeen)
- **Email**: [amin.makni@outlook.fr](mailto:amin.makni@outlook.fr)
