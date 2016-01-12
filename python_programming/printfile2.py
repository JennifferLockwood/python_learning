# printfile2.py
#   Prints a file to the screen

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    for i in range(5):
        line = infile.readline()
        print(line[:-1])

main()
