# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.

#stroke = input('Введите строку в нижнем регистре: ')
stroke = 'qwerty'
def up(str):
    yield str.upper()

new_stroke = up(stroke)
for i in new_stroke:
    print(i)

