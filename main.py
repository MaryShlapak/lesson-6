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
        return  False
    if number >= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    num = 5
    while num * num <= number:
        if number % num == 0 or number % (num + 2) == 0:
        return False
            num += 6
    return True

def prime_num_sum (numbers):
    prime = []
    for number in numbers:
        if prime_num(number):
            prime.append(number)
    return prime


result = prime_num_sum(numbers)
print("The number of prime numbers in list:", result)
