# exercise5-10.py
#   A program that calculates the average word length in a
#   sentence entered by the user.

def main():
    print("This program calculates the average word length in a sentence.")

    sentence = input("Please enter a sentence: ")

    words = sentence.split()

    total = 0

    for i in words:
        total = total + len(i)

    averageWordLength = total / len(words)

    print("{0:0.2f} is the average word length of the sentence.".format(averageWordLength))

'''    
    print(averageWordLength, "is the average word length of the sentence.")

'''

main()

