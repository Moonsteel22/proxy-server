from typing import Generator


def test_prime():
    """
    Парочка тестов для функции
    :return:
    """

    assert tuple(get_prime_numbers(10)) == (2, 3, 5, 7)

    assert tuple(get_prime_numbers(20)) == (2, 3, 5, 7, 11, 13, 17, 19)


def get_prime_numbers(n: int) -> Generator[int, None, None]:
    """
    Функция реализует метод "Решето Эратосфена" для нахождения простых чисел.
    Решето Эратосфена "просеивает" числа бОльшие, чем искомое, которые на него делятся.
    Сложность - O(n*log(log(n))), доп.память - O(n)
    :param n: Число, до которого выводятся простые числа
    :return: генератор, возвращающий простое число
    """
    # генерируем список из True ( изначально полагаем, что все числа - простые )
    numbers: list[int] = [True for _ in range(n)]
    # Отсеиваем числа, которые имеют >2 делителей
    for i in range(2, n):
        for j in range(i**2, n, i):
            numbers[j] = False
    # Возвращаем числа
    for i in range(2, n):
        if numbers[i]:
            yield i


if __name__ == "__main__":
    test_prime()

    n = 50
    for i in get_prime_numbers(n):
        print(i, end="  ")
