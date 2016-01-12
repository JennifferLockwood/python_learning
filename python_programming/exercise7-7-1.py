# exercise7-7-1.py

def get_time(time):
    timeHHMM = time.split(":")
    timeHH = float(timeHHMM[0])
    timeMM = float(timeHHMM[1]) / 60
    total_time = timeHH + timeMM
    return total_time

def main():
    print("This program calculates the total babysitting bill.")
    try:
        start_time = input("Please enter a start time in form HH:MM: ")
        end_time = input("Please enter a end time in form HH:MM: ")
        startHHMM = get_time(start_time)
        endHHMM = get_time(end_time)

        if endHHMM <= 21.00:
            total_bill = (endHHMM - startHHMM) * 2.50
            print("The total babysitting bill is ${0:0.2f}.".format(total_bill))
        elif startHHMM > 21.00:
            total_bill = (endHHMM - startHHMM) * 1.75
            print("The total babysitting bill is ${0:0.2f}.".format(total_bill))
        else:
            total_bill = ((21.0 - startHHMM) * 2.50) + ((endHHMM - 21.0) * 1.75)
            print("The total babysitting bill is ${0:0.2f}.".format(total_bill))            
            
        print(startHHMM, endHHMM)

    except NameError:
        print("Please enter a correct time, and try again.")

main()
    
    
