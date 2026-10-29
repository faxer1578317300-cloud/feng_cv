import numpy as np

# Чтение результата, экспортированного из CloudCompare
cc = np.loadtxt("cc_filtered.asc")
cc_ids = set(cc[:, 4].astype(int))

# Чтение результата, полученного в Python
py = np.loadtxt("py_filtered.asc")
py_ids = set(py[:, 4].astype(int))

print("Количество ID в CloudCompare:", len(cc_ids))
print("Количество ID в Python:", len(py_ids))
print("Наборы ID полностью совпадают:", cc_ids == py_ids)

# Если есть различия, вывести их
if cc_ids != py_ids:
    print("Только в CC:", cc_ids - py_ids)
    print("Только в Python:", py_ids - cc_ids)




