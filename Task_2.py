# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

n = int(input('Enter mount of patches: '))
if n < 3: print('There should be 3+ patches')
else:
    array = []
    for i in range(n):
        array.append(int(input('Enter amount of berries: ')))

    first_num = array[0] + array[1] + array[n-1]
    last_num = array[0] + array[n-2] + array[n-1]
    max_num = 0
    if first_num > last_num:
        max_num = first_num
    else: max_num = last_num    
    for i in range(1, n-1):
        if max_num < array[i] + array[i-1] + array[i+1]:
            max_num = array[i] + array[i-1] + array[i+1]
    print(max_num)