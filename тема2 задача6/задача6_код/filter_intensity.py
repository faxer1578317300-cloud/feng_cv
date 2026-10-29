import numpy as np
import matplotlib.pyplot as plt

# 1. Чтение исходного файла
# Порядок столбцов: X Y Z intensity ID
data = np.loadtxt("input_intensity.asc")

xyz = data[:, 0:3]        # X, Y, Z
intensity = data[:, 3]    # intensity
ids = data[:, 4].astype(int)  # ID

print("Общее количество точек:", len(intensity))

# 2. Создание маски с включением границ: 40 <= intensity <= 60
mask = (intensity >= 40) & (intensity <= 60)

# Применение ко всем атрибутам одновременно
xyz_sel = xyz[mask]
intensity_sel = intensity[mask]
ids_sel = ids[mask]

print("Количество точек после фильтрации:", len(intensity_sel))
print("Диапазон ID после фильтрации: от", ids_sel.min(), "до", ids_sel.max())

'''3. Проверка результатов'''
# Проверка количества точек
assert len(intensity_sel) == 102, f"Ожидалось 102 точки, фактически {len(intensity_sel)}"

# Проверка диапазона intensity
print("Минимальное значение intensity:", intensity_sel.min())  # Должно быть 40
print("Максимальное значение intensity:", intensity_sel.max())  # Должно быть 60

# Проверка исключения значения 61
assert 61 not in intensity_sel
print("Значение 61 успешно исключено")

# Проверка, что вся группа со значением 50 включена
count_50 = np.sum(intensity_sel == 50)
print("Количество точек со значением 50:", count_50)  # Должно быть 100

# Проверка двух граничных точек
count_40 = np.sum(intensity_sel == 40)
count_60 = np.sum(intensity_sel == 60)
print("Количество точек со значением 40:", count_40)  # Должно быть 1
print("Количество точек со значением 60:", count_60)  # Должно быть 1

'''Сохранение результатов'''
# Сохранение в ASCII: X Y Z intensity ID
result = np.column_stack([xyz_sel, intensity_sel, ids_sel])
np.savetxt("py_filtered.asc", result, fmt="%.6f", delimiter=" ")
print("Файл py_filtered.asc сохранен")

'''Визуализация пространственного распределения'''
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xyz_sel[:, 0], xyz_sel[:, 1], xyz_sel[:, 2],
           c=intensity_sel, cmap='viridis', s=10)
ax.set_xlabel('X (м)')
ax.set_ylabel('Y (м)')
ax.set_zlabel('Z (м)')
ax.set_title('Отфильтрованные точки: 40 <= intensity <= 60 (n=102)')
plt.colorbar(ax.collections[0], label='intensity')
plt.savefig("py_filtered_view.png", dpi=150)
plt.show()