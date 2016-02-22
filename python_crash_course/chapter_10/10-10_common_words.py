def count_common_words(filename):
    """Count how many times the word 'the' in the file."""
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count how many times the word 'the' in the file.
        total = 0
        for line in lines:
            x = line.lower().count('the')
            total += x
        print("The word 'the appears " + str(total) +
              " times in the file " + filename + ".")

filenames = ['a_strange_disappearance.txt', 'the_rome_express.txt']
for filename in filenames:
    count_common_words(filename)
