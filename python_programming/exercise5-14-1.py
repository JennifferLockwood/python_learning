# exercise5-14-1.py
#   A program that counts lines, words and characters
#   from a file name

def main():
    print("This program counts lines, words and characters")
    print("from a file of phrases.")

    # get the file phrases
    infileName = input("What file are the phrases in? ")

    # open the files
    infile = open(infileName, "r")
    characters = infile.read()
    totalCharacters = len(characters)

    # close file
    infile.close()

    # open the files
    infile = open(infileName, "r")

    totalLines = 0
    totalWords = 0

    # process each line of the input file
    for line in infile:
        totalLines = totalLines + 1
        wordsLine = line.split()
        totalWords = totalWords + len(wordsLine)

    print("The file", infileName, "has", totalLines, "lines,", totalWords, "words, and",
          totalCharacters, "characters.")
                       
    # close file
    infile.close()
    
main()
