# convert.py
#     A program to convert Celsius temp to Fahrenheit
# by: Susan Computewell

def main():
    print("This program converts Celsius temperature to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
