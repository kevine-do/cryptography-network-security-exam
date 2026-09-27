import hashlib
import re


def calculate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


print("Python Security Toolkit")
print("------------------------")

sample_text = "sample-data"
print("SHA-256:", calculate_sha256(sample_text))

sample_password = "Example123!"
print("Password strength:", check_password_strength(sample_password))