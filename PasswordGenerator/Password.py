import secrets
import string


def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))