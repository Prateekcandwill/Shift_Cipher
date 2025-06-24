def calculate_shift(input_str, key):
    """Calculate a consistent shift based on alphabetic characters and a key."""
    # Sum ASCII values of alphabetic characters in input string
    str_sum = sum(ord(char.lower()) for char in input_str if char.isalpha())
    # Sum ASCII values of alphabetic characters in key
    key_sum = sum(ord(char.lower()) for char in key if char.isalpha())
    # Combine and reduce to 0-25
    return (str_sum + key_sum) % 26 if (str_sum + key_sum) != 0 else 1  # Avoid zero shift

def meme_shift_encrypt_char(ch, shift):
    """Encrypt a single character with the given shift."""
    if ch.islower():
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    elif ch.isupper():
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    return ch

def meme_shift_decrypt_char(ch, shift):
    """Decrypt a single character with the given shift."""
    if ch.islower():
        return chr((ord(ch) - ord('a') - shift + 26) % 26 + ord('a'))
    elif ch.isupper():
        return chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
    return ch

def encrypt_string(input_str, key):
    """Encrypt the input string and return ciphertext with shift."""
    shift = calculate_shift(input_str, key)
    ciphertext = ''.join(meme_shift_encrypt_char(char, shift) for char in input_str)
    # Append shift as a two-digit number for decryption
    return f"{ciphertext}:{shift:02d}"

def decrypt_string(ciphertext_with_shift, key):
    """Decrypt the ciphertext using the provided key and stored shift."""
    try:
        # Split ciphertext and shift
        ciphertext, shift_str = ciphertext_with_shift.rsplit(':', 1)
        shift = int(shift_str)
        # Verify shift using key and decrypted text
        decrypted = ''.join(meme_shift_decrypt_char(char, shift) for char in ciphertext)
        expected_shift = calculate_shift(decrypted, key)
        if shift != expected_shift:
            raise ValueError("Invalid key or corrupted ciphertext.")
        return decrypted
    except ValueError as e:
        return f"Decryption failed: {e}"

def main():
    """Main function to handle user interaction."""
    try:
        # user will tell his choice
        choice = int(input("Do you want to (1) encrypt or (2) decrypt a string? "))
        if choice not in [1, 2]:
            raise ValueError("Choice must be 1 or 2.")
        
        # Getting input string and key
        input_str = input("Enter a string: ").strip()
        if not input_str:
            raise ValueError("Input string cannot be empty.")
        key = input("Enter a key: ").strip()
        if not key:
            raise ValueError("Key cannot be empty.")
        
        if choice == 1:
            result = encrypt_string(input_str, key)
            print(f"Encrypted: {result}")
        else:
            result = decrypt_string(input_str, key)
            print(f"Decrypted: {result}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
    
