# 6-8_pets.py

wally = {'animal': 'cockatiel',
         'owner': 'edward collins',
          'city': 'springfield',
          }
sparky = {'animal': 'cockatiel',
         'owner': 'michelle lauren',
          'city': 'san diego',
          }
apolo = {'animal': 'dog',
         'owner': 'phil jackson',
          'city': 'portland',
          }
darwin = {'animal': 'guinea pig',
         'owner': 'grace vogue',
          'city': 'vacaville',
          }

pets = [wally, sparky, apolo, darwin]

for pet in pets:
    # print(pets[pet].upper())
    print("Kind of animal: " + pet['animal'].title())
    print("Owner: " + pet['owner'].title())
    print("city: " + pet['city'].title())
