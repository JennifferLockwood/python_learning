# exercise5-2.py
#   A program that accepts 5-point quiz score as an input and
#   prints out the corresponding grade

def main():
    # get the score
    score = eval(input("Please enter the 5-point quiz score: "))

    grades = ["F", "F", "D", "C", "B", "A"]

    grade = grades[score]

    print("The corressponding grade for this quiz is", grade, ".")

main()
