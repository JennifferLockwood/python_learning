# 4-12_more_loops.py

my_foods = ['salads', 'falafel', 'hummus', 'fish']
friend_foods = my_foods[:]

my_foods.append('spaguetti')
friend_foods.append('sprouts')

print("\nMy favorite foods are:")
for food in my_foods:
    print("- " + food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("- " + food.title())
