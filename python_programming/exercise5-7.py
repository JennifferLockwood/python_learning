# exercise5-7.py
#   A program that can encode and decode a Caesar ciphers.
#   A Caesar cipher is a simple substitution cipher based on the
#   idea of shifting each letter of the plaintext message a fixed
#   number (called the key).

def main():
    print("This program encode and 'reencode' Caesar ciphers.")

    message = input("Please enter a plaintext to encode (or to 'reencode'): ")
    key = eval(input("Please enter key value (to 'reencode' enter a negative key): "))

    for ch in message:
        print(chr(ord(ch)+key), end="")

    print()

main()
