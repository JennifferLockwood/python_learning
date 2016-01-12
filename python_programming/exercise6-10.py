# exercise6-10.py
#   A program that calculates the numeric value of a single name

def acronym(phrase):
    total = 0
    for ch in phrase.lower():
        total = total + (ord(ch)-96)
    return total

def main():
    print("This program calculates the numeric value of a single name.")

    name = input("Please enter a single name: ")
    nameNumericValue = acronym(name)
    
    print("The numeric value of", name, "is", nameNumericValue)

main()
