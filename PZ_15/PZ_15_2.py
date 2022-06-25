# в матрице найти сумму элементов второй половины матрицы
# (делить по горизонтали)
import random
M = 4   # размер 4х4
matrix = [[random.randint(0, 2) for y in range(M)] for x in range(M)]
print("Исходная матрица:")
print(*matrix, sep="\n")   # исходная матрица

new = []   # создаю пустой список
for i in range(len(matrix)):
    a = matrix[2:][i]   # берём срез (2 последние строки)
    new += a   # добавляю получение элементы в список
    print("Вторая половину матрицы:", *a)
    if i > 0:   # иначе выдаёт ошибку
        break

print("Сумма элементов во второй половине матрицы:", sum(new))