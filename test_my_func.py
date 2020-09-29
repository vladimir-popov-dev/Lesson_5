from divisor_master import isprime, decomposition, all_divisors
import pytest
import random

list_of_prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
assertion = True


@pytest.fixture()
def number():
    """
    Возвращает произвольное число
     """
    return random.choice(range(5, 500))


@pytest.fixture()
def any_division():
    """
    Возвращает кортеж из произвольного числа и произвольного делителеля этого числа
    """
    rand_number = random.choice(range(5, 1500))
    any_division = random.choice(all_divisors(rand_number))
    return any_division, rand_number


def test_isprime_prime():
    """
    Проверка функции на достоверность идентификации простых чисел
    :return: 
    """""
    for x in list_of_prime_number:
        assert isprime(x) == assertion


def test_isprime_isbool():
    """
    Проверка функции на возврат значения логического типа
    :return:
    """
    for x in list_of_prime_number:
        assert type(isprime(x)) == bool


def test_decomposit_number(number):
    """
    Функция проверяет произведение множетелей числа с самим (исходным) числом
    :param number: число которое расклыдвается на канонические множетели (decomposition) и заново множители перемножаются
    """
    test_number = 1
    for n in decomposition(number):
        test_number *= n
    assert test_number == number


def test_all_divisors(any_division):
    """
    проверяет условие деления без остатка числа на его произвольный делитель
    """
    assert any_division[1] % any_division[0] == 0
