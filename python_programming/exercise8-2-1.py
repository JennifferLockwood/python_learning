# exercise8-2-1.py

def main():
    print("This program prints a table of windchill values.")
    windchillIndex = 0
    temperature = list(range(-20, 70, 10))
    print("{0:^3}{1:10}{2:10}{3:10}{4:10}{5:10}{6:10}{7:10}{8:10}{9:10}".
          format("V\T", temperature[0], temperature[1], temperature[2],
                 temperature[3], temperature[4], temperature[5], temperature[6],
                 temperature[7], temperature[8]))
    for v in range(0, 55, 5):
        print("{0:3}".format(v), end = "")
        for t in range(-20, 70, 10):
            windchillIndex = 35.74 + (0.6215 * t) - (35.75 * (v**0.16)) + (
                0.4275 * t * (v**0.16))
            print("{0:10.4f}".format(windchillIndex), end="")
        print()

main()
