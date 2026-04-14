

# Итеративный вариант (оптимальный по памяти)
def x_iter(n):
    if n == 1: return 1.0
    if n == 2: return -0.125
    
    x1, x2 = 1.0, -0.125
    for i in range(3, n + 1):
        xi = ((i - 1) * x2) / 3 + ((i - 2) * x1) / 4
        x1, x2 = x2, xi
    return x2

# Вывод первых 5 элементов для проверки
print("Последовательность x_i:")
for n in range(1, 6):
    print(f"x({n}) = {x_iter(n):.4f}")