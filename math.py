print('Приветствую вас')
q1 = int(input('Введите число первое число: '))
q2 = int(input('Введите число второе число: '))

v = int(input("Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n"))

if v == 1:
    r = q1 + q2
    p = 'сложения'
    t = p
if v == 2:
    r = q1 - q2
    l = 'вычитания'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'деления'
    t = m
if v == 4:
    r = q1 * q2
    n = 'умножения'
    t = n
print('Результат ', t, ' = ', r)
