import csv
import json


def create_index(my_data: list, column_name: str) -> dict:
    """
    Функция создаёт индекс по колонке
    :param my_data: список словарей, каждый элемент списка имеет одинаковые ключи
    :param column_name: имя ключа, по которому делать индекс
    :return: индекс
    """
    my_index = dict()
    for data_entry in my_data:
        if data_entry[column_name] not in my_index:
            my_index[data_entry[column_name]] = list()
        my_index[data_entry[column_name]].append(data_entry)
    return my_index


def index_group_populations(my_index: dict) -> dict:
    population_dict = dict()
    for key, value in my_index.items():
        population_dict[key] = len(value)
    return population_dict


def display_index(my_index: dict):
    print(json.dumps(my_index, indent=4, sort_keys=True))


if __name__ == '__main__':
    # считываем ряды csv файла в список словарей
    # один элемент списка == один ряд
    # один ряд == словарь, где ключи - названия колонок
    with open('children.csv', newline='') as csvfile:
        # reader зависит от file handler`a csv file
        # следовательно, как и любой другой файл, его можно прочитать только один раз
        # затем нужно делать f.seek(0) или открыть заново
        reader = csv.DictReader(csvfile)
        # сразу прочитать всё содержимое файла
        data = list(reader)
        # цикл пустой, потому что list(reader) уже прочитало все данные
        for row in reader:
            print(row)
        """ # уже известный вариант с накоплением
        data = list()
        for row in reader:
            data.append(row)
        """
    for row in data:
        print(row)

    print('=' * 20, '\nAGE INDEX\n', '=' * 20)
    age_index = create_index(data, 'age')
    display_index(age_index)
    display_index(index_group_populations(age_index))

    print('=' * 20, '\nGROUP INDEX\n', '=' * 20)
    group_index = create_index(data, 'group')
    display_index(group_index)
    display_index(index_group_populations(group_index))

    print('=' * 20, '\nODESSA AGE INDEX\n', '=' * 20)
    # рекурсивный вызов функции
    # odessa_age_index = create_index(create_index(data, 'group')['Odessa'], 'age')
    # Рекурсию в Пайтоне мы ИЗБЕГАЕМ. Она занимает слишком много места в памяти и не отрабатывает должным образом
    # Лучше всего переписывать рекурсивные алгоритмы на циклы
    odessa_age_index = create_index(group_index['Odessa'], 'age')
    display_index(odessa_age_index)
    display_index(index_group_populations(odessa_age_index))
