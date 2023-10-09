# Завдання 4
#
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

import random

digits_number = 20
numbers = []

for i in range(digits_number):
  numbers.append(random.randint (0,20))

print(numbers)

deleted_number = int(input("Enter the number you want to delete: "))



def delete_num (numbers, number):
    num_of_del = numbers.count(number)
    while number in numbers:
        numbers.remove(number)
    return num_of_del

num_of_del = delete_num(numbers, deleted_number)

print("Number pf deleted numbers = ",num_of_del)
print(numbers)
