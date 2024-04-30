from classes import HH
from class_vacancy import FromVacancy
from class_connector import SaveJson


hh_api = HH()

def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = FromVacancy.cast_to_object_list(hh_vacancies)
    sorted_vac = FromVacancy.sort_vacancies(vacancies_list)
    top_vac = FromVacancy.get_top_vacancies(sorted_vac, top_n)
    # filter_vac = FromVacancy.filter_vacations(sorted_vac, filter_words)

    print(top_vac)
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    #
    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
