# 3-4_guest_list.py

guests_list = ['elvis', 'robi draco', 'margarita rosa', 'miryam troncoso',
               'bachin']
print(guests_list[0].title() + ', join the Lockwoods for a fun dinner tonight!')
print(guests_list[2].title() + ', join the Lockwoods for a fun dinner tonight!')
print(guests_list[4].title() + ', join the Lockwoods for a fun dinner tonight!')
print()

for i in range(len(guests_list)):
    print(guests_list[i].title() +
          ', join the Lockwoods for a fun dinner tonight!')
