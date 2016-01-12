# sumcubesn.py
#    Program to compute the sum cubes of the first n natural numbers
#    where the value of n is provided by the user.

def main():
    n = eval(input("Please enter a whole number: "))
    result = 1
    for number in range(2, n + 1):
        result = result + number ** 3
    print("The sum of the cubes of the first", n, "natural numbers is", result)

main()

