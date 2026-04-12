# minha solução
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(List) - 1
        last = last + 1

        List[-1] = last

        return List

# solução alternativa

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        return self.plusOne(digits[:-1]) + [0]
        

# explicação:

# Vamos com [2,3,9] + 1 = [2,4,0] PASSO A PASSO
# 🎬 Execução COMPLETA:
# text
# CHAMADA 1: plusOne([2,3,9])
# digits[-1] = 9? SIM!
# return plusOne([2,3]) + [0]     ← Remove 9, coloca 0

# CHAMADA 2: plusOne([2,3])
# digits[-1] = 3? 3 != 9! NÃO!
# digits[-1] += 1 → [2,4]         ← AQUI ADICIONA O 1!
# return [2,4]

# FINAL: [2,4] + [0] = [2,4,0] ✅
# 🔑 Onde o "1" é adicionado?
# text
# 1. [2,3,9] → 9? RECURSÃO → [2,3] + [0]
# 2. [2,3]   → 3<9? SIM → [2,4] (3+1=4!)
# 3. [2,4] + [0] = [2,4,0]
# O +1 aparece quando encontra <9! A recursão "carrega" o 1 automaticamente.

# 🎨 TODOS os casos:
# text
# [1,2,3] +1
# 3<9 → [1,2,4] ✅ (simples)

# [9] +1  
# 9=9 → plusOne([]) + [0]
#      [1] + [0] = [1,0] ✅

# [4,3,2,9] +1
# 9=9 → plusOne([4,3,2]) + [0]
# 2<9 → [4,3,3] + [0] = [4,3,3,0] ✅

# [9,9,9] +1
# 9=9 → plusOne([9,9]) + [0]
# 9=9 → plusOne([9]) + [0]  
# 9=9 → plusOne([]) + [0]
#      [1] + [0] + [0] + [0] = [1,0,0,0] ✅


# terceira resolução invertendo

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1] #inverte o array
        one, i = 1, 0 # o número 1 e o indice

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    one = 1 #garante o valor
                    digits[i] = 0
                else:
                   digits[i] += 1
                   one = 0 
            else:
                #caso seja 999, adiciona o 1
                digits.append(1)
                one = 0
            i+=1
        return digits[::-1] #reverte