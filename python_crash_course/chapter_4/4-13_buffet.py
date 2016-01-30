# 4-13_buffet.py

menu = ('nutburger', 'millet burger', 'super nachos', 'vegetable taco',
        'burrito')

print("\nOur menu today is:")
for item in menu:
    print("- " + item.title())

new_menu = ('nutburger', 'grilled cheese', 'super nachos', 'avocado sandwich',
            'burrito')
print("\nOur menu has changed. Here is the new menu:")
for item in new_menu:
    print("- " + item.title())

# new_menu[0] = 'beef'      # intentional error
