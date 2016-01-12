# exercise7-10.py

def easterYear(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
    easterDate = 22 + d + e
    return easterDate

def yearCheck(year, date):
    yearsExcept = [1954, 1981, 2049, 2076]
    for i in yearsExcept:
        if i == year:
            date = date - 7
            print("Date has changed to", date)
    return date

def main():
    print("This program calculates the date of Easter in the years 1900 - " +
          "2099, inclusive.")
    try:
        year = int(eval(input("Please enter an exact year: ")))
        if 1900 > year:
            print("Year is out of range.")
        elif year > 2099:
            print("Year is out of range.")
        else:
            date = easterYear(year)

            date = yearCheck(year, date)
            
            if 22 <= date <= 31:
                print("The Easter in {0} is March {1}.".format(year, date))
            elif 32 <= date <= 61:
                print("The Easter in {0} is April {1}.".format(year, date - 31))
            else:
                print("Wrong calculation!")
                
    except NameError:
        print("Please enter a number, and try again.")
    except:
        print("Unknown error.")

main()
