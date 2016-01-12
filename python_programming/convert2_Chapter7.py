# convert2_Chapter7.py
#       A program to convert Celsius temp to Fahrenheit
#       This version issues heat and cold warnings

def main():
    print("This program converts Celsius temperature to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")


main()
