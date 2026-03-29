nums = [1, 2, 4, 6]
target = [8]

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

# segunda versão

def twoSum(nums, target):
    numbertoIndex = {}

    for i in range(len(nums)):
        numbertoIndex[nums[i]] = i
    
    for i in range(len(nums)):
        numberneeded = target - nums[i]

        if numbertoIndex[numberneeded] is not None and numbertoIndex[numberneeded] != i:
            return [i, numbertoIndex[numberneeded]];

