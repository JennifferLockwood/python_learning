# convert.py
#     A program to convert Celsius temp to Fahrenheit
# by: Susan Computewell

def main():
    print("This program converts Celsius temperature to Fahrenheit")
    print("CELSIUS       FAHRENHEIT")
    for celsius in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        fahrenheit = 9/5 * celsius + 32
        print("{0:0.2f}         {1:0.2f}".format(fahrenheit, celsius))


main()
