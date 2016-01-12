# sumnumbers.py
#    Program to compute the sum of the first n natural numbers
#    where the value of n is provided by the user.

def main():
    n = eval(input("Please enter a whole number: "))
    number = 1
    for  result in range(n,1,-1):
        number = number + result
    print("The sum of the first", n, "natural numers is", number)

main()

