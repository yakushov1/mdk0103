# Задание 2: Полиморфизм и наследование
# 1. Определите базовый класс Vehicle с атрибутами: make (марка) и model
# (модель), а также методом get_info(), который возвращает информацию о
# транспортном средстве.
# 2. Создайте класс Car, наследующий от Vehicle, и добавьте в него атрибут
# fuel_type (тип топлива). Переопределите метод get_info() таким образом,
# чтобы он включал информацию о типе топлива.


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return (
            f"Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}"
        )


test_data = [Car("audi", "А4", "бензин"), Vehicle("Jeep", "Wrangler")]


for item in test_data:
    print(item.get_info())
