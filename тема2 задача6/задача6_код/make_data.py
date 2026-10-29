import numpy as np

np.random.seed(42)  # Фиксируем генератор случайных чисел для воспроизводимости

n_per_group = 100
n_extra = 3

# Три группы по 100 точек, значения intensity: 10, 50, 90
groups = []
for val in [10, 50, 90]:
    for _ in range(n_per_group):
        groups.append(val)

# Три дополнительные точки: 40, 60, 61
groups.extend([40, 60, 61])

intensity = np.array(groups, dtype=float)
n_total = len(intensity)  # 303

# Генерация случайных координат XYZ (в метрах, диапазон 0-10)
xyz = np.random.rand(n_total, 3) * 10.0

# Генерация уникальных ID: от 1 до 303
ids = np.arange(1, n_total + 1, dtype=int)

# Запись в файл: X Y Z intensity ID
with open("input_intensity.asc", "w") as f:
    for i in range(n_total):
        f.write(f"{xyz[i,0]:.6f} {xyz[i,1]:.6f} {xyz[i,2]:.6f} "
                f"{intensity[i]:.6f} {ids[i]}\n")

print(f"Сгенерировано {n_total} точек и сохранено в input_intensity.asc")
print(f"Точка с intensity=40: ID={ids[np.where(intensity==40)[0][0]]}")
print(f"Точка с intensity=60: ID={ids[np.where(intensity==60)[0][0]]}")
print(f"Точка с intensity=61: ID={ids[np.where(intensity==61)[0][0]]}")