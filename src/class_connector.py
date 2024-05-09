from abc import ABC, abstractmethod
import json

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

    def __init__(self, __file_):
        self.__file_ = 'data/vacantions.json'

    @staticmethod
    def add_vacancy(x):
        """Добавление вакансий"""
        with open('data/vacantions.json', 'w', encoding="utf8") as file:
            json.dump(x, file)
            file.write('\n')

    def get_vacancies(self):
        """Просмотр вакансий"""
        with open(self.__file_, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def del_vacancies(self):
        """Удаление вакансий"""
        with open(self.__file_, "w") as file:
            pass
