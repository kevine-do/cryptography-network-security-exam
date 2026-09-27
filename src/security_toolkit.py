import hashlib
import os
from cryptography.fernet import Fernet


KEY_FILE = r"C:\Users\kabal\security_exam_key.key"


def load_key():
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key not found.")
    
    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_file(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found.")

    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError("Encrypted file not found.")

    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)


def calculate_sha256(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError("File not found.")

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for data in iter(lambda: file.read(4096), b""):
            sha256.update(data)

    return sha256.hexdigest()


def verify_integrity(filename, original_hash):
    current_hash = calculate_sha256(filename)
    return current_hash == original_hash


if __name__ == "__main__":
    print("Python Security Toolkit")
    print("------------------------")

    try:
        original_file = "sample_student_record.txt"
        encrypted_file = "results/encrypted_student_record.bin"
        decrypted_file = "results/decrypted_student_record.txt"

        os.makedirs("results", exist_ok=True)

        print("Original SHA-256:", calculate_sha256(original_file))

        encrypt_file(original_file, encrypted_file)
        print("File encrypted successfully.")

        decrypt_file(encrypted_file, decrypted_file)
        print("File decrypted successfully.")

        original_hash = calculate_sha256(original_file)
        decrypted_hash = calculate_sha256(decrypted_file)

        print("Decrypted SHA-256:", decrypted_hash)
        print("Contents match:", original_hash == decrypted_hash)

        print(
            "Integrity check:",
            "PASS" if verify_integrity(original_file, original_hash) else "FAIL"
        )

    except FileNotFoundError as error:
        print("File error:", error)
    except (ValueError, Exception) as error:
        print("Invalid input or other error:", error)