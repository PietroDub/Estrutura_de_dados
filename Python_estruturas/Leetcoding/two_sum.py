
# minha resolução
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
    
# resolução ideal