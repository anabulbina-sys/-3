
#Функция для подсчёта числа элементов в списках, включая вложенные списки
#С РЕКУРСИЕЙ
# Рекурсивный вариант
def count_recursive(data):
    total = 0
    for item in data:
        total += 1  # Считаем сам элемент
        if isinstance(item, list):
            total += count_recursive(item) # Считаем содержимое
    return total

# Проверка для всех примеров с картинки
print(f"count([]) -> {count_recursive([])}")           # 0
print(f"count([1, 2, 3]) -> {count_recursive([1, 2, 3])}")  # 3
print(f"count(['x', 'y', ['z']]) -> {count_recursive(['x', 'y', ['z']])}")  # 4
print(f"count([1, 2, [3, 4, [5]]]) -> {count_recursive([1, 2, [3, 4, [5]]])}")  # 5? или 7?
