# convert4.py
#     A program to convert Celsius temp to Fahrenheit
# by: Susan Computewell

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (5/9) * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius.")


main()
