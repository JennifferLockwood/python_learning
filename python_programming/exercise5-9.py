# exercise5-9.py
#   A program that counts the number of words in a
#   sentence entered by the user.

def main():
    print("This program counts the number of words in a sentence.")

    sentence = input("Please enter a sentence: ")

    print("The sentence has", len(sentence.split()), "words.")

main()
