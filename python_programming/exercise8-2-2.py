# exercise8-2-2.py

def printBlock(v, t):
    result = 35.74 + (0.6215 * t) - (35.75 * (v**0.16)) + (0.4275 * t *
                                                           (v**0.16))
    return result

def main():
    print(printBlock(5, -20))

main()
