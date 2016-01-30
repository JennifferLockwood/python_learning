# 3-5_changing_guest_list.py

guest_list = ['elvis', 'robi draco', 'margarita rosa', 'miryam troncoso',
               'bachin']
popped_guest = guest_list.pop(2)
print("Unfortunately " + popped_guest.title() + " can't make it tonight")
print("\nHere are the new invitations:")
guest_list.insert(2, 'sparky')
print(guest_list[0].title() + ', join the Lockwoods for a fun dinner tonight!')
print(guest_list[2].title() + ', join the Lockwoods for a fun dinner tonight!')
print(guest_list[4].title() + ', join the Lockwoods for a fun dinner tonight!')

print("\nHere are the new invitations:")
for i in range(len(guest_list)):
    print(guest_list[i].title() +
          ', join the Lockwoods for a fun dinner tonight!')
