# futval1.py
#   A program to compute the value of an investment
#   carried 10 years into the future
#   This program has an error.

def main():
    print("This program calculates the future value")
    print("of a n-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in", year, "years is:", "{0:0.2f}".format(principal))

main()
