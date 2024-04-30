class FromVacancy:
    """Класс для работы с вакансиями"""
    vacancies_list = []


    def __init__(self, name, url, salary_from, salary_to, currency, requirement):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirement = requirement

    @classmethod
    def cast_to_object_list(cls, raw_vacancies):
        """Преобразование набора данных в список объектов"""
        for item in raw_vacancies:
            if item['salary'] == None:
                vacancy = FromVacancy(item['name'], item['alternate_url'], 0, 0, 'Не указана',
                                      item['snippet']['requirement'])
            elif item['salary']['from'] == None:
                vacancy = FromVacancy(item['name'], item['alternate_url'], 0, item['salary']['to'], item['salary']['currency'],
                                      item['snippet']['requirement'])
            elif item['salary']['to'] == None:
                vacancy = FromVacancy(item['name'], item['alternate_url'], item['salary']['from'], 0, item['salary']['currency'],
                                      item['snippet']['requirement'])
            elif item['snippet']['requirement'] == None:
                vacancy = FromVacancy(item['name'], item['alternate_url'], item['salary']['from'], item['salary']['to'],
                                      item['salary']['currency'], 'Описания нет')
            else:
                vacancy = FromVacancy(item['name'], item['alternate_url'], item['salary']['from'], item['salary']['to'],
                                      item['salary']['currency'], item['snippet']['requirement'])
            cls.vacancies_list.append(vacancy)

        return cls.vacancies_list

    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Зарплата: {self.salary_from} - {self.salary_to} {self.currency}\n'
                f'Ссылка на вакансию: <{self.url}>\n'
                f'Описание: {self.requirement}\n'
                f'*****************\n'
                )

    @classmethod
    def sort_vacancies(cls, vacancies_list):
        """Возвращает отсортированные по зарплате вакансии"""

        sorted_vacancies = sorted(vacancies_list, key=lambda vacancy: vacancy.salary_from, reverse=True)

        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(sorted_vacancies, n: int):
        """Возвращает топ n вакансий"""

        top_vacancies = sorted_vacancies[0:n]
        return top_vacancies

    @staticmethod
    def filter_vacations(top_vacancies, filter_word):
        filter = []
        for item in top_vacancies:
            if filter_word in item.requirement:
                filter.append(item)
        return filter

