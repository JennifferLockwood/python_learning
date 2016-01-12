from math import*

def main():
    n = eval(input("Enter the nth term of the Fibonacci number: "))
    numFib = 0
    print("This is the sequence of the Fibonacci number:")
    for i in range(1, n + 1):
        numFib = ((1 + sqrt(5))**i - (1 - sqrt(5))**i) / (2**i * sqrt(5))
        print(int(numFib))

main()
