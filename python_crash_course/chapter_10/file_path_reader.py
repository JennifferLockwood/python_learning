file_path = '/home/john/Dropbox/source/python_learning/python_programming/numberExercise6-14'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
