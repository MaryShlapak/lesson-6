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