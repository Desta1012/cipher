
import string

ALPHABET = string.ascii_uppercase


def clean_text(text):
    """Mengambil hanya huruf A-Z dari teks."""
    return "".join(
        char for char in text.upper()
        if char in ALPHABET
    )


def clean_key(key):
    """Memvalidasi dan membersihkan kata kunci."""
    key = clean_text(key)

    if not key:
        raise ValueError(
            "Kunci harus berisi minimal satu huruf A-Z."
        )

    return key


def encrypt(plaintext, key):
    """Mengenkripsi plaintext dengan Vigenere Cipher."""
    plaintext = clean_text(plaintext)
    key = clean_key(key)

    result = []

    for i, char in enumerate(plaintext):
        plain_value = ord(char) - ord("A")
        key_value = ord(key[i % len(key)]) - ord("A")

        cipher_value = (plain_value + key_value) % 26
        result.append(chr(cipher_value + ord("A")))

    return "".join(result)


def decrypt(ciphertext, key):
    """Mendekripsi ciphertext dengan Vigenere Cipher."""
    ciphertext = clean_text(ciphertext)
    key = clean_key(key)

    result = []

    for i, char in enumerate(ciphertext):
        cipher_value = ord(char) - ord("A")
        key_value = ord(key[i % len(key)]) - ord("A")

        plain_value = (cipher_value - key_value) % 26
        result.append(chr(plain_value + ord("A")))

    return "".join(result)
