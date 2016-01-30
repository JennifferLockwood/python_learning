# 5-10_checking_usernames.py

print("TRY IT YOURSELF 5-10.")

current_users = ['jlockwood2016', 'admin', 'sparky2013',
                 'wally2014', 'cchiquitin8']
new_users = ['epresley1950', 'sparky2013', 'rdraco2000',
             'wally2014', 'mtroncoso2005']

for user in new_users:
    if user in current_users:
        print(user + " is already used.")
        print("You need to enter a new username.\n")
    else:
        print(user + " is available.\n")

print("Thank you for registering in our website. See you soon.")
