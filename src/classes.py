import requests
import json
from abc import ABC, abstractmethod


class HHabstract(ABC):
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(HHabstract):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def load_vacancies(self, keyword):
        """Выполняет запрос по ключевому слову и записывает в файл.json"""
        vacan = []
        self.params['text'] = keyword
        while self.params.get('page') != 1:
            response = requests.get(self.__url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            vacan.extend(vacancies)
            self.params['page'] += 1

        return vacan


if __name__ == '__main__':
    g = HH()
    print(g.load_vacancies('python'))

