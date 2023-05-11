def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            ciphered_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += ciphered_char
        else:
            result += char
    return result


def caesar_decipher(ciphertext, shift):
    result = ''
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            deciphered_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += deciphered_char
        else:
            result += char
    return result


plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)

decrypted_text = caesar_decipher(ciphertext, shift)
print("Decrypted text:", decrypted_text)

ww = input(print("Press enter to terminate"))