# exercise6-12.py

def sumList(nums):
    result = 0
    for i in range(len(nums)):        
        result = nums[i] + result
    return result

def test():
    numbers = [4, 10, 36, 50, 125, 200]    
    print(sumList(numbers))    

test()
