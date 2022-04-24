# Задание №8
# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# https://drive.google.com/file/d/1_xZuKf9YzvrNpc78bmIDbTy-_6sk_JWf/view

def vis_god(god):
    if god % 4  == 0:
        if god % 100  != 0:
            return ('Введенный год високосный')
        else:
            if god % 400 == 0:
                return ('Введенный год високосный')
            return ('Введенный год не високосный')
        return ('Введенный год не високосный')


god = int(input('Введите год (например 1980): '))
print(vis_god(god))

