# exercise7-9.py

def easterYear(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
    easterDate = 22 + d + e
    return easterDate

def main():
    print("This program calculates the date of Easter in the years 1982 - " +
          "2048, inclusive.")
    try:
        year = int(eval(input("Please enter an exact year: ")))
        if 1982 <= year <= 2048:
            date = easterYear(year)
            if 22 <= date <= 31:
                print("The Easter in {0} is March {1}.".format(year, date))
            elif 32 <= date <= 61:
                print("The Easter in {0} is April {1}.".format(year, date - 31))
            else:
                print("Wrong calculation!")
        else:
            print("Please enter a year between 1982 and 2048, inclusive.")
    except NameError:
        print("Please enter a number, and try again.")
    except:
        print("Unknown error.")

main()
