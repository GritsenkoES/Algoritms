# Задание №5
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
#  и сколько между ними находится букв.
# https://drive.google.com/file/d/1_xZuKf9YzvrNpc78bmIDbTy-_6sk_JWf/view

'''https://drive.google.com/file/d/1JzomxfRioOVOYMEvMiVzkb4TZ0zAow_J/view?usp=sharing'''

letter_1 = input('Введите строчную букву английского алфавита ')
letter_2 = input('Введите еще одну строчную букву английского алфавита ')

between = ord(letter_2) - ord(letter_1)-1

print(f'первая введенная буква стоит на {ord(letter_1)-96} месте в алфавите')
print(f'вторая введенная буква стоит на {ord(letter_2)-96} месте в алфавите')
print(f'Между введенными буквами находится {between} букв')