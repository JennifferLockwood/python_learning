# futval3.py
#   A program to compute the value of an investment
#   carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a n-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Enter number of years into the future: "))

    for i in range(n):
        principal = principal * (1 + apr)
        print("{0:0.2f}".format(principal))

    print("The value in ", n, "years is:", "{0:0.2f}".format(principal))

main()
