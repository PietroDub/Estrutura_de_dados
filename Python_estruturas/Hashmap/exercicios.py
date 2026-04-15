# 1 👉 Exercício:
# Crie um dicionário com nomes e idades e:

# adicione 3 pessoas
# imprima a idade de uma específica
# altere a idade de alguém

hashmap1 = { 
    "Pietro" : 18,
    "Anna" : 19,
    "Roberto" : 20
}

hashmap1["Mario"] = 10
hashmap1["Mario"] = 10
hashmap1["Mario"] = 10

print(hashmap1.get("Pietro"))

hashmap1["Anna"] = 20

# 2 Exercício:

nums = [1, 2, 3, 4, 5]

mapanums = {}

for n, i in range(len(nums)):
    mapanums[i] = nums[n]

if 3 in mapanums:
    print("3 existe!")


#correção
nums = [1, 2, 3, 4, 5]

mapanums = {}

for num in nums:
    mapanums[num] = True

if 3 in mapanums:
    print("3 existe!")


# 3 Exercício:

nums = [1, 1, 2, 3, 3, 3]

mapanumsrepeat = {}

for n in nums:
    if mapanums.get(n) is not None:
        mapanums[n] += 1 
    else:
        mapanums[n] = 1
    
print(mapanums)


#correção

nums = [1, 1, 2, 3, 3, 3]

contagem = {}

for num in nums:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

print(contagem)


# Exercicio 4

nums = [1, 2, 3, 1]

numsHash = {}

for n in nums:
    if n in numsHash:
        return True
    numsHash[n] = nums[n]

#correção

def containsDuplicate(nums):
    numsHash = {}

    for n in nums:
        if n in numsHash:
            return True
        numsHash[n] = True

    return False


# Exercicio 5

s = "leetcode"
shash = {}

for n in s:
    if n not in shash:
        return n
    
#correção

def firstUniqueChar(s):
    shash = {}

    for c in s:
        shash[c] = shash.get(c, 0) + 1

    for c in s:
        if shash[c] == 1:
            return c

    return None


# Exercicio 6

def ex6(palavras):
    palavras = ["maçã", "banana", "abacate", "uva"]

    hashword = {}
    for w in palavras:
        hashword[w] = w[0]

    hashword.sort()
    return hashword

#correção 

def ex6Correcao():
    palavras = ["maçã", "banana", "abacate", "uva"]

    hashword = {}

    for w in palavras:
        primeira_letra = w[0]

        if primeira_letra not in hashword:
            hashword[primeira_letra] = []

        hashword[primeira_letra].append(w)

    return hashword


# 🧠 Fase 3 — Padrões de entrevista
# 7. Two Sum (o clássico)

# 🎯 Padrão: complemento

# 👉 Exercício:

nums = [2, 7, 11, 15]
jafoi = {}
target = 9

for n in range(len(nums)):
    for i in range(len(nums + 1)):
        if nums[n] + nums[i] == target:
            return [n, i]
        jafoi[n] = True

# Correção

nums = [2, 7, 11, 15]
target = 9

mapa = {}

for i, num in enumerate(nums):
    complemento = target - num

    if complemento in mapa:
        print([mapa[complemento], i])
        break

    mapa[num] = i

# Retorne os índices dos dois números.

# 8. Anagrama

# 🎯 Padrão: contagem

# 👉 Exercício:

s = "anagram"
t = "nagaram"

# Retorne True se forem anagramas.
def isAnagram(s, t):
    maps = {}
    mapt = {}

    for l in s:
        if l in maps:
            maps[l] += 1
        else:
            maps[l] = 1

    for l in t:
        if l in mapt:
            mapt[l] += 1
        else:
            mapt[l] = 1

    return maps == mapt #true or false    

# 9. Interseção de arrays

# 🎯 Padrão: presença / lookup

# 👉 Exercício:

nums1 = [1,2,2,1]
nums2 = [2,2]

interseção = {}
# Retorne a interseção:

for n in nums1:
    for i in nums2:
        if nums1[n] == nums2[i]:
            if interseção[n]:
                return interseção[n]
            interseção[n] = True
        
# [2]

# resolução
def intersection(nums1, nums2):
    set1 = set(nums1)
    resultado = []

    for n in nums2:
        if n in set1:
            resultado.append(n)
            set1.remove(n)  # evita duplicado

    return resultado

# 🧠 Fase 4 — LeetCode básico real
# 10. Longest Substring Without Repeating Characters

# 🎯 Padrão: HashMap + Sliding Window

# 👉 Exercício:

# s = "abcabcbb"

# Retorne o tamanho da maior substring sem repetir caracteres.

# 👉 Saída:

# 3  # "abc"