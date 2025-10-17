def sum_of_two(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


def is_prime(n: int) -> bool:
    """Возвращает true, если число простое.
    Простое число - натуральное число больше 1, которое делится без остатка на 1 и на само себя
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def max_of_two(a: int, b: int) -> str:
    """Принимает 2 числа и возвращает большее из них"""
    if a > b:
        result = f"Большее число: {a}"
    if a < b:
        result = f"Большее число: {b}"
    if a == b:
        result = "Числа равны"
    return result
