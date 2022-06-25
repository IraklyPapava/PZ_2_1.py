# в матрице найти суммы элементов каждой строки и поместитьт их в новый массив.
# 3-й столбец матрицы заменить на сумму.
import random
M = 4   # размер 4х4
matrix = [[random.randint(0, 2) for y in range(M)] for x in range(M)]
print(*matrix, sep="\n")   # исходная матрица

sumArr = [*map(sum, matrix)]   # сумма в строках
print("Сумма строк в исходной матрице:", sumArr)

for i in range(len(matrix)):
    matrix[i][-2] = sumArr[i]   # заменяем 3-й столбец на значения суммы
print(*matrix, sep="\n")
