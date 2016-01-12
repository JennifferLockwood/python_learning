# exercise5-13.py
#   A program that creates a files of acronyms in batch mode

def main():
    print("This program creates a file of acronym from a")
    print("file of phrases.")

    # get the file phrases
    infileName = input("What file are the phrases in? ")
    outfileName = input("What file should the acronyms go in? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        for everyWord in line.split():
            firstLetter = everyWord[0]
            print(firstLetter.upper(), end="", file = outfile)
        print(file = outfile)

    #close both file
    infile.close()
    outfile.close()

    print("Acronyms have been written to", outfileName)

main()
