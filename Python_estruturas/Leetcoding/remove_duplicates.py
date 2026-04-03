# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

nums = [1,1,2]

def removeDuplicates(self, nums: List[int]) -> int:
    i = 0

    while (i < len(nums)):
        if nums[i] == esquerda or nums[i] == direita:
            nums.pop(i)
        

# melhora da minha solução:
def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    direita = i + 1

    while direita < len(nums):
        if  nums[i] == nums[direita]:
            nums.pop(i)
            continue
        
        i+= 1
        direita+= 1
        
    return(len(nums))