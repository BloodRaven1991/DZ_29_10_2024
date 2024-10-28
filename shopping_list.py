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