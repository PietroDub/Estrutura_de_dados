<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Guia de Arrays em Python para Estágios e LeetCode

Arrays em Python são implementados de três formas principais: **listas** (padrão), **array.array** (tipado) e **NumPy ndarray** (científico). Para estágios brasileiros como iFood, priorize listas para LeetCode.

## 1. Listas (Padrão - 80% do foco)

Dinâmicas e flexíveis como JavaScript arrays.

**Características:**

- Heterogêneas: `arr = [1, 2, 'texto', True]`
- Tamanho automático
- Sintaxe familiar: `arr.append(3)`, `arr[0]`, `len(arr)`

## 2. array.array (Módulo nativo)

Tipado e eficiente em memória.

**Importação e uso:**

```python
import array
arr = array.array('i', [1, 2, 3])  # 'i' = int 32-bit
arr.append(4)
print(arr)  # array('i', [1, 2, 3, 4])
```

**Tipos suportados:**


| Código | Tipo | Descrição |
| :-- | :-- | :-- |
| 'b' | signed char | Inteiro 8-bit |
| 'i' | int | Inteiro 32-bit |
| 'f' | float | Float 32-bit |
| 'd' | double | Float 64-bit |

## 3. NumPy ndarray (Biblioteca externa)

Otimização para dados científicos.

**Instalação e uso básico:**

```python
import numpy as np
arr = np.array([1, 2, 3])
arr2 = np.array([[1,2], [3,4]])  # Matriz 2x2

# Operações vetorizadas (muito rápidas)
print(arr * 2)     # [2 4 6]
print(np.sum(arr)) # 6
```


## Comparação Rápida

| Característica | Listas | array.array | NumPy |
| :-- | :-- | :-- | :-- |
| **Velocidade** | Boa | Muito boa | Excelente |
| **Memória** | Média | Baixa | Baixa |
| **Tipagem** | Dinâmica | Estática | Estática |
| **Operações matemáticas** | Lentas | Básicas | Rápidas |
| **LeetCode** | ✅ Ideal | ⚠️ Opcional | ❌ Não use |
| **Dados/Power BI** | ❌ | ⚠️ | ✅ Ideal |

## Plano de Estudo (Prioridade para Estágios)

### Semana 1-2: Listas (Domínio Total)

```
Dia 1: Sintaxe básica, append/pop/slice
Dia 2: List comprehension, enumerate
Dia 3: Two Sum + 5 exercícios LeetCode Easy
Dia 4: Busca binária em arrays ordenados
Dia 5: Two pointers (esquerda/direita)
Dia 6: Revisão + Medium array problems
Dia 7: Mock interview (explique código)
```


### Semana 3: array.array (Entendimento)

- Entenda tipagem `'i'`, `'f'`, `'d'`
- Compare performance vs listas
- 2-3 exercícios simples


### Semana 4+: NumPy (Bônus para Dados)

- Operações vetorizadas
- Integração com Power BI/Excel
- Projetos de dashboard


## Exercícios LeetCode Recomendados (Arrays)

```
✅ 1. Two Sum (O(n) hash map)
✅ 26. Remove Duplicates from Sorted Array
✅ 88. Merge Sorted Array
✅ 121. Best Time to Buy and Sell Stock
✅ 283. Move Zeroes
```

**Foco principal**: **Listas + LeetCode**. NumPy impressiona em entrevistas de dados, mas listas ganham processos técnicos de back-end/full-stack no Brasil.

***

*Copie este .md e salve como `arrays-python-estagios.md`*

