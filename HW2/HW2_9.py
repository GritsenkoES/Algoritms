# Задание №9
# https://drive.google.com/file/d/1BPeBidD9zmE6EBU1cwAXysRwJRxT-GTK/view?usp=sharing
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

print('Введите натуральные числа, для остановки ввода введите 0')
def sum_f(vvod, sum = 0, last_n_vvod = 0):
    if vvod == 0:
        return sum
    else:
        last_n_vvod = vvod % 10
        sum += last_n_vvod
        vvod = vvod // 10
        return sum_f(vvod, sum, last_n_vvod)

def max_s(sum_max = 0, vvod_max = 0):
    vvod = int(input('Введите число: '))
    if vvod == 0:
        return f'Введенное число {vvod_max}, сумма его чисел {sum_max}'
    else:
        if sum_f(vvod) > sum_max:
            sum_max = sum_f(vvod)
            vvod_max = vvod
    return max_s(sum_max, vvod_max)

res = max_s()
print(res)