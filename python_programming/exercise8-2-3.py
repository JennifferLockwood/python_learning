# exercise8-2-3.py

def main():
    v = 0
    while v <= 50:
        print("{0:3}".format(v), end = "")
        v = v + 5
        t = -20
        while t <= 60:
            result = 35.74 + (0.6215 * t) - (35.75 * (v**0.16)) + (0.4275 * t * (v**0.16))
            print("{0:14.4f}".format(result), end="")
            t = t + 10
        print()

main()
