def mixs(num):
    try:
        elem = int(num[0])
        return (0, elem, '')
    except ValueError:
        return (1, num, '')

def print_list(my_list):
	print('[')
	for i, elem in enumerate(my_list):
		if i < len(my_list) - 1:
			print(elem, ",", sep = "")
		else:
			print(elem)
	print(']')
	
print("Эта программа сортирует словарь по значениям.")
unsorted_dict = {0: 'Жак-Ив', 1: '22', 2: 20 ** 20, 
3: 'Black', 4: '060', 5: 0.07, 6: 1, 7: 'Heart',
8: 'Кусто', 9: '#', 10: '22', 11: '123', 15: 22,
14: -5, 13: chr(10), 21: chr(32)* 4}
print('Допустим, у нас есть словарь:\nКлюч\tЗначение')
for i in unsorted_dict:
	print(i, "\t", unsorted_dict.get(i))
list_from_dict = []
for i in unsorted_dict:
	temp_lst = [unsorted_dict.get(i), i]
	list_from_dict.append(temp_lst)
print('\nСделаем из него список списков из значений и ключей:')
print_list(list_from_dict)
list_from_dict.sort(key = mixs)
list_of_keys = []
list_of_values = []
print('\nОтсортируем:')
print_list(list_from_dict)
for i in list_from_dict:
	list_of_keys.append(i[1])
	list_of_values.append(i[0])
#print(list_of_keys)
#print(list_of_values)
sorted_dict = dict(zip(list_of_keys, list_of_values))
print('\nИ создадим из двух списков новый отсортированный словарь:\nКлюч\tЗначение')
for i in sorted_dict:
	print(i, "\t", sorted_dict.get(i))
input('Для завершения нажмите любую клавишу...')
