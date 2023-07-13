my_list = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7]
result = []
for item in my_list:
    if my_list.count(item) > 1 and item not in result:
        result.append(item)
print('Cписок повторяющихся элементов', my_list)
print('Список дублирующихся элементов без дубликатов', result)