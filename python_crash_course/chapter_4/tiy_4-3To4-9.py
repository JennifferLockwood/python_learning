# tiy_4-3To4-9.py

for value in range(1,21):       # 4-3
    print(value)
print()

print('TIY 4-4 and 4-5: "One Million" and "Summing a Million"') 
million = list(range(1, 1000001))
print("The minimum number is:")
print(min(million))
print("The maximum number is:")
print(max(million))
print("The sum of the first million of numbers is:")
print(sum(million))
print()

# 4-6 Odd Numbers
numbers = list(range(1, 20, 2))
for odd in numbers:
    print(odd)
print()

# 4-7 Threes
print("Following are the multiples of three from 3 to 30:")
multiples = list(range(0,33, 3))
for three in multiples:
    print(three)
print()

# 4-8 Cubes
print("List of the first 10 cubes:")
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)
print()

# 4-9 Cube Comprehension
print("List of the first 10 cubes:")
cubes = [value**3 for value in range(1, 11)]
print(cubes)
