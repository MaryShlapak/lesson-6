# Завдання 1

# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random

digits_number = 5
numbers = []

for i in range(digits_number):
  numbers.append(random.randint (1,10))

print(numbers)


def num_mult(numbers):
    mult = 1
    for number in numbers:
        mult *= number
    return mult
result = num_mult(numbers)
print("result of multiplication = ", result)


# Завдання 2

# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random

digits_number = 5
numbers = []

for i in range(digits_number):
  numbers.append(random.randint (1,10))

print(numbers)

def min_num (numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

result = min_num(numbers)
print("The smallest number: ", result)

# Завдання 3

# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random

digits_number = 10
numbers = []

for i in range(digits_number):
  numbers.append(random.randint (1,20))

print(numbers)

def prime_num (number):
    if number <= 1:
        return False
    if number <= 3:
        return  True
    if number % 2 == 0 or number % 3 == 0:
        return False
    num = 5
    while num * num <= number:
        if number % num == 0 or number % (num + 2) == 0:
            return False
        num += 6
    return True


def prime_num_count (numbers):
    prime_count = 0
    for number in numbers:
        if prime_num(number):
            prime_count += 1
    return prime_count

result = prime_num_count(numbers)

print("The number of prime numbers in list:", result)


# З перевіркою на просте число підказали, хотілося б по можливості розібрати це на лекції