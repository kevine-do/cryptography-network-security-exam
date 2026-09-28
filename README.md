# \# Cryptography and Network Security Exam

# 

# \## Project Overview

# 

# This project demonstrates basic cryptography, file integrity checking, password security, and network security controls using Python and an authorised laboratory environment.

# 

# \## Project Structure

# 

# ```text

# cryptography-network-security-exam/

# ├── src/

# │   └── security\_toolkit.py

# ├── tests/

# │   ├── test\_security\_toolkit.py

# │   └── test\_error\_handling.py

# ├── results/

# ├── report/

# ├── risk\_assessment.md

# └── README.md

# ```

# 

# \## Requirements

# 

# \* Python 3

# \* Python package: `cryptography`

# 

# Install the required package:

# 

# ```bash

# python -m pip install cryptography

# ```

# 

# \## Encryption and Decryption

# 

# The security toolkit encrypts the sample student record using Fernet symmetric encryption.

# 

# The encryption key is stored outside the GitHub repository for security.

# 

# Run the toolkit:

# 

# ```bash

# python src\\security\_toolkit.py

# ```

# 

# The program:

# 

# 1\. Reads the sample student record.

# 2\. Encrypts the file.

# 3\. Saves the encrypted output.

# 4\. Decrypts the encrypted file.

# 5\. Calculates SHA-256 hashes.

# 6\. Verifies that the decrypted file matches the original.

# 7\. Reports the integrity result.

# 

# \## Integrity Verification

# 

# SHA-256 is used to calculate a hash of the file.

# 

# If the file is modified, its SHA-256 hash changes. This allows a modification to be detected.

# 

# \## Testing

# 

# Run the main tests:

# 

# ```bash

# python -m unittest tests\\test\_security\_toolkit.py

# ```

# 

# Run the error-handling test:

# 

# ```bash

# python -m unittest tests\\test\_error\_handling.py

# ```

# 

# The tests verify SHA-256 hashing, password strength checking, and handling of missing files.

# 

# \## Security

# 

# Only sample data is used in this project.

# 

# Do not upload:

# 

# \* Encryption keys

# \* Real student records

# \* Real passwords

# \* Other sensitive information

# 

# The encryption key is stored outside the project repository.

# 

# \## Network Traffic Filtering

# 

# Network traffic filtering is performed in an authorised laboratory environment using firewall rules. The filtering configuration and test results are documented separately in `filter\_tests.md`.

# 

# \## Reproducibility

# 

# To reproduce the Python tests:

# 

# ```bash

# python -m unittest tests\\test\_security\_toolkit.py

# python -m unittest tests\\test\_error\_handling.py

# ```

# 

# To run the security toolkit:

# 

# ```bash

# python src\\security\_toolkit.py

# ```



