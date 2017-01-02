class Privileges():
    def __init__(self, *privileges):
        self.privileges = []
        for p in privileges:
            self.privileges.append(p)

    def show_privileges(self):
        print('Privileges:', self.privileges)