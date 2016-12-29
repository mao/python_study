current_users = ['admin', 'Eric', 'Tom', 'Adam', 'Smith', 'John']

new_users = ['Eric', 'Rose', 'Jack', 'Abraham', 'smith', 'joHn']

for user in new_users:
    if user.lower() in [username.lower() for username in current_users ]:
        print('The user name:', user,'is already taken by others, please choose another one.')
    else:
        print('The user name:', user, 'is available')