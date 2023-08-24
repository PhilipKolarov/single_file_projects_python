from abc import ABC, abstractmethod


class User(ABC):
    GENDER_OPTIONS_MALE = ['male', 'Male', 'Man', 'man', 'M', 'm']
    GENDER_OPTIONS_FEMALE = ['female', 'Female', 'Woman', 'woman', 'W', 'w']

    @abstractmethod
    def __init__(self):
        self.history = []

    def open_page(self, page):
        self.history.append(f'Page - {page}')
