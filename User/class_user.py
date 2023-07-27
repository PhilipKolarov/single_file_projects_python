from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username, password, first_name, last_name, gender):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @abstractmethod
    def __repr__(self):
        pass
