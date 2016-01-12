# dateconvert3.py
#   Convert day month and year numbers into two date formats
#   using string formatting

def main():
    # Get the day month and year
    day, month, year = eval(input("Enter day, month, and year numbers: "))

    # date1 = str(month) + "/" + str(day) + "/" + str(year)

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]
    monthStr = months[month-1]
    # date2 = monthStr + " " + str(day) + "," + str(year)

    # print("The date is:", date1, "or", date2 + ".")

    print("The date is {1:0>2}/{0:0>2}/{2} or {3} {0}, {2}.".format(
        day, month, year, monthStr))

main()
