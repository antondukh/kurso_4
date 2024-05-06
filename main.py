from src.classes import HH
from src.class_vacancy import FromVacancy

hh_api = HH()


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос:-> ")
    top_n = int(input("Введите количество вакансий для вывода в топ N:-> "))
    filter_words = input("Введите ключевое слово для фильтрации вакансий:-> ")
    salary_range = input("Введите диапазон зарплат: Пример: 100000 - 150000 -> ").split(' ')
    hh_vacancies = hh_api.load_vacancies(search_query)

    vacancies_list = FromVacancy.cast_to_object_list(hh_vacancies)

    filter_vac = FromVacancy.filter_vacations(vacancies_list, filter_words)

    ranged_vacancies = FromVacancy.get_vacancies_by_salary(filter_vac, salary_range)

    sorted_vac = FromVacancy.sort_vacancies(ranged_vacancies)

    top_vac = FromVacancy.get_top_vacancies(sorted_vac, top_n)

    print(top_vac)


if __name__ == "__main__":
    user_interaction()
