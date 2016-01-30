# 3-8_world_places.py

world_places = ['yellowstone', 'grand canyon', 'cano cristales', 'machupichu',
                'alaska', 'hawaii']
print(world_places)
print(sorted(world_places))
print("\nHere's the sorted list:")
print(sorted(world_places))
print("\nThis is the original list:")
print(world_places)

print("\nHere's is the sorted list in reverse alphabetical order:")
print(sorted(world_places,reverse=True))
print("\nThis is the original list:")
print(world_places)

world_places = ['yellowstone', 'grand canyon', 'cano cristales', 'machupichu',
                'alaska', 'hawaii']
print("\nHere's the list in reversed order (permanent change):")
world_places.reverse()
print(world_places)
print("\nHere's the original list:")
world_places.reverse()
print(world_places)

world_places = ['yellowstone', 'grand canyon', 'cano cristales', 'machupichu',
                'alaska', 'hawaii']
print("\nHere's the list using sort():")
world_places.sort()
print(world_places)
print("\nHere's the list using sort(reverse=True):")
world_places.sort(reverse = True)
print(world_places)

