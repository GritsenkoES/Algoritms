# Задание №3
# https://drive.google.com/file/d/1BPeBidD9zmE6EBU1cwAXysRwJRxT-GTK/view?usp=sharing
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, надо вывести 6843.


def revers(num, rev_num=0):
    if num == 0:
        return f'Ваше число в обратном порядке: {int(rev_num/10)}'
    else:
        rev_num += num % 10
        num = num // 10
        return revers(num, rev_num*10)

num = int(input('Введите число '))
print(revers(num))