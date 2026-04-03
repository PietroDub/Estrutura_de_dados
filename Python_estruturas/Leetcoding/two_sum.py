
# minha resolução número 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        direita = 1
        while direita < len(nums):
            if nums[i] + nums[direita] == target:
                resposta = [i, direita]
            i += 1
            direita += 1
        return resposta
    
# minha resolução número 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        direita = 1
        esquerda = 0
        if (i >= 1){
            esquerda = i - 1
        }

        while direita < len(nums):
            if nums[i] + nums[direita] == target:
               resposta = [i, direita]
               return resposta
            if nums[i] + nums[esquerda] == target:
                resposta = [i, esquerda]
                return resposta

# minha resolução número 3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        direita = 1
        esquerda = 0

        while direita < len(nums):
            if i >= 1:
                esquerda = i - 1
            
            match i:
                case i if nums[i] + nums[direita] == target and esquerda != None:
                    resposta = [i, direita]
                    return resposta

                case i if nums[i] + nums[esquerda] == target and esquerda != None:
                    resposta = [i, esquerda]
                    return resposta

                case i if nums[direita] + nums[esquerda] == target and esquerda != None: 
                    resposta = [esquerda, direita]
                    return resposta
            i += 1
            direita += 1

        return []
    
# resolução bruta mas entendivel

#i = loop EXTERNO (primeiro/fora)
#j = loop INTERNO (segundo/dentro) 

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1): # linha externa i 
        for j in range(i+1, len(nums)): # linha interna do i para frente
            if nums[i] + nums[j] == target:
                return [i, j]
    return []