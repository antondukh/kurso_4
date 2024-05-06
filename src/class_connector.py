from abc import ABC, abstractmethod
import json
from classes import *


class EditingFile(ABC):

    @abstractmethod
    def add_vacancy(self, *agrs, **kwargs):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def del_vacancies(self):
        pass


class SaveJson(EditingFile):
    """
    Класс для сохранения и получения вакансий в JSON-файл
    """

    def __init__(self, file_):
        self.file_ = file_

    def add_vacancy(self, vacancy_data):
        with open(self.file_, 'a') as file:
            json.dump(vacancy_data, file)
            file.write('\n')

    def get_vacancies(self):
        with open(self.file_, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def del_vacancies(self):
        with open(self.file_, "w") as file:
            pass
