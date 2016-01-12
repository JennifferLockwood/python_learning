# exercise5-12.py
#   A program to compute the value of an investment
#   carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a n-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    n = eval(input("Enter number of years into the future: "))
    
    print()
    print("{0:^5}  {1:^8}".format("Year", "Value"))
    print("----------------")
    print("{0:^5}  ${1:0.2f}".format("0", principal))

    for i in range(n):
        principal = principal * (1 + apr)
        print("{0:^5}  ${1:0.2f}".format(i+1, principal))
        
main()
