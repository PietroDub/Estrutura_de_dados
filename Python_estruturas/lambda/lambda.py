# Lambda em Python: Sintaxe Simples + Quando Usar
# Lambda = função de 1 linha. Perfeita para map, filter, reduce quando não vale criar def.

# Sintaxe (Fórmula Mágica)
# text
# lambda parâmetros: resultado
# Args	Exemplo	O que faz
# 0	lambda: "oi"	Sem parâmetro
# 1	lambda x: x*2	Um número → dobra
# 2+	lambda x,y: x+y	Soma dois números
# Múltiplos	lambda a,b,c: (a+b)/c	Média de 3
# Teste Rápido
# python

# Salve isso e rode!
dobrar = lambda x: x * 2
print(dobrar(5))  # 10

soma = lambda a, b: a + b
print(soma(3, 4))  # 7