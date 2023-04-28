def my_func(x: int):
    return x ** 2 + 4


def my_sorting_key(x):
    print(x, type(x))
    return x[0].lower()


if __name__ == '__main__':
    f = my_func
    # функция - это тоже тип данных. Неявный тип данных
    print(f, type(f))
    print(f(3))
    print(f(6))
    print(f(2))

    # анонимные однострочные функции
    f_lambda = lambda x: x ** 2 + 4
    print(f_lambda, type(f_lambda))

    print(sorted([-10, 2, -5, 3, 4, 1, 50], key=lambda x: abs(x)))

    print('Sorted', sorted({'Orange': 3, 'Banana': 5, 'apple': 1, 'kiwi': 3}.items(), key=my_sorting_key))
    print('Sorted', sorted({'Orange': 3, 'Banana': 5, 'apple': 1, 'kiwi': 3}.items(), key=lambda x: x[1]))

    # синтаксис lambda функции
    # lambda <перечень входных параметров через запятую>: <возвращаемое значение>
    z = lambda x, y: x + y
    print(z(3, 4))

    # в <возвращаемое значение> можно впихнуть if/else вот так:
    # <возвращается когда true> if <проверяемое условие> else <возвращается когда false>
    z = lambda x, y: x + y if x > 0 else -1
    print(z(3, 4))
    print(z(-10, 4))

    # работает не только в lambda функциях
    print(12 + 10 if 5 > 0 else -1)
    print(12 + 10 if 5 > 10 else -1)
