from chapter09.e05_user.user import User
from chapter09.e08_privileges.privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, middle_name=''):
        super().__init__(first_name, last_name, middle_name)

        self.privileges = Privileges('cna add post', 'can delete post', 'can ban user')

    def show_privileges(self):
        self.privileges.show_privileges()