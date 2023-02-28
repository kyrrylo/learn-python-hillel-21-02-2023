usd_to_uah = 39

user_input = input('Сколько USD вы хотите продать?')
# print(type(user_input))
amount_usd = float(user_input)
# amount_usd = user_input

# сообщаем пользователю исходные данные (что на входе)
print(f'У вас есть {amount_usd} USD, вы хотите их продать')

# считаем результат
amount_uah = usd_to_uah * amount_usd

# выводим результат
print(f'Вы продали {amount_usd} USD и получили {amount_uah} UAH')
