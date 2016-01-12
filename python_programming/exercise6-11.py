# exercise6-11.py

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

def test():
    numbers = [4, 10, 25, 36, 50]
    squareEach(numbers)
    print(numbers)

test()
