#Реализуйте алгоритм перемешивания списка, без использования встроеных методов 
# (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

import random

#def shuf(List):
#    newList=[]
#    for i in List:
#        i=random.randrange(len(List))
 #       newList.append(i)
  #  return newList

n = int(input('Введите размерность массива: '))
myList = []
for i in range(n):
    myList.append(random.randint(0,10))

print(myList)

newList = []
for i in range(len(myList)-1):
    j = random.randint(0, len(myList)-1)
    myList[i], myList [j] = myList[j], myList[i]

print(myList)