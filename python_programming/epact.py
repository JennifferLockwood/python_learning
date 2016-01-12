# epact.py
#    A program that calculates the Gregorian epact, the number of days between
#    January 1st and the previous new moon.

def main():
    print("This program calculate the Gregorian epact.")
    print()

    year = eval(input("Please enter a 4-digit year: "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
    print()
    
    print("The value of the epact is:", epact)

main()

