from class_registered_user import RegisteredUser


class Admin(RegisteredUser):
    def __init__(self, username, password, first_name, last_name, gender):
        super().__init__(username, password, first_name, last_name, gender)
        self.commits = {}
        self.updates = {}
        self.deletes = {}

    def __repr__(self):
        return f"My name is {self.first_name} {self.last_name} and I am an admin."

    def commit(self, title, command):
        self.commits[title] = command
        self.history.append(f"Commit - {title}")

    def update(self, title, command):
        self.commits[title] = command
        self.history.append(f"Update - {title}")

    def delete(self, title, command):
        self.commits[title] = command
        self.history.append(f"Delete - {title}")

    def display_history(self):
        result = ''
        for el in self.history:
            result += f"{el} \n"

        result += ' --- '
        return result
