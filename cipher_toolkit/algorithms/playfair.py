
import string


ALPHABET = string.ascii_uppercase.replace("J", "")


def create_matrix(key):
    """Membuat matriks Playfair 5x5 berdasarkan kata kunci."""
    key = "".join(
        char for char in key.upper()
        if char in string.ascii_uppercase
    ).replace("J", "I")

    # Hilangkan huruf yang berulang pada kunci.
    unique_chars = []
    for char in key + ALPHABET:
        if char not in unique_chars:
            unique_chars.append(char)

    return [
        unique_chars[i:i + 5]
        for i in range(0, 25, 5)
    ]


def prepare_text(text):
    """Membersihkan teks dan membentuk pasangan huruf."""
    text = "".join(
        char for char in text.upper()
        if char in string.ascii_uppercase
    ).replace("J", "I")

    pairs = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 >= len(text):
            second = "X" if first != "X" else "Q"
            i += 1
        elif text[i] == text[i + 1]:
            second = "X" if first != "X" else "Q"
            i += 1
        else:
            second = text[i + 1]
            i += 2

        pairs.append(first + second)

    return pairs


def transform_pair(pair, matrix, mode):
    """Mengenkripsi atau mendekripsi satu pasangan huruf."""
    positions = {
        matrix[row][col]: (row, col)
        for row in range(5)
        for col in range(5)
    }

    a, b = pair
    row_a, col_a = positions[a]
    row_b, col_b = positions[b]

    if row_a == row_b:
        shift = 1 if mode == "encrypt" else -1
        return (
            matrix[row_a][(col_a + shift) % 5]
            + matrix[row_b][(col_b + shift) % 5]
        )

    if col_a == col_b:
        shift = 1 if mode == "encrypt" else -1
        return (
            matrix[(row_a + shift) % 5][col_a]
            + matrix[(row_b + shift) % 5][col_b]
        )

    # Persegi panjang: tukar posisi kolom.
    return matrix[row_a][col_b] + matrix[row_b][col_a]


def encrypt(plaintext, key):
    """Mengenkripsi plaintext menggunakan Playfair Cipher."""
    if not key.strip():
        raise ValueError("Kunci tidak boleh kosong.")

    matrix = create_matrix(key)
    pairs = prepare_text(plaintext)

    return "".join(
        transform_pair(pair, matrix, "encrypt")
        for pair in pairs
    )


def decrypt(ciphertext, key):
    """Mendekripsi ciphertext menggunakan Playfair Cipher."""
    if not key.strip():
        raise ValueError("Kunci tidak boleh kosong.")

    text = "".join(
        char for char in ciphertext.upper()
        if char in string.ascii_uppercase
    ).replace("J", "I")

    if len(text) % 2 != 0:
        raise ValueError(
            "Ciphertext Playfair harus memiliki jumlah huruf genap."
        )

    matrix = create_matrix(key)
    pairs = [
        text[i:i + 2]
        for i in range(0, len(text), 2)
    ]

    return "".join(
        transform_pair(pair, matrix, "decrypt")
        for pair in pairs
    )
