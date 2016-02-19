print("Printing the content of a file by reading in the entire file:")
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)


print("\nPrinting the content of a file by looping over the file object:")
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print()

print("\nPrinting the content of a file by storing the lines in a list")
print("and then working with them outside the with block:")
with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''
for line in lines:
    learning_python_string += line

print(learning_python_string)
print(len(learning_python_string))
