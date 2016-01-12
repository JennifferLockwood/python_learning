# convert5.py
#     A program to convert kilometers to miles.
# by: Jenniffer Lockwood

def main():
    print("This program converts distances measured in kilometers to miles")
    
    kilometers = eval(input("What is the distance in kilometers? "))
    miles = kilometers * 0.62
    print("The measure is", miles, "miles.")


main()
