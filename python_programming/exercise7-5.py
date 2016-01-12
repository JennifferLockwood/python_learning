# exercise7-5.py

def main():
    print("This program calculates a person's BMI (body mass index).")
    weightPounds = eval(input("Please enter your weight in pounds: "))
    heightInches = eval(input("Please enter your height in inches: "))

    bodyMassIndex = (720 * weightPounds) / (heightInches ** 2)

    if bodyMassIndex < 19:
        print("Your BMI is {0:0.2f}, and it's below the healthy range.".format(
            bodyMassIndex))
    elif bodyMassIndex > 25:
        print("Your BMI is {0:0.2f}, and it's above the healthy range.".format(
            bodyMassIndex))
    else:
        print("Your BMI is {0:0.2f}, and it's within the healthy range.".
              format(bodyMassIndex))

main()
