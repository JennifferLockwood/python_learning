# 3-7_shriking_list.py

print("Hello everybody. Unfortunately I have to inform you " +
      "that I can invite only two people for dinner. :(")

guest_list = ['robi draco', 'margarita rosa', 'miryam troncoso',
               'sparky', 'wally', 'bachin']
popped_guest = guest_list.pop(0)
print('\nHello ' + popped_guest.title() + ", I'm sorry I can't invite you " +
      'to dinner tonight.')
popped_guest = guest_list.pop(0)
print('\nHello ' + popped_guest.title() + ", I'm sorry I can't invite you " +
      'to dinner tonight.')
popped_guest = guest_list.pop(1)
print('\nHello ' + popped_guest.title() + ", I'm sorry I can't invite you " +
      'to dinner tonight.')
popped_guest = guest_list.pop(1)
print('\nHello ' + popped_guest.title() + ", I'm sorry I can't invite you " +
      'to dinner tonight.')

print("\nHere are the new set of invitations:")
print(guest_list[0].title() + ", you're still invited!")
print(guest_list[1].title() + ", you're still invited!")

print("\nHere are the new invitations:")
for i in range(len(guest_list)):
    print(guest_list[i].title() + ", you're still invited!")

for i in range(len(guest_list)):
    del guest_list[i-1]
print(guest_list)

if guest_list == []:
    print("The guest list is empty, you sent all your invitations.")

