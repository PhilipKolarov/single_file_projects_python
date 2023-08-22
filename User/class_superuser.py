from class_user import User


class Superuser(User):
    def __init__(self, username, password, first_name, last_name, gender):
        super().__init__(username, password, first_name, last_name, gender)
        self.commits = {}
        self.updates = {}
        self.deletes = {}

    def __repr__(self):
        return f"My name is {self.first_name} {self.last_name} and I am a superuser."

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

    @staticmethod
    def display_history_other_user(other_user):
        result = ''
        for el in other_user.history:
            result += f"{el} \n"

        result += ' --- '
        return result
