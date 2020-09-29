from Impure_functions import create_list_names
from random import choice
import pytest


list_names = 'Денис Виктор Алена Вова Вадим Дарья Ева Захар Злата Григорий Матвей Яна Ася Петр Иван Дарина Галина ' \
             'Антон Алексей Виктор Влад Венера Дмитрий Лида Алина '


@pytest.fixture()
def my_data():
    n = choice(range(2, 100))
    new_list_names = create_list_names(list_names, n)
    n = choice(range(2, 100))
    new_list_names_2 = create_list_names(list_names, n)
    return new_list_names, new_list_names_2

def test_create_list_names(my_data):
    """
    Функция проверяет неравеснтво списков, т.к. списки не могут быть равны из-за "грязной функции"... хотя есть очень мизерная вероятность
    """
    assert my_data[0] != my_data[1]

def test_create_list_names_2(my_data):
    """
    Функция проверяет неравеснтво длин списков, т.к. списки не могут быть равны из-за "грязной функции"... хотя есть очень мизерная вероятность
    """
    assert len(my_data[0]) != len(my_data[1])