from class_user import User


class UnregisteredUser(User):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"I am an unregistered user."


unregistered = UnregisteredUser()
print(unregistered.__repr__())
