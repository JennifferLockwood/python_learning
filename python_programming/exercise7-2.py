# exercise7-2.py

def main():
    print("This program calculates the corresponding grade for a five-point quiz.")
     
    try:
        quizScore = eval(input("Please enter the 5-point quiz score: "))
        if quizScore == 5:
            print('\nThis student got A grade.')
        elif quizScore == 4:
            print('\nThis student got B grade.')
        elif quizScore == 3:
            print('\nThis student got C grade.')
        elif quizScore == 2:
            print('\nThis student got D grade.')
        elif quizScore == 1:
            print('\nThis student got F grade.')
        elif quizScore == 0:
            print('\nThis student got F grade.')
        else:
            print('\nPlease enter a number between 0 and 5.')
    except NameError:
        print('\nPlease correct the number.')
        
main()
