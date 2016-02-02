# 6-5_rivers.py

major_rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'mississippi': 'united states',
    'chang jiang': 'china',
    'ob': 'russia',
    'huang he': 'china',
    'yenisei': 'russia',
    'parana' : 'argentina',
    }

for river, country in major_rivers.items():
    print("The " + river.title() + " runs through " +
          country.title() + ".")

print("\nThe following rivers have been mentioned:")
for river in sorted(major_rivers.keys()):
    print("- " + river.title())

print("\nThe following countries have been mentioned:")
for country in set(major_rivers.values()):
    print("- " + country.title())
