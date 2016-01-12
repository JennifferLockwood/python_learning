'''
Two functions below show two different ways to square a list of numbers.  The first function
mutates the list "in place".  The second creates a new list and returns it.

Using these two ways of designing a function to act on a list, write a similar program that takes
a list of strings with new lines and removes the new line from each string in the list.  Write one
function to "trim" the string in place, and another to return a new list with the trimmed strings.
'''

# Returns the squares in place
def square_list_mutate(numberList):
	for i in range(len(numberList)):
		numberList[i] = numberList[i] * numberList[i]

# Returns a new list with the squares
def square_list_return(numberList):
	new_list = []
	for i in range(len(numberList)):
		new_list.append(numberList[i] * numberList[i])
	return new_list

def main():
	numbers = [5,4,3,2,1]
	square_list_mutate(numbers)
	print(numbers)

	numbers = [1,2,3,4,5]
	new_numbers = square_list_return(numbers)
	print(new_numbers)

main()