# players.py

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print()
print(players[1:4])
print()
print(players[:4])
print()
print(players[2:])
print()
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print()
