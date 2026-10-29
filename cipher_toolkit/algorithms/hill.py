
import math
import string

ALPHABET = string.ascii_uppercase


def validate_key(key):
    """Memastikan kunci Hill Cipher berupa matriks 2x2 yang valid."""
    if len(key) != 4 or not key.isalpha() or not key.isascii():
        raise ValueError(
            "Kunci harus terdiri dari 4 huruf, contoh: HILL."
        )

    values = [ord(char.upper()) - ord("A") for char in key]
    a, b, c, d = values

    determinant = (a * d - b * c) % 26

    if math.gcd(determinant, 26) != 1:
        raise ValueError(
            "Kunci tidak valid. Determinan matriks harus relatif prima "
            "terhadap 26. Coba kunci: HILL."
        )

    return [[a, b], [c, d]]


def mod_inverse(number, modulus):
    """Mencari invers perkalian modulo."""
    for i in range(1, modulus):
        if (number * i) % modulus == 1:
            return i

    raise ValueError("Invers modulo tidak ditemukan.")


def prepare_text(text):
    """Mengambil huruf A-Z dan mengisi X jika panjangnya ganjil."""
    text = "".join(
        char for char in text.upper()
        if char in ALPHABET
    )

    if len(text) % 2 != 0:
        text += "X"

    return text


def encrypt(plaintext, key):
    """Enkripsi Hill Cipher menggunakan matriks kunci 2x2."""
    matrix = validate_key(key)
    text = prepare_text(plaintext)
    result = []

    for i in range(0, len(text), 2):
        x = ord(text[i]) - ord("A")
        y = ord(text[i + 1]) - ord("A")

        first = (matrix[0][0] * x + matrix[0][1] * y) % 26
        second = (matrix[1][0] * x + matrix[1][1] * y) % 26

        result.append(chr(first + ord("A")))
        result.append(chr(second + ord("A")))

    return "".join(result)


def decrypt(ciphertext, key):
    """Dekripsi Hill Cipher menggunakan invers matriks modulo 26."""
    matrix = validate_key(key)
    text = "".join(
        char for char in ciphertext.upper()
        if char in ALPHABET
    )

    if len(text) % 2 != 0:
        raise ValueError(
            "Ciphertext Hill harus memiliki jumlah huruf genap."
        )

    a, b = matrix[0]
    c, d = matrix[1]

    determinant = (a * d - b * c) % 26
    inverse_det = mod_inverse(determinant, 26)

    # Adjugat matriks dikalikan invers determinan modulo 26.
    inverse_matrix = [
        [(d * inverse_det) % 26, (-b * inverse_det) % 26],
        [(-c * inverse_det) % 26, (a * inverse_det) % 26],
    ]

    result = []

    for i in range(0, len(text), 2):
        x = ord(text[i]) - ord("A")
        y = ord(text[i + 1]) - ord("A")

        first = (
            inverse_matrix[0][0] * x
            + inverse_matrix[0][1] * y
        ) % 26

        second = (
            inverse_matrix[1][0] * x
            + inverse_matrix[1][1] * y
        ) % 26

        result.append(chr(first + ord("A")))
        result.append(chr(second + ord("A")))

    return "".join(result)
