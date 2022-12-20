def mixs(num):
    try:
        elem = int(num)
        return (0, elem, '')
    except ValueError:
        return (1, num, '')
print("Эта программа сортирует словарь по значениям.")
unsorted_dict = {0: 'Жак-Ив', 1: '11', 2: 10 ** 3, 3:'Black', 4: "060", 5: 0.07, 6: 1, 7: 'Heart', 8:'Кусто', 9:"#"}
print("Допустим, у нас есть словарь: ", unsorted_dict, ".", sep = "")
temp_values = []
for i in unsorted_dict:
	temp_values.append(unsorted_dict.get(i))
print("Возьмём из него список значений: ", temp_values, ".", sep = "")
temp_values.sort(key = mixs)
#res = sorted(temp_values, key = lambda ele: (0, int(ele))
#                        if ele.isdigit() else (1, ele))
#print(res)
print("Отсортируем: ", temp_values, ".", sep = "")
#for i, elem in enumerate(temp_values):
#	print(i, "-", elem)
temp_keys = unsorted_dict.keys()
print("Теперь возьмём список ключей: ", temp_keys, ".", sep = "")
sorted_dict = dict(zip(temp_keys, temp_values))
print("И создадим из двух списков новый отсортированный словарь:\n", sorted_dict, ".", sep = "")
input("Для завершения нажмите любую клавишу...")