from class_user import User


class Superuser(User):
    def __init__(self, username, password, first_name, last_name, gender):
        super().__init__(username, password, first_name, last_name, gender)

    def __repr__(self):
        return f"My name is {self.first_name} {self.last_name} and I am an unregistered user."
