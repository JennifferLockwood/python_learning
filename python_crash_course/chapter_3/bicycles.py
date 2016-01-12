# bicycles.py

bicycles = ['trek', 'cannondale', 'redline', 'schwinn', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[3].title() + "."
print(message)

'''
for i in range(len(bicycles)):
    print(bicycles[i].title())
print("Done!")
'''
