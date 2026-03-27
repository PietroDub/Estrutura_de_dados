

from array import *

valores = array('i', [1, 2, 4, 6, 9])
#letras = array('u', ['a', 'n', 'd'])

newArr = array(valores.typecode, (a*a for a in valores))


for i in range(len(valores)):
    print(valores[i])

for e in valores:
    print(e)

for e in newArr:
    print(e)


I = 0

while i<len(newArr):
    print(newArr[i])
    i+=1