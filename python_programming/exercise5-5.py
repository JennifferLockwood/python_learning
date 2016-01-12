# exercise5-5.py
#   A program that calculates the numeric value of a single name

def main():
    print("This program calculates the numeric value of a single name.")

    name = input("Please enter a single name: ")

    total = 0
    for ch in name.lower():
        total = total + (ord(ch)-96)

    print("The numeric value of", name, "is", total, ".")

main()
