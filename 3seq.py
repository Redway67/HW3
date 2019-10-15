# МОДУЛЬ 3

# Первый список
digits_str = input('Введите элементы 1-го списка (через запятую):').split(',')
first_list = [int(i) for i in digits_str]

# Второй список
digits_str = input('Введите элементы 2-го списка (через запятую):').split(',')
second_list = [int(i) for i in digits_str]

result = [j for j in first_list if j not in second_list]

print(result)

# что значит "проверить на разных списках"?
# если списки с разными типами, то можно убрать приведение к целому, должно работать.