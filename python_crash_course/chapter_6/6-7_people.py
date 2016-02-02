# 6-7_people.py

person_0 = {'first_name': 'wally',
          'last_name': 'cockatiel',
          'age': 2,
          'city': 'springfield',
          }
person_1 = {'first_name': 'sparky',
          'last_name': 'cockatiel',
          'age': 4,
          'city': 'santa clara',
          }
person_2 = {'first_name': 'edward',
          'last_name': 'collins',
          'age': 25,
          'city': 'nashville',
          }

people = [person_0, person_1, person_2]

for person in people:
    print("\nFIRST NAME: " + person['first_name'].title())
    print("LAST NAME: " + person['last_name'].title())
    print("AGE: " + str(person['age']) + " years")
    print("CITY: " + person['city'].title())
