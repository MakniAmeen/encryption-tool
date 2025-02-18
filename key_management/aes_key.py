# Save the key to a file
def save_key(key, filename="key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the key from a file
def load_key(filename="key.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()