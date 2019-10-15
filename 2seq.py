# МОДУЛЬ 2

digits_str = input('Ввведите любые цифры через запятую:').split(',')
digits = [int(i) for i in digits_str]

result = [j for j in digits if digits.count(j) == 1]
print(result)
