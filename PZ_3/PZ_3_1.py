# Даны три целых числа : A , B , C. Проверить истинность высказывания : 'Ровно два из чисел  A,B,C,0
# положительное.'
a = int(input("Введите число a : "))
b = int(input("Введите число b : "))
c = int(input("Введите число c : "))

x = \
    (a and b and not c) \
    or (not a and b and c) \
    or (a and not b and c)

print("Ровно два из чисел A, B, C являются положительными: ", x)5