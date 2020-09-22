from math import sqrt


# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сам
def isprime(x):
    """
    Функция проверяет простое  число или нет, возвращает True или False

    :param x: Проверяемое число
    :return: True or False
    """
    try:
        x = int(x)
        if x == 1:
            return False
        else:
            outer = x if x < 100 else int(sqrt(x)) # для больших чисел, чтобы снизить кол-во циклов
            for i in range(2, outer):
                if x % i == 0:
                    return False
            return True
    except ValueError:
        print('Ошибка входных данных.Это не число.')


# 2) выводит список всех делителей числа;
def all_divisors(x):
    """
    Функция возращает список всех делителей числа

    :param x: Число для которого необходимо найти делители
    :return: список делителей
    """
    try:
        divisors = []
        for i in range(1, x + 1):
            if x % i == 0:
                divisors.append(i)
        return divisors
    except ValueError:
        print('Ошибка входных данных.Это не число.')


# 3) выводит самый большой простой делитель числа.

def superior_prime_divisor(x):
    """
    Функция возращает самый большой простой делитель числа

    :param x: Число для которого необходимо найти делитель
    :return: самый большой простой делитель
    """
    try:
        for i in range(x + 1, 1, -1):
            if x % i == 0:
                if isprime(i):
                    return i
    except ValueError:
        print('Ошибка входных данных.Это не число.')


# функция выводит каноническое разложение числа на простые множители;
def decomposition(x):
    """
    Функция возращает массив канонического разложение числа

    :param x: Число которое необходимо разложить
    :return: массив канонического разложение числа
    """
    try:
        prime_divisors = []
        if isprime(x):
            prime_divisors.append(x)
        else:
            outer = x if x < 900000 else int(sqrt(x))  # для больших чисел, чтобы снизить кол-во циклов
            for i in range(2, outer):
                if isprime(i):
                    while x % i == 0:
                        # print(i)
                        prime_divisors.append(i)
                        x /= i
        return prime_divisors
    except ValueError:
        print('Ошибка входных данных.Это не число.')


# функция выводит самый большой делитель (не обязательно простой) числа (кроме самого числа).
def superior_divisor(x):
    """
    Функция возращает самый большой делитель числа, кроме самого числа!!!

    :param x: Число для которого необходимо найти делитель
    :return: самый большой делитель
    """
    try:
        new_list = all_divisors(x)
        new_list.sort(reverse=True)
        return new_list[1]
    except ValueError:
        print('Ошибка входных данных.Это не число.')


if __name__ == '__main__':
    pass
    # для тестов.