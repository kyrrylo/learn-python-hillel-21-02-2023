# имя + параметры/аргументы = сигнатура функции
def get_user_float(comment: str):
    # внутри функции - локальная область видимости
    while True:
        try:
            z = input(comment)
            return float(z)
        except Exception:
            print('Число!!!')


def get_user_int(comment: str):
    # внутри функции - локальная область видимости
    while True:
        try:
            z = input(comment)
            return int(z)
        except Exception:
            print('Число!!!')
