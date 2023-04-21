# передача параметров в функцию по порядку
def my_function_args(arg1, arg2, arg3):
    print(f'{arg1=}')
    print(f'{arg2=}')
    print(f'{arg3=}')


# передача параметров в функцию по ключу
def my_function_kwargs(arg1=1, arg2=1, arg3=1):
    print(f'{arg1=}')
    print(f'{arg2=}')
    print(f'{arg3=}')


def my_function_dymanic(*args, **kwargs):
    # args - список аргументов по порядку
    print(f'{args=}')
    # kwargs - словарь аргументов по ключу
    print(f'{kwargs=}')


def my_function_init_example(**kwargs):
    # kwargs - словарь аргументов по ключу
    print(f'{kwargs=}')
    date = kwargs['date']
    time = kwargs['time']


if __name__ == '__main__':
    my_function_args(1, 3, 2)

    my_function_kwargs(2, arg3=1, arg2=3)

    my_function_dymanic(1, 2, argX=3)

    # date="05-Mar-2022"
    row = {"date": "05-Mar-2022", "time": "20:28:53", "sku": "KP3497", "warehouse": "A25", "warehouse_cell_id": "2308", "operation": "first_arrival", "invoice": "22804686", "expiration_date": "07-Jan-2023", "operation_cost": "-24365.24", "comment": "operation_cost = purchase_cost + delivery_cost"}
    my_function_init_example(**{"date": "05-Mar-2022", "time": "20:28:53", "sku": "KP3497", "warehouse": "A25", "warehouse_cell_id": "2308", "operation": "first_arrival", "invoice": "22804686", "expiration_date": "07-Jan-2023", "operation_cost": "-24365.24", "comment": "operation_cost = purchase_cost + delivery_cost"})
    my_function_init_example(date=row['date'], time=row['time'], sku=row['sku'])
