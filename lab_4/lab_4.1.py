# Задание 1: Защита данных пользователя
# 1. Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами:
#  имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password).
# 2. Используйте конструктор __init__ для инициализации этих атрибутов.
# 3. Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта.
# 4. Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль
#  текущему паролю аккаунта и возвращает True или False.
# 5. Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его
#  с помощью методов set_password и check_password.


class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, entered_password):
        return self.password == entered_password


new_user = UserAccount("Vasily", "test@test.ru", "abrakadabra")
print(f"Изначальный пароль: {new_user.password}")


new_user.set_password("ahalaimahalai")
print(f"Измененный пароль: {new_user.password}")


password_from_form = "abrakadabra"
print(new_user.check_password(password_from_form))

password_from_form = "ahalaimahalai"
print(new_user.check_password(password_from_form))
