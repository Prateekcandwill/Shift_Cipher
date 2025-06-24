# Meme Shift Cipher

The Meme Shift Cipher is an enhanced classical substitution cipher that builds on the Caesar Cipher by using a dynamic shift value derived from the input string and a user-provided key. This project implements the improved cipher in Python, addressing issues in the original design, such as inconsistent encryption-decryption cycles, by incorporating a consistent shift calculation, key-based encryption, and robust error handling.

---

## Story behind this project

This I started long ago in library there was a new arrival of a Book nammed "The Code Book" I thought then to make a cipher probably with some meme context that's why the name is this but no meme relation is present here.

---

## Features

- **Dynamic Shift:** Shift value calculated from alphabetic characters of the input string and key.
- **Key-Based Encryption:** User-provided key enhances security.
- **Shift Storage:** Shift value appended to ciphertext for reliable decryption.
- **Input Validation:** Handles invalid inputs gracefully.
- **Educational Tool:** Demonstrates classical cryptography concepts.

---

## Implementation Details

The cipher is implemented in `meme_shift_cipher.py` with the following key functions:

- `calculate_shift(input_str, key)`: Computes a shift value from alphabetic characters of the input and key.
- `meme_shift_encrypt_char(ch, shift)`: Encrypts a single character.
- `meme_shift_decrypt_char(ch, shift)`: Decrypts a single character.
- `encrypt_string(input_str, key)`: Encrypts the input and appends the shift (e.g., ciphertext:15).
- `decrypt_string(ciphertext_with_shift, key)`: Decrypts the ciphertext, verifying the shift with the key.

---

# Shift Calculation Formula

This formula calculates a shift value based on the sum of ASCII values of alphabetic characters in both an input string and a key.

## Formula

shift = (sum(ASCII(char.lower()) for alpha char in input_str) + 
         sum(ASCII(char.lower()) for alpha char in key)) % 26


- **input_str**: The string to be processed.
- **key**: The key string used for the calculation.
- Only **alphabetic characters** are considered.
- Characters are converted to **lowercase** before getting their ASCII values.
- The result is taken modulo 26.

## Example

![](https://github.com/Prateekcandwill/Shift_Cipher/blob/1ecaa9a499b124227d64a068ee2e014835ada5df/demoofmemecipher.gif)

```
$ python meme_shift_cipher.py
Do you want to (1) encrypt or (2) decrypt a string? 1
Enter a string: hello
Enter a key: secret
Encrypted: rknzc:15
```

```
$ python meme_shift_cipher.py
Do you want to (1) encrypt or (2) decrypt a string? 2
Enter a string: rknzc:15
Enter a key: secret
Decrypted: hello
```
## Calculation:
 - Convert all alphabetic characters to lowercase.
 - Sum their ASCII values.
 - Add the sums from `input_str` and `key`.
 - Take the result modulo 26 to get the shift value.


---

## Security

- **Strengths:** More resistant to frequency analysis than the Caesar Cipher due to the dynamic key-based shift.
- **Limitations:** Vulnerable to frequency analysis with sufficient ciphertext; not suitable for secure applications compared to modern ciphers like AES.

---

## Comparison with Classical Ciphers

| Cipher     | Key Space              | Frequency Analysis     | Complexity |
|------------|------------------------|-----------------------|------------|
| Caesar     | 26                     | Vulnerable            | Low        |
| Vigenère   | 26^k (k = key length)  | Moderately Resistant  | Medium     |
| Meme Shift | Variable (input + key) | Moderately Resistant  | Medium     |

---

## Contact

For support, email prateek.kumar17@s.amity.edu or raise an issue on this repository.

---
