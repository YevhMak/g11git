import random
list1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
list2 = sampling = random.choices(list1, k=5)
list3 = sampling = random.choices(list2, k=1)
res1 = "Случайные пять чисел:" + str(list2)
res2 = "Случайное число:" + str(list3)
print(list1)
print(res1)
print(res2)
Num1 = int(input("Введите число: "))
if Num1 in list2:
    y = list2.index(Num1) + 1
    res3 = "Номер в списке:" + str(y)
print(res3)
