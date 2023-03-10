text = """
The diesel engine, named after Rudolf Diesel, is an internal combustion
 engine in which ignition of the fuel is caused by the elevated temperature 
 of the air in the cylinder due to mechanical compression; thus, the diesel 
 engine is called a compression-ignition engine (CI engine). This contrasts 
 with engines using spark plug-ignition of the air-fuel mixture, such as a 
 petrol engine (gasoline engine) or a gas engine (using a gaseous fuel like 
 natural gas or liquefied petroleum gas)."""

text_words = text.split()


i = 0
while i < 10:
    print('Я поднимаюсь по лестнице')
    print(f'Я на {i} этаже')

    # две идентичные команды
    # i = i + 1
    i += 1
print('Я поднялся!')


# применима к любым спискам (итерируемым данным - те, которые поддерживают
# операцию subscribe/index: <переменная/значение>[<i-ый элемент>]
# все типы данных, которые это поддерживают, так же
# поддерживают слайсы: <переменная/значение>[<от i-ый элемент>:<до i-ый элемент>]
i = 0
len_text_words = len(text_words)
while i < len_text_words:
    print(text_words[i])
    i += 1


"""
while True:
    if time_to_exit:
        exit()
        # или
        break
"""
