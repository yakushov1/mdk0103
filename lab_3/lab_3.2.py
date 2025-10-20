# Задание 2: Работа с конструктором
# 1. Определите класс Circle для представления круга.
# 2. Используйте конструктор __init__ для инициализации радиуса круга (radius).
# 3. Добавьте метод get_radius(), который возвращает значение радиуса.
# 4. Добавьте метод set_radius(new_radius), который позволяет изменить радиус круга.
# 5. Создайте объект класса Circle, измените его радиус и выведите новый радиус на экран


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius


small_circle = Circle(5)

small_circle.set_radius(4)

print(small_circle.radius)
