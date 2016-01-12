# lightningStrike
#    A program that calculates the distance to a lightning strike.
#    The speed of sound is approx. 1100 ft/sec and 1 mile is 5280 ft.

def main():
    print("This program calculates the distance to a lightning strike.")

    time = eval(input("Please enter the number of seconds between the flash and the sound of thunder: "))
    distance = (5 / 24) * time      #  1100 / 5280 = 5 / 24

    print()
    print("The distance to a ligthning strike is: ", "{0:0.2f}". format(distance), "miles.")

main()
    
