from chapter09.e05_user.user import User

users = [{'first_name': 'John', 'middle_name': 'Walfgang', 'last_name': 'straus'},
         {'first_name': 'Micheal', 'middle_name': '', 'last_name': 'schumache'}]

for user in users:
    current_user = User(user['first_name'], user['last_name'], user['middle_name'])
    current_user.describe_user()
    current_user.greet_user()

    current_user.increment_login_attemps()
    current_user.increment_login_attemps()

    print(current_user.login_attempts)

    current_user.reset_login_attempts()
    print(current_user.login_attempts)
