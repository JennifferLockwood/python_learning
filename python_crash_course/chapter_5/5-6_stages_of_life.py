# 5-6_stages_of_life.py

print("This program determines a person's stage of life.")
age = eval(input("Please enter the person's age: "))

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print("\nThis person is a " + stage + ".\n")



