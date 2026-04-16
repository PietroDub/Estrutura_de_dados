# 1. Contar palavras
# 🎯 Padrão: contagem (HashMap)
# 👉 Dado:

frase = "maçã banana maçã uva banana maçã"

# 👉 Retorne:
# {"maçã": 3, "banana": 2, "uva": 1}

frases = frase.split()
print(frases)
frasehash = {}
i = 1

for w in frases:
    if w in frasehash:
        frasehash[w] += 1
    else:
        frasehash[w] = 1

print(frasehash)


# 2. Encontrar o número mais frequente

nums = [1,1,2,3,3,3,2]
hashnums = {}
for n in nums:
    if n in hashnums:
        hashnums[n] += 1
    else:
        hashnums[n] = 1

# retornar o maior
print(max(hashnums, key=hashnums.get))

# 3. Tirar duplicatas

nums = [1,2,2,3,1,4]
numsolo = {}

for n in nums:
    if n not in numsolo:
        numsolo[n] = True
    
print(numsolo.keys())
print(list(numsolo.keys()))


# 🧠 Fase 2 — Começando padrão real
# 4. Primeiro número que se repete

# 🎯 Padrão: HashSet

nums = [2,5,1,2,3,5,1]
# 👉 Retorne:
# 2

numset = {}

def firstrepeated():
    for n in nums:
        if n in numset:
            numset[n] = 1
        else:
           return n

        if numset[n] == 2:
            return n
    

# solução
def firstrepeated(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return n
        seen.add(n)

    return None


# 5. Verificar se duas listas têm algum elemento em comum

# 🎯 Padrão: HashSet

a = [1,2,3]
b = [4,5,3]

hashab = {}
# 👉 Retorne: True

for l in a:
    hashab[l] = 1

for c in b:
    if c not in hashab:
        hashab[c] = 1
    else:
        hashab[c] += 1

# soluções

def tem_comum(a, b):
    set_a = set(a)

    for x in b:
        if x in set_a:
            return True

    return False


def tem_comum(a, b):
    return bool(set(a) & set(b))



# 6. Agrupar anagramas

# 🎯 Padrão: HashMap + chave transformada

palavras = ["eat","tea","tan","ate","nat","bat"]

# 👉 Retorne:

[["eat","tea","ate"],["tan","nat"],["bat"]]

# 🧠 Treina:

# chave = palavra ordenada

hashword = {}
