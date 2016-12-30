class User():
    def __init__(self, first_name, last_name, middle_name=''):
        self.first_name = first_name.lower().title()
        self.last_name = last_name.lower().title()
        self.middle_name = middle_name.lower().title()
        self.login_attempts = 0

    def describe_user(self):
        print('User name:', self.first_name, self.middle_name, self.last_name)

    def greet_user(self):
        print('Hello,', self.first_name + '!')

    def increment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
