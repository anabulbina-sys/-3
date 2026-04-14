# Рекурсивный вариант
def x_rec(i):
    if i == 1:
        return 1.0
    if i == 2:
        return -1/8  # -0.125
    return ((i - 1) * x_rec(i - 1)) / 3 + ((i - 2) * x_rec(i - 2)) / 4

# Вывод первых 5 элементов для проверки
print("Последовательность x_i:")
for n in range(1, 6):
    print(f"x({n}) = {x_rec(n):.4f}")  # Исправлено: x_rec вместо x_iter