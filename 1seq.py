# МОДУЛЬ 1

quantity_of_elements = int(input('Введите количество элементов:'))

# инициализируем список с вводом числа
digit_list = [int(input(f'Введите число для элемента списка с индексом {i}:')) for i in range(quantity_of_elements)]

print('Вывод: ', digit_list)
print('Длина списка = ', len(digit_list))
