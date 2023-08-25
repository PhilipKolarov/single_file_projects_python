from class_registered_user import RegisteredUser


class StandardRegisteredUser(RegisteredUser):
    def __init__(self, username, password, first_name, last_name, gender):
        super().__init__(username, password, first_name, last_name, gender)

    def __repr__(self):
        return f"My name is {self.first_name} {self.last_name} and I am a registered user."

    def display_history(self):
        result = ''
        for el in self.history:
            result += f"{el} \n"

        result += ' --- '
        return result
