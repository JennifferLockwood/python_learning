# ifelifelse_example2.py

def main():
    color = input("Please enter a primary color: ")
    primaryColor = color.capitalize()
    if primaryColor == "Red":
        print("1 -", primaryColor, "is the color of fire and blood.")
    elif primaryColor == "Yellow":
        print("2 -", primaryColor, "is the color of sunshine.")
    elif primaryColor == "Blue":
        print("3 -", primaryColor, "is the color of the sky and sea.")
    else:
        print("Please enter a primary color, and try again.")

    print("Good bye!")

main()
