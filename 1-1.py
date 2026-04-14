

#Функция для подсчёта числа элементов в списках, включая вложенные списки
# Итеративный вариант (через стек)
def count_iterative(data):
    if not data:
        return 0
    
    count = 0
    stack = [data]  # Кладём исходный список в стек
    
    while stack:
        current = stack.pop()  # Достаём текущий список
        for item in current:   # Проходим по всем элементам
            count += 1          # Считаем элемент
            if isinstance(item, list):
                stack.append(item)  # Если это список, кладём его в стек для дальнейшего обхода
    return count


print("\n--- Итеративный вариант ---")
print(f"count([]) -> {count_iterative([])}")                          # 0
print(f"count([1, 2, 3]) -> {count_iterative([1, 2, 3])}")           # 3
print(f"count(['x', 'y', ['z']]) -> {count_iterative(['x', 'y', ['z']])}")  # 4
print(f"count([1, 2, [3, 4, [5]]]) -> {count_iterative([1, 2, [3, 4, [5]]])}")  # 7

