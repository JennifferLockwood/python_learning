# exercise8-3.py

def main():
    print("This program determines how long it takes for an investment")
    print("to double at a given interest rate.")

    principal = 100.00
    apr = eval(input("Enter the annual interest rate: "))
    n = 0

    while principal <= 200.00:
        principal = principal * (1 + apr)
        n = n + 1
        # print (principal)

    print("The investment takes", n, "years to double.")

main()