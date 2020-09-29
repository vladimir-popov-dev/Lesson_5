import random


def create_list_names(strin, n):
    """
    Возвращает новый рандомный список из n элементов
    :param strin: список имен
    :param n: желаемая длина нового списка
    :return: список случайных имен
    """
    words = strin.split()
    lists = []
    for x in range(0, n + 1):
        lists.append(words[random.randint(0, len(words) - 1)])
    return lists


if __name__ == '__main__':
    pass
