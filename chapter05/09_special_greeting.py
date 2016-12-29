users = ['admin', 'Eric', 'Tom', 'Adam', 'Smith', 'John']

for user in users:
    if user == 'admin':
        print('Hello', user+',', 'would you like to see a status report?')
    else:
        print('Hello', user + ',', 'thank you for logging in again.')

users.clear()

if not users:
    print('We need to find some users!')