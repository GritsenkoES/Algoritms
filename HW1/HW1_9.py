# Задание №9
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1_xZuKf9YzvrNpc78bmIDbTy-_6sk_JWf/view

def avg_test(a,b,c):
    if a > b:
        if b > c:
            return (f'среднее число = {b}')
        else:
            if a > c:
                return (f'среднее число = {c}')
            else:
                return (f'среднее число = {a}')
    else:
        if a > c:
            return (f'среднее число = {a}')
        else:
            if b > c:
                return (f'среднее число = {c}')
            else:
                return (f'среднее число = {b}')


print('Введите 3 числа')
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))

print(avg_test(a,b,c))
