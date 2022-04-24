# Задание №8
# https://drive.google.com/file/d/1BPeBidD9zmE6EBU1cwAXysRwJRxT-GTK/view?usp=sharing
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.'''


def number(num, figure, count_in_num=0):
    if num == 0:
        return count_in_num
    else:
        cur_n = num % 10
        if figure == cur_n:
            count_in_num += 1
        num = num//10
        return number(num, figure, count_in_num)


def count_num(n, figure, count=0):
    if n == 0:
        return f'количество повторов искомого числа равно: {count}'
    else:
        num = int(input('Введите элемент последовательности (число) '))
        count += number(num, figure)
        return count_num(n-1, figure, count)


n = int(input('Введите количество чисел в последовательности '))
figure = int(input('Введите искомую цифру '))

print(count_num(n, figure))