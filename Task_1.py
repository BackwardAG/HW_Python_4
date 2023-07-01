# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

amount1 = int(input('Enter amount of elements on array1: '))
amount2 = int(input('Enter amount of elements on array2: '))
array1 = []
array2 = []
for i in range(amount1):
    array1.append(int(input('Enter an element of array1: ')))
for j in range(amount2):
    array2.append(int(input('Enter an element of array2: ')))
array3 = []
for i in array1:
    if i in array2 and i not in array3:
            array3.append(i)
array3.sort()
print(array3)