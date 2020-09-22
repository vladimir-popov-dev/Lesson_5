from divisor_master import *

# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
for x in range(1, 30):
    if isprime(x):
        print(f'{x} - Простое число')
print()

number = 590

# 2) выводит список всех делителей числа;
print(f'Все делители числа {number}:  ', all_divisors(number))
print()

# 3) выводит самый большой простой делитель числа.
print(f'Наибольший простой делитель числа {number}:  ', superior_prime_divisor(number))
print()

# функция выводит каноническое разложение числа на простые множители;
print(f'Каноническое разложение {number} на простые множители :  ', decomposition(number))
print('Каноническое разложение 12 на простые множители :  ', decomposition(12))
print('Каноническое разложение 78 на простые множители :  ', decomposition(78))
print('Каноническое разложение 83006 на простые множители :  ', decomposition(83006))
print('Каноническое разложение 897924289 на простые множители :  ', decomposition(897924289))
print()

# функция выводит самый большой делитель, кроме самого числа (не обязательно простой) числа.
print(f'Наибольший делитель числа {number}, кроме самого числа {number}:  ', superior_divisor(number))
