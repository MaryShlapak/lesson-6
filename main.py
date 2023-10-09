# Завдання 5
#
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списк

first_list = input("Enter first list: ")
second_list = input("Enter second list: ")

def comb_list (first_list,second_list):
    combined = first_list + second_list
    return combined

result = comb_list(first_list,second_list)
print("Combined list: ", result)