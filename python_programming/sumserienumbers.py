# sumserienumbers.py
#    Program to compute the sum a series of numbers entered by the user.


def main():
    total = 0
    n = eval(input("Please enter how many numbers are to be summed: "))
    for i in range(n):
        number = eval(input("Please enter a number: "))
        total = number + total
        
    print("The total sum of the serie of numbers is ", total)

main()

