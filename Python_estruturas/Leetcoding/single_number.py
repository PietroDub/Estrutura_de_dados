class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        right = 1
        for n in range(len(nums) - 1):
            if nums[n] == nums[right]:
                nums[n] = 0
                nums[right] = 0
            
            right += 1
            
        nums.remove(0)

        return(nums)