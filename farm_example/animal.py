class Animal:
    # initialization
    # вызывается автоматически при создании объекта класса
    # Animal.__init__() то же самое, что Animal()
    def __init__(self, name: str, preferred_food: set, age: int):
        self.name = name
        self.preferred_food = preferred_food
        self.age = age

        self.say_word = "???"
        self.animal_type = "Животное"
        self.hungry = True

        # return self представьте что оно здесь так

    def __str__(self):
        return f"{self.animal_type} по имени {self.name}, {self.age} лет."

    def eat(self, food: str):
        if food in self.preferred_food:
            print(f"{self.name} кушает {food}")
            self.hungry = False
        else:
            print(f"{self.name} такое не ест: {food}")

    def say(self):
        print(f"{self.name} говорит: {self.say_word}")

    def treat(self, hours: int = 1):
        print(f"Вы ухаживаете за {self.name} {hours} час(ов)")
        if self.hungry:
            print(f"{self.name} голодное!")
