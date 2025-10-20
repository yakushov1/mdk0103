# Создайте класс Employee с общими атрибутами, такими как name (имя), id (идентификационный номер)
#  и методами, например, get_info(), который возвращает базовую информацию о сотруднике.


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}"


# 2. Создайте класс Manager с дополнительными атрибутами, такими как department (отдел)
#  и методами, например, manage_project(), символизирующим управление проектами.


class Manager(Employee):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет проектами в отделе {self.department}"


# 3. Создайте класс Technician с уникальными атрибутами, такими как specialization (специализация),
#  и методами, например, perform_maintenance(), означающим выполнение технического обслуживания.


class Technician(Employee):
    def __init__(self, id, name, specialization):
        super().__init__(id, name)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} выполняет техническое обслуживание ({self.specialization})"


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
        self.team = []  # Список для хранения сотрудников

    def add_employee(self, employee):
        """Добавляет сотрудника в команду"""
        self.team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду"

    def get_team_info(self):
        """Возвращает информацию о всех сотрудниках команды"""
        if not self.team:
            return "В команде пока нет сотрудников"
        return "\n".join(employee.get_info() for employee in self.team)


# 7. Создайте объекты каждого класса и демонстрируйте их функциональность.

if __name__ == "__main__":
    # Создаем обычных сотрудников
    emp1 = Employee(1, "Иван Иванов")
    print(emp1.get_info())

    # Создаем менеджера
    mgr = Manager(2, "Петр Петров", "ИТ")
    print(mgr.manage_project())

    # Создаем техника
    tech = Technician(3, "Сергей Сергеев", "сети")
    print(tech.perform_maintenance())

    # Создаем TechManager
    tech_mgr = TechManager(4, "Алексей Алексеев", "Разработка", "базы данных")
    print(tech_mgr.manage_project())
    print(tech_mgr.perform_maintenance())

    # Добавляем сотрудников в команду
    print(tech_mgr.add_employee(emp1))
    print(tech_mgr.add_employee(tech))

    # Получаем информацию о команде
    print("\nИнформация о команде TechManager:")
    print(tech_mgr.get_team_info())
