def reading_files(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        pass
    else:
        # Print the contents of the file to the screen.
        print("\nThe file " + filename + " has the following names:")
        for line in lines:
            print("\t" + line.rstrip())

filenames = ['cats.txt', 'birds.txt', 'dogs.txt']
for filename in filenames:
    reading_files(filename)
