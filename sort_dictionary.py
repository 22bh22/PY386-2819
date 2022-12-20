def mixs(num):
    try:
        elem = int(num)
        return (0, elem, '')
    except ValueError:
        return (1, num, '')
print("Эта программа сортирует словарь по значениям.")
unsorted_dict = {0: 'Жак-Ив', 1: '22', 2: 20 ** 20, 3: 'Black', 4: '060', 5: 0.07, 6: 1, 7: 'Heart', 8: 'Кусто', 9: '#', 10: '22', 11: '123', 15: 22, 14: -5, 13: chr(32) * 4, 21: chr(10)}
print('Допустим, у нас есть словарь: ', unsorted_dict, '.', sep = '')
temp_values = []
for i in unsorted_dict:
	temp_values.append(unsorted_dict.get(i))
print('Возьмём из него список значений: ', temp_values, '.', sep = '')
temp_values.sort(key = mixs)
print('Отсортируем: ', temp_values, '.', sep = '')
temp_keys = unsorted_dict.keys()
print('Теперь возьмём список ключей: ', temp_keys, '.', sep = '')
sorted_dict = dict(zip(temp_keys, temp_values))
print('И создадим из двух списков новый отсортированный словарь:\n', sorted_dict, '.', sep = '')
input('Для завершения нажмите любую клавишу...')