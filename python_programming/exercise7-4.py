# exercise7-4.py

def main():
    print("This program calculates class standing from the number of credit " +
          "earned.")

    numberCredits = eval(input("\nPlease enter number of credits earned by " +
                                 "the student: "))

    if 0 <= numberCredits < 7:
        print("The students is a Freshman.\n")
    elif 7 <= numberCredits < 16:
        print("The student is a Sophomore.\n")
    elif 16 <= numberCredits < 26:
        print("The student is a Junior.\n")
    elif numberCredits >= 26:
        print("The student is a Senior.\n")
    else:
        print("Please enter a correct number.\n")

main()
