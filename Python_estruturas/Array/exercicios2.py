# Mesmo nível dos anteriores! Copie e resolva antes de ver soluções.

# Exercícios Nível Fácil
# 1. Quadrado dos Números (MAP)
# python
nums = [1, 2, 3, 4, 5]
# # Resultado esperado: [1, 4, 9, 16, 25]
nums = [x * x for x in nums]
print(nums)

# 2. Múltiplos de 3 (FILTER)
# python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Resultado esperado: [3, 6, 9]
nums = list(filter(lambda x: x % 3 == 0, nums))
print(nums)

# 3. Produto Total (REDUCE)
# python
from functools import reduce
nums = [2, 3, 4]
nums = reduce(lambda x, y: x * y, nums)
print(nums)
# # Resultado esperado: 24

# 4. Ordenar Decrescente (SORT)
# python
nums = [3, 8, 1, 9, 4]
# # Resultado esperado: [9, 8, 4, 3, 1]
nums.sort()
print(nums)
nums.reverse()
print(nums)


# Exercícios Nível Médio
# 5. Triplicar Apenas Ímpares (MAP + FILTER)
# python
nums = [1, 2, 3, 4, 5, 6]
nums = list(filter(lambda x: x % 2 != 0, nums))
nums = [x * 3 for x in nums]
print(nums)
# # Resultado esperado: [3, 9, 15]


# 6. Menor Número (REDUCE)
# python
nums = [7, 2, 9, 1, 5]
# # Resultado esperado: 1
nums = reduce(lambda x, y:x if x < y else y, nums)
print(nums)

# 7. Palavras Começando com 'P' (FILTER)
# python
words = ["python", "java", "php", "c++", "pascal"]
words = list(filter(lambda x:x[:1] == "p", nums))
print(words)
# # Resultado esperado: ['python', 'php', 'pascal']

# 8. Soma dos Quadrados (MAP + REDUCE)
# python
nums = [1, 2, 3]
# # Resultado esperado: 14 (1² + 2² + 3² = 1 + 4 + 9)
nums = [x * x for x in nums]
nums = reduce(lambda x, y: x + y, nums)
print(nums)

# Exercícios Nível Avançado
# 9. Produtos Acima de R$100 (MAP + FILTER)
# python
produtos = [
 {"nome": "notebook", "preco": 3500},
 {"nome": "mouse", "preco": 50},
 {"nome": "teclado", "preco": 150}
]
# # Resultado esperado: ['NOTEBOOK', 'TECLADO']


# 10. Média dos Múltiplos de 5 (FILTER + REDUCE)
# python
# nums = [2, 5, 8, 10, 15, 20, 25]
# # Resultado esperado: 15.0