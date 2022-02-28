#В последовательности на n целых чисел умножить все элементы на первый
#элемент.
#from random import randint
#dlina = int(input('Введите длину последовательности: '))
#n = [randint(-10, 10) for i in range(dlina)]

n = [3, 2, 3, 5, 6]
print(n)
nn = [i*n[0] for i in n]
print(nn)
