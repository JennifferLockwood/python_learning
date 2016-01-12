# exercise6-9.py
#   A program that prints out the corresponding grade
#   for a 100-point exam.

def grade(score):
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    grade = grades[score//10]
    return grade

def main():
    print("This program prints out the correponding grade")
    print("for an exam score.")

    score = eval(input("Please enter an exam score: "))
    finalGrade = grade(score)
    
    print("A score of", score, "has a corresponding grade of", finalGrade)

main()
