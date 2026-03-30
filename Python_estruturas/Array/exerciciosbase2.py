# 10 Exercícios Práticos: Map, Filter, Reduce e Sort
# Copie, cole no seu editor e resolva! Soluções no final. Use list comprehension sempre que possível.

# Exercícios Nível Fácil
# 1. Dobrar Números (MAP)
# python
nums = [1, 2, 3, 4, 5]
nums = [x * 2 for x in nums]

# # Resultado esperado: [2, 4, 6, 8, 10]
# 2. Pares Apenas (FILTER)
# python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# # Resultado esperado: [2, 4, 6, 8]
from functools import reduce
nums = list(filter(lambda x: x % 2 == 0, nums))

# 3. Soma Total (REDUCE)
# python
from functools import reduce
nums = [1, 2, 3, 4, 5]
# # Resultado esperado: 15
nums = reduce(lambda x: x + (x+1), nums) #precisa passar 2 var x, y
print(nums)

# 4. Ordenar Crescente (SORT)
# python
nums = [5, 2, 8, 1, 9]
# # Resultado esperado: [1, 2, 5, 8, 9]
nums = nums.sort()


# Exercícios Nível Médio
# 5. Dobrar Apenas Pares (MAP + FILTER)
# python
nums = [1, 2, 3, 4, 5, 6]
# # Resultado esperado: [4, 8, 12]
nums = list(filter(lambda n: n % 2 == 0, nums))
nums = [x * 2 for x in nums]

# 6. Maior Número (REDUCE)
# python
nums = [3, 7, 2, 9, 1]
# # Resultado esperado: 9
nums = reduce(lambda x, y: x if x > y else y, nums)

# 7. Strings com 3+ Letras (FILTER)
# python
words = ["eu", "gosto", "de", "programar", "python"]
# # Resultado esperado: ['gosto', 'programar', 'python']
words = list(filter(lambda x: len(x) > 3, words))


# 8. Produto Total (REDUCE)
# python
nums = [2, 3, 4]
# # Resultado esperado: 24
nums = reduce(lambda x, y: x + y, nums)

# Exercícios Nível Avançado
# 9. Nome Maiúsculo + Idade Par (MAP + FILTER)
# python
pessoas = [
    {"nome": "ana", "idade": 25},
    {"nome": "joão", "idade": 30},
    {"nome": "maria", "idade": 28}
]
# # Resultado esperado: ['JOÃO', 'MARIA']


# 10. Média dos Números Pares (FILTER + REDUCE)
# python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# # Resultado esperado: 5.0

pares = list(filter(lambda x: x % 2 == 0, nums))
pares = reduce(lambda x, y: x + y, nums)
pares = reduce(lambda x: x / len(pares), nums)

#reduce(lambda x, y: x + y, pares, 0) / len(pares)
