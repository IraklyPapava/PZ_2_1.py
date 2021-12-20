#Даны три целых числа , одно из которых отлично от двух других , равных между собой.
#Определить порядковый номер отличающегося числа.
a = input('Введите первое число(a): ')
b = input('Введите второе число(b): ')
c = input('Введите третье число(c): ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Нужно ввести целое число!')
        a = input('a = ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Нужно ввести целое число!')
        b = input('b = ')

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('Нужно ввести целое число!')
        c = input('c = ')

if a == b == c:
    print('Все числа одинаковые')
elif a == b:
    print('Третье число отличается от других')
elif a == c:
    print('Второе число отличается от других')
elif c == b:
    print('Первое число отличается от других')
else:
    print('Вае числа разные')