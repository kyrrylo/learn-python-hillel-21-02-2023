from input_number import get_user_int

MENU = [
    ('Чай', 10),
    ('Эспрессо', 12),
    ('Американо', 12),
    ('Малиновый пончик', 15),
    ('Шоколадный пончик', 15),
    ('Круассан', 15)
]


def display_menu():
    """
    Пользуется константой MENU чтобы красиво и читаемо вывести на экран меню
    """
    print('Меню:')
    for menu_entry in MENU:
        name, price = menu_entry
        # https://pyformat.info
        # '{:10}'.format('test') ==  f'{"test":10}' одно и то же
        print(f'  {name:20} {price:.2f} UAH')


if __name__ == '__main__':
    # для поиска что есть в меню, а чего нет, будем использовать set()
    menu_set = set()
    for menu_entry in MENU:
        menu_set.add(menu_entry[0].lower())
    # print(menu_set)

    user_pouch = get_user_int('Сколько у вас денег (UAH)? ', 0)

    while True:
        # даём возможность выйти
        to_exit = input(f'Нажмите enter чтобы сделать заказ или введите exit чтобы уйти... ').lower()
        # выходим
        if to_exit == 'exit':
            break
        # отображаем меню
        display_menu()
        # берем данные о заказе
        order = input(f'У вас есть {user_pouch:.2f} UAH. Что будете заказывать? ').lower()
        # заказ есть в меню
        if order in menu_set:
            # ищем информацию о заказе в меню
            for menu_entry in MENU:
                # нашли
                if menu_entry[0].lower() == order:
                    # сравниваем цену из информации о заказе с средствами клиента
                    if user_pouch >= menu_entry[1]:
                        # средств хватает, вычитываем нужную сумму
                        user_pouch -= menu_entry[1]
                        # выдаём заказ
                        print(f'{menu_entry[0]} подано, с вас {menu_entry[1]:.2f} UAH')
                    # средств не хватает
                    else:
                        print(f'{menu_entry[0]} стоит {menu_entry[1]:.2f} UAH. У вас не хватает!')
                    # нужный заказ найден, можно дальше не искать
                    break
        else:
            # такие заказы здесь не принимают!
            print(f'У нас нет {order}!')


# x = x + 2 то же самое x += 2
# x = x - 5 то же самое x -= 5
# x = x * 2 то же самое x *= 2
# x = x / 5 то же самое x /= 5
