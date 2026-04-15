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