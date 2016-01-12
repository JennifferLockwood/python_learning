# function_call_mongo101.py

fruit = ['apple', 'orange', 'grape', 'kiwi', 'orange',
         'apple']    # init the array

# reports the frequency of every item in a list
def analize_list(l):
    counts = {}
    for item in l:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts

# let's analize a list
counts = analize_list(fruit)
print(counts)
