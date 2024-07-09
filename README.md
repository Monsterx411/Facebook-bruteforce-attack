# Facebook Brute Force Tool

## Introduction

This tool is intended for educational purposes to demonstrate brute force attacks on Facebook accounts. It is designed to help users understand the risks associated with weak passwords and the importance of strong security measures.

**Disclaimer:** This tool is intended for educational purposes only. The author is not responsible for any illegal use of this tool.

## Prerequisites

Before using this tool, make sure you have the following installed on your system:

- Python 3.x
- `mechanize` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Ahmed-Massoud/Facebook-bruteforce-attack.git
    cd Facebook-bruteforce-attack
    ```

2. Install the required Python library:

    ```sh
    pip install mechanize
    ```

## Usage

1. Run the script:

    ```sh
    python massoud.py
    ```

2. Follow the on-screen instructions:

    - Enter the target Facebook account's email or phone number.
    - Provide the path to the password file containing a list of potential passwords.

    Example of the password file format:

    ```txt
    password123
    qwerty
    letmein
    123456
    ```

3. The tool will attempt to log in to the Facebook account using each password from the provided file.

## Important Notes

- Ensure you have permission to perform brute force attacks on the target account.
- Use this tool responsibly and only for educational or authorized security testing purposes.

## Disclaimer

This tool is intended for educational purposes only. The author is not responsible for any illegal use of this tool. By using this tool, you agree to use it responsibly and ethically.

## Passwords File

I have provided a `passwords.txt` file that contains a list of the most common passwords. This file can be used to test the brute force attack functionality of the tool. Make sure to use it responsibly and only for educational or authorized security testing purposes.
