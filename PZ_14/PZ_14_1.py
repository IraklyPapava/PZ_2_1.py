# Из исходного текстового файла выбрать все цены и,
# посчитать количество цифр в тексте
import re
with open('tex.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    # НАХОЖДЕНИЕ ЦЕН В ТЕКСТЕ
    k1 = re.compile(r"[0-9]+ руб. [0-9]+ коп.", re.S)   # буквы не прилипли к словам
    f3 = re.findall(k1, text)

    k2 = re.compile(r"[0-9]+ копеек", re.S)   # 10 копеек
    f4 = re.findall(k2, text)

    k3 = re.compile(r"[0-9]+ руб. [0-9]+коп.", re.S)   # прилипло к копейке
    f5 = re.findall(k3, text)

    k4 = re.compile(r"[0-9]+руб. [0-9]+ коп.", re.S)   # прилипло к рублю
    f6 = re.findall(k4, text)

    k5 = re.compile(r"[0-9]+руб. [0-9]+коп.", re.S)  # прилипло к рублю и к копейке
    f7 = re.findall(k5, text)

    al = f3 + f4 + f5 + f6 + f7
    print(f"Найденные цены в тексте:\n", al)

    # НАХОЖДЕНИЕ КОЛИЧЕСТВА ЦИФР В ТЕКСТЕ
    num = re.compile(r"([0-9]+)", re.S)   # определяет число
    f1 = re.findall(num, text)   # применяем выражение к тексту
    f2 = len(str("".join(f1)))
    print(f"Всего найдено {f2} количеств(о) цифр")

