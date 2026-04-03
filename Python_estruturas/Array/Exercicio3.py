# # PARTE 1: 5 Exercícios Map/Filter/Reduce (Nível Médio/Avançado)

# # 1. Números Positivos ao Quadrado (MAP + FILTER)
# # python
nums = [-2, 1, -5, 3, 0, 7, -1]
# # # Resultado: [1, 9, 49]
nums = list(filter(lambda x: x > 0, nums))
nums = [x * x for x in nums]
print(nums)

# # 2. Primeira Letra Maiúscula (MAP)
# # python
words = ["python", "é", "incrível", "para", "dados"]
# # Resultado: ['Python', 'É', 'Incrível', 'Para', 'Dados']
[x.capitalize() for x in words]
words = [x[:1].upper() for x in words]
print(words)

# # 3. Soma dos Pares (FILTER + REDUCE)
# # python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# # Resultado: 20 (2+4+6+8)
nums = list(filter(lambda x: x % 2 == 0, nums))
from functools import reduce
nums = reduce(lambda x, y : x + y, nums)
print(nums)

# 4. Clientes VIP (FILTER por dicionário)
# python
clientes = [
     {"nome": "Ana", "compras": 1500},
     {"nome": "Bruno", "compras": 800},
     {"nome": "Clara", "compras": 2200}
 ]
# Resultado: ['Ana', 'Clara']

clientesvip = list(filter(lambda x : x["compras"] >= 1500, clientes))
print(clientesvip)

# Se quiser só nomes:
[x["nome"] for x in clientes if x["compras"] >= 1500]  # ['Ana', 'Clara']


# 5. Média de Notas Acima da Média (FILTER + REDUCE)
# python
notas = [6, 8, 4, 9, 7, 3, 10]

notas = list(filter(lambda x: x >= 6, notas))
notastam = len(notas)
print(notastam)

notas = reduce(lambda x, y : (x + y), notas)
print(notas)
notas2 = notas / notastam

print(notas2)

# # Resultado: ~7.33 (média das notas >= 6)


# PARTE 2: 5 Exercícios Big O Notation (com explicação)
# 1. Busca Simples
# python
# def busca_simples(lista, alvo):
#     for i in range(len(lista)):  # ← Percorre TODA lista
#         if lista[i] == alvo:
#             return i
#     return -1
# Big O: O(n) - No pior caso, vê todos os n elementos

# 2. Dobrar Lista (MAP)
# python
# def dobrar_todos(nums):
#     return [x*2 for x in nums]  # ← 1 operação por elemento
# Big O: O(n) - Transforma n elementos

# 3. Força Bruta Two Sum
# python
# def two_sum_bruta(nums, target):
#     for i in range(len(nums)):           # n iterações
#         for j in range(i+1, len(nums)):  # n iterações
#             if nums[i] + nums[j] == target:
#                 return [i, j]
# Big O: O(n²) - n × n = n² comparações

# 4. Hash Map Two Sum (sua solução!)
# python
# def two_sum_map(nums, target):
#     mapa = {}
#     for i, n in enumerate(nums):     # n iterações
#         diff = target - n
#         if diff in mapa:             # O(1) busca
#             return [mapa[diff], i]
#         mapa[n] = i
# Big O: O(n) - 1 loop + buscas O(1)

# 5. Sort + Busca Linear
# python
# def sort_busca(lista, alvo):
#     lista.sort()              # O(n log n)
#     for i in range(len(lista)):  # O(n)
#         if lista[i] == alvo:
#             return i
# Big O: O(n log n) - Sort domina (maior termo)


    