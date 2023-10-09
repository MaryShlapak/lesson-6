# Завдання 6
#
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

import random

digits_number = 10
numbers = []

for i in range(digits_number):
  numbers.append(random.randint (1,10))

print(numbers)

power = int(input("Enter the power of numbers: "))

def num_pow (numbers, power):
    result = []
    for num in numbers:
        result.append(num ** power)
    return result

result = num_pow(numbers, power)

print("The list of numbers brought to a power: ", result)