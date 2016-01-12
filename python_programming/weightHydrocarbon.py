# weightHydrocarbon
#    A program that calculates the weight of a hydrocarbon
#    Given the number of hydrogen, carbon and oxygen.

def main():
    print("This program calculates the weight of a hydrocarbon.")

    hydrogen = eval(input("Please enter the number of hydrogen: "))
    carbon = eval(input("Please enter the number of carbon: "))
    oxygen = eval(input("Please enter the number of oxygen: "))
    total = (1.0079 * hydrogen) + (12.011 * carbon) + (15.994 * oxygen)

    print()
    print("The weight of the hydrocarbon is: ", total)

main()
    
