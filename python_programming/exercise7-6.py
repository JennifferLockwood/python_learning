# exercise7-6.py

def main():
    try:
        print("This program calculates the amount of the fine, if the speed")
        print("was illegal, according tohe policy in Podunksville.")
        speedLimit = eval(input("Please enter the zone speed limit: "))
        speedClocked = eval(input("Please enter the clocked speed: "))

        overSpeed = speedClocked - speedLimit
        speedFine = (5 * overSpeed) + 50
        speedOver90 = speedFine + 200

        if speedClocked <= 0:
            print("Please enter a correct speed and try again.")
        elif speedClocked <= speedLimit:
            print("The speed was legal.")
        elif speedClocked <= 90:
            print("The speed was illegal. The speeding ticket fine is " +
                  "${0:0.2f}.".format(speedFine))
        else:
            print("The speed was over 90 mph. The speeding ticket fine is " +
                  "${0:0.2f}.".format(speedOver90))
    except NameError:
        print("You didn't enter a number. Please try again.")
        
main()
