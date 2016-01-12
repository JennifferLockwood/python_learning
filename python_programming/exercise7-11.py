# exercise7-11.py

def main():
    print("This program calculates whether a year is a leap year.")
    try:
        year = eval(input("Please enter a year: "))
        year = int(year)
        if year % 400 == 0:
            print(year, "is a leap year.")
        elif year % 100 == 0:
            print(year, "is not a leap year.")
        elif year % 4 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    except NameError:
        print("Please enter a correct number.")
    except:
        print("\nUnknown error.")

main()
