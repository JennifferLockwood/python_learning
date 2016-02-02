# 6-9_favorite_places.py

favorite_places = {
    'john': ['folsom lake', 'golden gate bridge'],
    'monique': ['gran canyon', 'statue of liberty'],
    'edward': ['central park', 'lincoln memorial'],
    'rose': ['yellowstone national park', 'niagara falls'],
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
