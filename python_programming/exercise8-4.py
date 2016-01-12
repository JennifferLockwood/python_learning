# exercise8-4.py

def main():
    x = eval(input("Enter a natural number >> "))

    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = (3 * x) + 1
        print(int(x), end=" ")

main()
