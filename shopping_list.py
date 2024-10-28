'''Создайте модуль "shopping_list.py", который будет реализовывать функционал списка покупок. 
Внутри должны быть функции add_item (для добавления в список, например «Хлеб, 2», где «Хлеб» - 
ключ, «2» - значение, которой по умолчанию в функции равно 0), remove_item для удаления покупки 
из списка, edit_quantity для редактирования количества (то есть значения), view_list для 
отображения всего списка (то есть словаря). Создайте новый файл, куда вы импортируете созданный 
модуль и отобразите работу каждый из этих функций. Например, пользователь сначала добавил в 
список три покупки: Хлеб – 2, Молоко, Яйца – 10, далее посмотрел этот список; потом он понял, 
что не хочет молоко, удалил его, посмотрел измененный список; потом решил, что 10 яиц – это 
много, и поменял их количество на 7 и в конце решил посмотреть на итоговый список.

Дополнительно: улучшите функционал, если вы, конечно, изначально так не сделали, следующим 
образом. Если добавляемый объект уже содержится в списке (например, «Хлеб» уже есть, но мы 
хотим добавить его еще раз), то он не добавляет в словарь новую строку, а прибавляет количество 
(значение) к этому же наименованию. Заодно повторите работу со словарями '''


Shopping_list = []

def add_item(item, quantity=0):
    for i, (existing_item, existing_quantity) in enumerate(Shopping_list):
        if existing_item == item:
            Shopping_list[i] = (existing_item, existing_quantity + quantity)
            return f"Товар '{item}' обновлен. Новое количество: {Shopping_list[i][1]}"
    Shopping_list.append((item, quantity))
    return f"Товар '{item}' добавлен в список с количеством: {quantity}"

def remove_item(item):
    for i, (existing_item, _) in enumerate(Shopping_list):
        if existing_item == item:
            Shopping_list.remove(Shopping_list[i])
            return f"Товар '{item}' удален из списка."
    return f"Элемент '{item}' не найден в списке."

def edit_quantity(item, quantity):
    for i, (existing_item, _) in enumerate(Shopping_list):
        if existing_item == item:
            Shopping_list[i] = (existing_item, quantity)
            return f"Количество товара '{item}' обновлено на: {quantity}"
    return f"Элемент '{item}' не найден в списке."

def view_list():
    if not Shopping_list:
        return "Список покупок пуст."
    else:
        result = "Список покупок:\n"
        for item, quantity in Shopping_list:
            result += f"{item}: {quantity}\n"
        return result.strip()