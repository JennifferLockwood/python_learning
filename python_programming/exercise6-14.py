# exercise6-14.py

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums

def sumList(nums):
    result = 0
    for i in range(len(nums)):        
        result = nums[i] + result
    return result

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

def main():
    print("This program computes the sum of the squares of numbers read")
    print("from a file.")

    infileName = input("What file are the numbers in? ")
    infile = open(infileName, "r")
    
    numbersList = []
    for line in infile.readlines():
        numbersList.append(line[:-1])

    numbers = toNumbers(numbersList)
    
    squareNumbers = squareEach(numbers)
    
    sumSquares = sumList(squareNumbers)
    
    print("The sum of the squares of numbers read from file", infileName, "is:")
    print(sumSquares)
    
    infile.close()
    
main()
