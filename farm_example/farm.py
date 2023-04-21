from animals import Animal, Dog, Hen, Cow
from random import choices


def anti_polymoprhism_example(animals: list):
    """
    Отвечает за демонстрацию метода isinstance и работы с другими объектами не класса Animal
    Если найдено голодное животное, сообщает об этом
    :param animals: список животных Animals
    """
    animals.append('Оса')
    animals.append(5)
    animals.append([3, 4, 'Шершень'])
    for animal in animals:
        # if type(5) == int
        # if type(animal) == Dog
        # то же самое, что и выше, но рекомендуется сравнивать типы именно через isinstance
        if isinstance(animal, Animal):
            print(f'Найден представитель типа данных Animal: {animal}')
            if animal.hungry:
                print(f"На вашей ферме голодное животное! {animal}")
        else:
            print(f"{animal} не с нашей фермы.")

def polymorphism_example(animals: list):
    """
    Отвечает за симуляцию обычного дня разных животных на ферме
    В конце дня подводит итоги
    :param animals: список животных, наследников класса Animal
    """
    # пример полиморфизма - одинаковые названия функций, но разные классы и разная логика выполнения.
    food_to_offer = ['мясо', 'сало', 'борщ', "пшено", "крупа", "вода", "трава", "сено"]
    what_we_lost = list()
    what_we_get = list()
    for animal in animals:
        print('\n', animal, type(animal))
        animal.say()
        for food in choices(food_to_offer, k=3):
            animal.eat(food)
            what_we_lost.append(food)
        what_we_get.append(animal.treat())
    print()
    print(f'Ухаживая за животными, мы потеряли: {what_we_lost}')
    print(f'Ухаживая за животными, мы получили: {what_we_get}')


def test_animal_class(a: Animal):
    """
    Создаёт класс типа Animal и тестирует его основные возможности
    :return:
    """
    print(a, type(a))
    # то что перед точкой - пайтон ставит ПЕРВЫМ аргументом метода. SELF
    a.say()
    a.eat('печенька')
    a.treat()
    a.name = 'Не Чупакабра'
    a.age = 5
    print(a.hungry)
    a.eat('???')
    print(a.hungry)
    a.hungry = 10
    print(a)
    a.say()


if __name__ == '__main__':
    # смотрим как работает класс Animal
    an_animal = Animal('Чупакабра', {'???'}, -1)
    test_animal_class(an_animal)
    # создаём список представителей наследников класса Animal
    farm_animals = [
        Dog('Напас', {'мясо', 'сало', 'борщ'}, 14),
        Hen('Ряба', {"пшено", "крупа", "вода"}, 2),
        Cow('Бурёнка', {"трава", "сено"}, 5)
    ]
    # смотрим на пример полиморфизма этих наследников
    polymorphism_example(farm_animals)
    # смотрим на пример отсеивания "своих" от "чужих" среди наследников Animal
    anti_polymoprhism_example(farm_animals)
