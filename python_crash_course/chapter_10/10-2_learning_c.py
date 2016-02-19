filename = 'learning_python.txt'

print("Replacing the word Python with JavaScript:")
with open(filename) as file_object:
    lines = file_object.readlines()

learning_python_string = ''
for line in lines:
    line = line.replace('Python', 'JavaScript')
    learning_python_string += line

print(learning_python_string)
