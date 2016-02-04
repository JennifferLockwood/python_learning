group = input("How many people are in your dinner group? ")
group = int(group)

if group > 8:
    print("\nI'm sorry, but you'll have to wait for a table because you have a group of " + str(group) + " people.")
else:
    print("\nGreat! Your table is ready.")