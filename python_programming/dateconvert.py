# dateconvert.py
#   Convert a date in form "mm/dd/yyyy" to 'month day, year.'

def main():
    # Get the date
    dateStr = input("Enter a date in form (mm/dd/yyyy): ")

    # Split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # Convert monthStr to the month name
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # Output result in month day, year. format
    print("The converted date is:", monthStr, dayStr + ",", yearStr, ".")

main()
