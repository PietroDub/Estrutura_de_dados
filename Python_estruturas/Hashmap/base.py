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

