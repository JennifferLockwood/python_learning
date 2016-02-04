# Start with a list called sandwich_orders,
# and an empty list to hold finished sandwiches.
sandwich_orders = ['smokehouse', 'italian', 'turkey breast', 'veggie patty']
finished_sandwiches = []

# Print a message for each order.
# Move each finished order into the list of finished sandwiches.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich.title() + " sandwich.")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())