from divisor_master import isprime, decomposition, all_divisors, superior_prime_divisor
import pytest
import random

list_of_prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991]
assertion = True


@pytest.fixture()
def number():
    """
    Возвращает произвольное число
     """
    return random.choice(range(5, 800))


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


def test_superior_prime_divisor(number):
    """
    проверяет является наибольший простой делитель простым числом. (до 1000)
    """
    assert superior_prime_divisor(number) in list_of_prime_number