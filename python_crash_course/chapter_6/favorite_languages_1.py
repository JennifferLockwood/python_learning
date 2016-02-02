# 6-6_polling.py

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

other_people = ['john', 'sarah', 'david', 'phil', 'monique']

for name in favorite_languages.keys():
    print(name.title() + ",thank you for taking the poll.")

    if name in other_people:
        print("  Hi " + name.title() +
              ", please take our poll!")
