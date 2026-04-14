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

mapa = {}

# inicializando a key

mapa["Canada"] = []
cidades = ["Vancouver", "Toronto"]
mapa["Canada"] += cidades

// com dictdefault (vem com chaves predefinidas)

from collections import defaultdict
mapa_cidades = defaultdict(list)

cidades = ["Vancouver", "Toronto"]
mapa_cidades["Canada"] += cidades

