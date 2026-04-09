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

# comandos básicos
arr = []
arrce = [1, 2, 3, "arroz"]
arrnum = list(range(5))

#adicionando elementos
arr.append(2)
arr.append("oi")
arr.extend([3, 6, 9, 10, 34])
arr.insert(1, 50) #posição / valor

print(arr)

# Remover Elementos
arr.pop() #remove o último
arr.pop(0)
arr.remove(3)  #por valor
print(arr) 
del arr[0] #por indíce
print(arr)
# arr.clear() tira todos os elementos 
print(arr)


# Acessar e verificar
len(arr) #tamanho 
print(arr[2])
arr[-1]
print(2 in arr) # verifica se existe o valor
print(arr.index(9)) # retorna a posição do valor!


# Fatiamento (slicing)
print(arr[1:4]) #do um até antes do 4
print(arr[:3])
print(arr[2:])
print(arr[::-1]) #INVERTER

# Transformações!

# | Função | Propósito                  | JS                              | Python                       | Retorno                    |
# | ------ | -------------------------- | ------------------------------- | ---------------------------- | -------------------------- |
# | map    | Transforma TODOS elementos | arr.map(x => x*2)               | [x*2 for x in arr]           | Nova lista (mesmo tamanho) |
# | filter | Filtra por condição        | arr.filter(x => x > 2)          | [x for x in arr if x > 2]    | Lista menor                |
# | reduce | Reduce lista a 1 valor     | arr.reduce((acc, x) => acc + x) | reduce(lambda x,y: x+y, arr) | Único valor                |

# lambda arg1, arg2: resultado
lambda x: x*2           # 1 argumento
lambda x, y: x + y      # 2 argumentos (reduce)

# Map
[x*2 for x in arr]                  # JS: arr.map(x => x*2)
[x*2 for x in arr if x > 2]         # JS: arr.map().filter()

# Filter
list(filter(lambda x: x > 2, arr))  # JS: arr.filter(x => x > 2)

# reduce
from functools import reduce

reduce(lambda acc, x:acc * x, arr, 1)

# Sort
arr.sort()                          # JS: arr.sort((a,b)=>a-b)
arr.reverse()                       # JS: arr.reverse()