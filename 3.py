#Задайте список из n чисел последовательности (1+1/n)^n
#Выведитте на экран саму последовательность и сумму элеементов этой последовательности
# (для проверки сумма для 4 элементов = 9,06 (примерно))

num = int(input('Введите число: '))
arr = []
result = 1

for i in range(1, num+1):
    result = (1 + 1/i)**i
    arr.append(result)
print(f'Сумма элементов последовательности {arr} = {sum(arr)}')
