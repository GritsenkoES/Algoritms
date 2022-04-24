# Задание №4
# https://drive.google.com/file/d/1BPeBidD9zmE6EBU1cwAXysRwJRxT-GTK/view?usp=sharing
#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#Количество элементов (n) вводится с клавиатуры.'''

def progress(n, summa=0, num=1):
    if n == 0:
        return f'сумма элементов равна: {summa}'
    else:
        summa += num
        return progress(n-1, summa, num/-2)
n = int(input('Введите количество элементов в ряду '))
print(progress(n))
