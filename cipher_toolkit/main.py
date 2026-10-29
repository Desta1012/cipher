
from algorithms import playfair, hill, vigenere


def display_menu():
    print("\n" + "=" * 45)
    print("          CIPHER TOOLKIT PYTHON")
    print("=" * 45)
    print("1. Playfair Cipher")
    print("2. Hill Cipher")
    print("3. Vigenere Cipher")
    print("4. Keluar")
    print("=" * 45)


def select_algorithm(choice):
    algorithms = {
        "1": ("Playfair Cipher", playfair),
        "2": ("Hill Cipher", hill),
        "3": ("Vigenere Cipher", vigenere),
    }

    return algorithms.get(choice)


def run_cipher(name, algorithm):
    print(f"\n--- {name} ---")
    print("1. Enkripsi")
    print("2. Dekripsi")

    operation = input("Pilih operasi (1/2): ").strip()

    if operation not in ("1", "2"):
        print("Pilihan operasi tidak valid.")
        return

    text = input(
        "Masukkan plaintext: " if operation == "1"
        else "Masukkan ciphertext: "
    ).strip()

    key = input("Masukkan kunci: ").strip()

    if not text:
        print("Teks tidak boleh kosong.")
        return

    try:
        if operation == "1":
            result = algorithm.encrypt(text, key)
            label = "Ciphertext"
        else:
            result = algorithm.decrypt(text, key)
            label = "Hasil dekripsi"

        print("\n" + "-" * 45)
        print(f"Algoritma : {name}")
        print(f"{label} : {result}")
        print("-" * 45)

    except ValueError as error:
        print(f"\nInput tidak valid: {error}")


def main():
    while True:
        display_menu()
        choice = input("Pilih algoritma (1-4): ").strip()

        if choice == "4":
            print("\nTerima kasih telah menggunakan Cipher Toolkit!")
            break

        selected = select_algorithm(choice)

        if selected is None:
            print("Pilihan tidak valid. Silakan pilih 1 sampai 4.")
            continue

        name, algorithm = selected
        run_cipher(name, algorithm)


if __name__ == "__main__":
    main()
