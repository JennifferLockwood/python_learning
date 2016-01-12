# exercise8-2.py

def main():
    print("This program prints a table of windchill values.")
    windchillIndex = 0
    for v in range(0, 55, 5):
        for t in range(-20, 70, 10):
            windchillIndex = 35.74 + (0.6215 * t) - (35.75 * (v**0.16)) + (
                0.4275 * t * (v**0.16))
            print("{0:8.4f}".format(windchillIndex))

main()
