# Cryptography and Network Security Exam

## Project Overview

This project demonstrates basic cryptography, file integrity checking, password security, and network security controls using Python and an authorised laboratory environment.

Only sample student data was used. No real student records, passwords, or encryption keys are stored in the repository.

## Project Structure

```text
cryptography-network-security-exam/
├── src/
│   └── security_toolkit.py
├── tests/
│   ├── test_security_toolkit.py
│   └── test_error_handling.py
├── results/
├── report/
│   ├── technical_report.tex
│   └── Cryptography_and_Network_Security_Exam.pdf
├── risk_assessment.md
├── filter_tests.md
└── README.md
```

## Requirements

* Python 3
* Python package: `cryptography`
* An authorised laboratory environment for firewall testing

## Installation

Install the required Python package:

```bash
python -m pip install cryptography
```

## Encryption and Decryption

The security toolkit encrypts the sample student record using Fernet symmetric encryption.

The encryption key is stored outside the GitHub repository for security.

Run the toolkit:

```bash
python src\security_toolkit.py
```

The program:

1. Reads the sample student record.
2. Encrypts the file.
3. Saves the encrypted output.
4. Decrypts the encrypted file.
5. Calculates SHA-256 hashes.
6. Verifies that the decrypted file matches the original.
7. Reports the integrity result.
8. Handles missing files and invalid inputs.

## Integrity Verification

SHA-256 is used to calculate a hash of the file.

If the file is modified, its SHA-256 hash changes. This allows a modification to be detected.

The demonstrated results included:

```text
Contents match: True
Integrity check: PASS
Modified file detected: True
```

## Testing

Python's built-in `unittest` framework was used.

Run the main tests:

```bash
python -m unittest tests\test_security_toolkit.py
```

Run the error-handling test:

```bash
python -m unittest tests\test_error_handling.py
```

The tests verify:

* SHA-256 hashing
* Password strength checking
* Missing-file error handling

## Network Traffic Filtering

Network traffic filtering was tested in an authorised laboratory environment using UFW (Uncomplicated Firewall).

The laboratory service used for testing was a Python HTTP server on TCP port 8080.

The firewall configuration and test results are documented in:

```text
filter_tests.md
```

The documented tests include:

* One permitted TCP connection.
* One blocked connection to TCP port 8080.
* One blocked connection to TCP port 8081.

## Risk Assessment

The security risks, vulnerabilities, consequences, risk rankings, and recommended controls are documented in:

```text
risk_assessment.md
```

## Technical Report

The complete technical report is available in the `report` directory in both formats:

* `technical_report.tex`
* `Cryptography_and_Network_Security_Exam.pdf`

## Security

Do not upload or share:

* Encryption keys
* Real student records
* Real passwords
* Other confidential information

The encryption key used by the project is stored outside the repository.

## Reproducibility

To reproduce the Python tests:

```bash
python -m unittest tests\test_security_toolkit.py
python -m unittest tests\test_error_handling.py
```

To run the security toolkit:

```bash
python src\security_toolkit.py
```

Firewall test commands and results can be reproduced in an authorised laboratory environment using the procedures documented in `filter_tests.md`.

## Repository

GitHub repository:

https://github.com/kevine-do/cryptography-network-security-exam
