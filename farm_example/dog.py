from animal import Animal


class Dog(Animal):
    def __init__(self, name: str, preferred_food: set, age: int):
        super().__init__(name, preferred_food, age)
        self.say_word = "Гав-гав!"
        self.animal_type = "Собака"

        # del self.name антипаттерн, противоречит принципу наследования

    def treat(self, hours: int = 1) -> str:
        print(f"Мы гуляем с {self.name} {hours} часов и у нас поднимается настроение.")
        return "Хорошее настроение"
