# Caesar Cipher Program


def encrypt(text, shift):
    result = ""
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetical characters remain the same
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Reusing encrypt function with negative shift


def caesar_cipher():
    print("Caesar Cipher Program")
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter choice (1 or 2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice. Existing program.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == "1":
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == "2":
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")


# Run the program
if __name__ == "__main__":
    caesar_cipher()
