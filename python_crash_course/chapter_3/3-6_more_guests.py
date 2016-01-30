# 3-6_more_guests.py

print("Hello everybody. I found a bigger dinner table for tonight!")

guest_list = ['robi draco', 'margarita rosa', 'miryam troncoso',
               'bachin']
guest_list.insert(0, 'sparky')
guest_list.insert(3, 'wally')
guest_list.append('joyce')

print("\nHere are the new set of invitations:")
print(guest_list[0].title() + ', join the Lockwoods for a fun dinner tonight!')
print(guest_list[3].title() + ', join the Lockwoods for a fun dinner tonight!')
print(guest_list[6].title() + ', join the Lockwoods for a fun dinner tonight!')

print("\nHere are the new invitations:")
for i in range(len(guest_list)):
    print(guest_list[i].title() +
          ', join the Lockwoods for a fun dinner tonight!')
