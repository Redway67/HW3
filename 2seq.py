# МОДУЛЬ 2

# Если не использовать import re
digits_str = input('Ввведите любые цифры через запятую (слэш или точку с запятой):') \
    .replace(';', ',').replace('/', ',').split(',')

digits = [int(i) for i in digits_str]

result = [j for j in digits if digits.count(j) == 1]
print(result)
