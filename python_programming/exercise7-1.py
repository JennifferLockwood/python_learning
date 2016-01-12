# exercise7-1.py

def main():
    print("This program calculate the total wages for the week.\n")
    hoursWorked, hourRate = eval(input("Please enter the number of hours worked" +
                                       "and the hourly rate (Hours, Rate): "))

    if hoursWorked <= 40:
        weekWage = hoursWorked * hourRate
        print("\nThe total wages for the week are ${0:0.2f}.".format(weekWage))

    else:
        fullTime = 40
        extraHours = hoursWorked - fullTime
        extraWage = extraHours * (1.5 * hourRate)
        weekWage = (fullTime * hourRate) + extraWage
        print("\nThe total wages for the week are ${0:0.2f}.".format(weekWage))

main()
