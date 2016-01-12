# solutionfunction_assigment_solution.py

def string_list_mutate(stringList):
    for i in range(len(stringList)):
        stringList[i] = stringList[i][:-1]

def string_list_return(stringList):
    newList = []
    for i in range(len(stringList)):
        newList.append(stringList[i][:-1])
    return newList

def main():
    strings = ["blue\n", "orange\n", "yellow\n", "pink\n", "black\n"]
    string_list_mutate(strings)
    print(strings)

    strings1 = ["black\n", "pink\n", "yellow\n", "orange\n", "blue\n"]
    newStrings = string_list_return(strings1)
    print(newStrings)

main()
