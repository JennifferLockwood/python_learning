# exercise7-8.py

def main():
    try:
        print("This program outputs the eligibility of a person for " +
              "US representative or US senator.")
        agePerson = eval(input("Please enter the age of the person: "))
        yearsCitizen = eval(input("Please enter years of citizenship: "))

        if 30 > agePerson >= 25 and 9 > yearsCitizen >= 7:
            print("This person is eligible for US representative.")
            print("But this person is not eligible for US senator.")
        elif agePerson >= 30 and yearsCitizen >= 9:
            print("This person is eligible for US representative and " +
                  "US senator.")
        elif agePerson < 25 and yearsCitizen < 7:
            print("This person is not eligible either for US representative " +
                  "or US senator.")
        else:
            print("Please enter a correct age!")
    except NameError:
        print("Please enter a number and try again.")
    except SyntaxError:
        print("Please enter a number and try again.")

main()
