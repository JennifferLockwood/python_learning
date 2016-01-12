# exercise5-6.py
#   A program that calculates the numeric value of a complete name

def main():
    print("This program calculates the numeric value of a complete name.")

    fullName = input("Please enter a complete name: ")

    newValue = ord("a") - 1         # "a"=1, "b"=2, etc., up to "z"=26
    total = 0
    for ch in fullName.replace(" ", chr(newValue)).lower():
        total = total + (ord(ch)-newValue)

    print("The numeric value of", fullName, "is", total, ".")

main()
