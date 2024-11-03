# TODO Напишите функцию для поиска индекса товара

def find_first_occurrence(items, target_item):
    for index, item in enumerate(items):
        if item == target_item:  # Сравниваем текущий элемент с искомым товаром
            return index  # Возвращаем индекс первого вхождения
    return None  # Если товар не найден, возвращаем None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = index_item = find_first_occurrence(items_list, find_item) # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
