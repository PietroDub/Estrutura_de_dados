#valores recebidos
nums = [3,2,2,3]
val = 3

# primeira tentativa!
def removeElement(nums: list[int], val: int) -> int:
    for x in nums:
        if(x == val):
            valor = val
            nums.pop(x)
    return valor

# segunda 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for n in nums:
            for j in nums:
                if j == val:
                    nums.remove(j)

        return(len(nums))    
    

# correção ! O(n)
def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)  # Remove por índice
            continue     # NÃO incrementa i
        i += 1
    return len(nums)

# Melhora!

def removeElement(self, nums: List[int], val: int) -> int:
    left = 0  # Ponteiro "bom" (não-val)
        
    for right in range(len(nums)):  # right percorre tudo
        if nums[right] != val:      # Achou elemento bom?
            nums[left] = nums[right]  # Mover pro início
            left += 1               # Avança "bom"
        
    return left  # Tamanho da nova lista "boa"