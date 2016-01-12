# exercise5-4.py
#   A program that outputs the acronym for a phrase typed in
#   by the user

def main():
    userPhrase = input("Please type in a phrase: ")

    for everyWord in userPhrase.split():
        firstLetter = everyWord[0]
        # acronym = acronym + firstLetter.upper()

        print(firstLetter.upper(), end="")

main()
