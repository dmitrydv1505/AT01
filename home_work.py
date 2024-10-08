def calculate_remainder(dividend, divisor):

    # Вычисляет остаток от деления dividend на divisor.

    :param dividend: 5 #Делимое
    :param divisor: 6 #Делитель
    :return: Остаток от деления
    :raises ZeroDivisionError: Если divisor равен нулю

    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return dividend % divisor

# Тесты для функции calculate_remainder
def test_calculate_remainder():
    # Тест на корректный остаток
    assert calculate_remainder(10, 3) == 1, "Тест не пройден: 10 % 3 должно быть 1"
    assert calculate_remainder(20, 5) == 0, "Тест не пройден: 20 % 5 должно быть 0"
    assert calculate_remainder(7, 4) == 3, "Тест не пройден: 7 % 4 должно быть 3"

    # Тест на отрицательные числа
    assert calculate_remainder(-10, 3) == 2, "Тест не пройден: -10 % 3 должно быть 2"
    assert calculate_remainder(10, -3) == -2, "Тест не пройден: 10 % -3 должно быть -2"
    assert calculate_remainder(-10, -3) == -1, "Тест не пройден: -10 % -3 должно быть -1"

    # Тест на деление на ноль
    try:
        calculate_remainder(10, 0)
        assert False, "Тест не пройден: Должно выброситься исключение ZeroDivisionError"
    except ZeroDivisionError:
        pass

    print("Все тесты пройдены.")

# Запуск тестов
test_calculate_remainder()