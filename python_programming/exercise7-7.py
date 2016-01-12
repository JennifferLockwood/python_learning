# exercise7-7.py

def main():
    print("This program calculates the total babysitting bill.")
    try:
        start_time = input("Please enter a start time in form HH:MM: ")
        end_time = input("Please enter a end time in form HH:MM: ")
        startHHMM = start_time.split(":")
        endHHMM = end_time.split(":")
        startHH = int(startHHMM[0])
        startMM = int(startHHMM[1]) / 60
        endHH = int(endHHMM[0])
        endMM = int(endHHMM[1]) / 60
        totalHH = endHH - startHH
        totalMM = endMM - startMM
        print(startHHMM, endHHMM, startHH, startMM, endHH, endMM,
              totalHH, totalMM)

        if endHH <= 21:
            total_bill = (totalHH + totalMM) * 2.50
            print("The total babysitting bill is ${0:0.2f}.".format(total_bill))
        elif endHH > 21 and startHH > 21:
            total_Bill = (totalHH + totalMM) * 1.75
            print("The total babysitting bill is ${0:0.2f}.".format(total_bill))
        else:
            bill2_50 = (21 - startHH - startMM) * 2.50
            bill1_75 = (endHH + endMM - 21) * 1.75
            total_bill = bill2_50 + bill1_75
            print("The total babysitting bill is ${0:0.2f}.".format(total_bill))

    except NameError:
        print("Please enter a correct time, and try again.")

main()
