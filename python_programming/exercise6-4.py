# exercise6-4.py

def sumN(n):
    number = 1
    for  result in range(n,1,-1):
        number = number + result
    print("The sum of the first", n, "natural numbers is", number)

def sumNCubes(n):
    result = 1
    for number in range(2, n + 1):
        result = result + number ** 3
    print("The sum of the cubes of the first", n, "natural numbers is", result)

def main():
    n = eval(input("Please enter a whole number: "))
    sumN(n)
    sumNCubes(n)

main()
