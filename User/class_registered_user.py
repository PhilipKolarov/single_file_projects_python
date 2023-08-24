from abc import ABC, abstractmethod
from class_user import User


class RegisteredUser(User, ABC):
    GENDER_OPTIONS_MALE = ['male', 'Male', 'Man', 'man', 'M', 'm']
    GENDER_OPTIONS_FEMALE = ['female', 'Female', 'Woman', 'woman', 'W', 'w']

    def __init__(self, username, password, first_name, last_name, gender):
        super().__init__()
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = self.check_gender(gender)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def view_history(self):
        result = ''
        for el in self.history:
            result += f'{el}\n'
        result += ' ---------- '
        return result

    def check_gender(self, g):
        if g in self.GENDER_OPTIONS_MALE:
            return 'male'
        elif g in self.GENDER_OPTIONS_FEMALE:
            return 'female'
        else:
            return 'unspecified'

    def delete_history(self):
        self.history = []

    @abstractmethod
    def __repr__(self):
        pass
