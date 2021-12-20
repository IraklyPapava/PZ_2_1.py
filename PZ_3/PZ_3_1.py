# Даны три целых числа : A , B , C. Проверить истинность высказывания : 'Ровно два из чисел  A,B,C,
# положительное.'
a = input("Введите число a : ")
while type (a) != int:
    try:
        a = int(a)
    except ValueError:
        print ('Введено неверно')
        a = int(input("Введите число a : "))
b = input("Введите число b : ")
while type (b) != int:
    try:
        b = int(b)
    except ValueError:
        print ('Введено неверно')
        b = int(input("Введите число b : "))
c = input("Введите число c : ")
while type (c) != int:
    try:
        c = int(c)
    except ValueError:
        print ('Введено неверно')
        c = int(input("Введите число c : "))

if a > 0 and b > 0 and c < 0:
    print ('True')
elif a > 0 and c > 0 and b < 0:
    print ('True')
elif b > 0 and c > 0 and a < 0:
    print ('True')
else:
    print ('False')

