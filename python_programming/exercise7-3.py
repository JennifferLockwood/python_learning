# exercise7-3.py

def main():
    print("This program calculates the corresponding grades " +
          "for 100-point exams.")

    pointsExam = eval(input("Please enter an exam score from 0 - 100: "))
    if 90 <= pointsExam <= 100:
        print(pointsExam, "points exam got a A grade.")
    elif 80 <= pointsExam <= 89:
        print(pointsExam, "points exam got a B grade.")
    elif 70 <= pointsExam <= 79:
        print(pointsExam, "points exam got a C grade.")
    elif 60 <= pointsExam <= 69:
        print(pointsExam, "points exam got a D grade.")
    elif pointsExam < 60:
        print(pointsExam, "points exam got a F grade.")
    else:
        print("Please enter a number between 0 and 100.")

main()
