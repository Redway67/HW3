quantity_of_elements = int(input('Введите количество элементов:'))
digit_list = [int(input(f'Введите число для {i} элемента списка:')) for i in range(quantity_of_elements)]
print('Вывод: ', digit_list)
