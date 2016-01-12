# exercise5-11.py
#   A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    print()
    print("{0:^3} {1:^12} {2:^12}".format("index", x, y))
    print("-----------------------------")
    for i in range(n):
        x = 3.9 * x - 3.9 * x * x
        y = 3.9 * y - 3.9 * y * y
        print("{0:>3} {1:>12f} {2:>12f}".format(i+1, x, y))

main()

