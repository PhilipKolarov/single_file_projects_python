from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username, password, first_name, last_name, gender):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.history = []

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

    @abstractmethod
    def __repr__(self):
        pass

    def open_page(self, page):
        self.history.append(f'Page - {page}')

    def delete_history(self):
        self.history = []
