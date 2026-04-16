#o hashmap é uma estrutra baseada em um array/dicionário com listas
# geralmente com valor predefinido
# ele é um array onde em cada posição tem uma lista
# seja ela um list do python ou uma lista encadeada
# ao adicionar um elemento ele vai ser hash(elemento)
# cada elemento terá chave:valor
# e depois % vai ser feito seu nódulo pelo tamanho
# do array self.size guardando ele na lista da posição
# resultante, ao procurar um item, o msm  será feito
# mas ao chegar na lista indicada pelo hash
# ela terá q ter percorrida por O(n) oque pode deixar
# a estrutura um pouco mais lenta

# base 
# ✅ Modelo mental correto (simplificado e poderoso)

# Pensa assim:

mapa[numero] = indice

# Exemplo:

nums = [2, 7, 11, 15]

mapa = {
    2: 0,
    7: 1,
    11: 2,
    15: 3
}

# 👉 Agora você consegue:

# if 7 in mapa:  # O(1)


mapa2 = {}

# inicializando a key

mapa2["Canada"] = []
cidades = ["Vancouver", "Toronto"]
mapa2["Canada"] += cidades

# com dictdefault (vem com chaves predefinidas)

from collections import defaultdict
mapa2_cidades = defaultdict(list)

cidades = ["Vancouver", "Toronto"]
mapa2_cidades["Canada"] += cidades

# 🧠 Diferença simples (guarda isso)
# 🔹 dict (dicionário)
# mapa = {"a": 1}

# 👉 tem:

# chave
# valor
# 🔹 set
# conjunto = {1, 2, 3}

# 👉 tem:

# só valores (únicos)
# NÃO tem chave → valor
# 💡 Então por que usei set?

# Porque o problema era:

# “existe algum elemento em comum?”

# 👉 Você NÃO precisa:

# contar ❌
# guardar índice ❌
# guardar valor extra ❌

# 👉 Só precisa saber:

# “isso existe?”

# 🔥 Comparação direta
# ❌ Usando dict (funciona, mas exagerado)
# hashab = {}

# for x in a:
#     hashab[x] = True

# for y in b:
#     if y in hashab:
#         return True
# ✅ Usando set (mais correto)
# set_a = set(a)

# for y in b:
#     if y in set_a:
#         return True