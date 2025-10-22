# Лабораторная работа по ООП
# Система управления сотрудниками

# 1. Создайте класс Employee с общими атрибутами, такими как name (имя), id (идентификационный номер)
# и методами, например, get_info(), который возвращает базовую информацию о сотруднике.


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_info(self):
        return f"ID: {self.id}, Имя: {self.name}"

    def work(self):
        return f"Сотрудник {self.name} работает"


# 2. Создайте класс Manager с дополнительными атрибутами, такими как department (отдел)
# и методами, например, manage_project(), символизирующим управление проектами.


class Manager(Employee):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет проектами в отделе '{self.department}'"

    def work(self):
        return f"Менеджер {self.name} управляет отделом '{self.department}'"


# 3. Создайте класс Technician с уникальными атрибутами, такими как specialization (специализация),
# и методами, например, perform_maintenance(), означающим выполнение технического обслуживания.


class Technician(Employee):
    def __init__(self, id, name, specialization):
        super().__init__(id, name)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} выполняет работу по специализации '{self.specialization}'"

    def work(self):
        return f"Техник {self.name} специализируется на '{self.specialization}'"


# 4. Создайте класс TechManager, который наследует как Manager, так и Technician.
# Этот класс должен комбинировать управленческие способности и технические навыки, например, иметь методы для
# управления проектами и выполнения технического обслуживания.

# 5. Добавьте метод add_employee(), который позволяет TechManager
# добавлять сотрудников в список подчинённых.

# 6. Реализуйте метод get_team_info(), который выводит информацию о всех подчинённых сотрудниках.


class TechManager(Manager, Technician):
    def __init__(self, id, name, department, specialization):
        # Вызываем конструктор Employee напрямую
        Employee.__init__(self, id, name)
        self.department = department
        self.specialization = specialization
        self.team = []  # список подчиненных

    def add_employee(self, employee):
        """Добавляет сотрудника в команду"""
        self.team.append(employee)
        return f"Добавлен сотрудник: {employee.name}"

    def get_team_info(self):
        """Возвращает информацию о всех сотрудниках команды"""
        if len(self.team) == 0:
            return "В команде нет сотрудников"

        result = f"Команда менеджера {self.name}:\n"
        for emp in self.team:
            result += f"- {emp.get_info()}\n"
        return result

    def work(self):
        return f"TechManager {self.name} управляет отделом '{self.department}' и специализируется на '{self.specialization}'"

    # Переопределяем методы для более точного отображения
    def manage_project(self):
        return (
            f"TechManager {self.name} управляет проектами в отделе '{self.department}'"
        )

    def perform_maintenance(self):
        return f"TechManager {self.name} выполняет техническую работу по специализации '{self.specialization}'"


# 7. Создайте объекты каждого класса и демонстрируйте их функциональность.

print("=== СИСТЕМА УПРАВЛЕНИЯ СОТРУДНИКАМИ ===\n")

# Создаем сотрудников
employee1 = Employee(1, "Иван Иванов")
manager1 = Manager(2, "Петр Петров", "ИТ отдел")
technician1 = Technician(3, "Сергей Сергеев", "компьютерные сети")
tech_manager1 = TechManager(4, "Алексей Алексеев", "Разработка", "базы данных")

# Демонстрируем функциональность

print("1. Информация о сотрудниках:")
print(employee1.get_info())
print(manager1.get_info())
print(technician1.get_info())
print(tech_manager1.get_info())

print("\n2. Демонстрация полиморфизма (метод work()):")
staff = [employee1, manager1, technician1, tech_manager1]
for person in staff:
    print(person.work())

print("\n3. Специальные методы:")
print(manager1.manage_project())
print(technician1.perform_maintenance())

print("\n4. Работа TechManager (множественное наследование):")
print(tech_manager1.manage_project())  # метод от Manager, но переопределен
print(tech_manager1.perform_maintenance())  # метод от Technician, но переопределен

print("\n5. Управление командой (методы TechManager):")
tech_manager1.add_employee(employee1)
tech_manager1.add_employee(technician1)
print(tech_manager1.get_team_info())

print("\n6. Собственный метод work() для TechManager:")
print(tech_manager1.work())

print("\n=== ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА ===")
