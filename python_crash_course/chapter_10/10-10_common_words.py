def count_common_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        sum = 0
        for line in lines:
            x = line.lower().count('the')
            sum = sum + x
        print("The word 'the appears " + str(sum) +
              " times in the file " + filename + ".")

filenames = ['a_strange_disappearance.txt', 'the_rome_express.txt']
for filename in filenames:
    count_common_words(filename)
