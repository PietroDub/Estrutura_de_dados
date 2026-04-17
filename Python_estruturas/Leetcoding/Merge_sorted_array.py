# minha solução:

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()

        for n in nums1:
            if n == 0:
                nums1.remove(0)

        print(nums1)

# solução two pointers 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ponteiroNums1 = m - 1
        ponteiroNums2 = n - 1
        indice_final = m + n - 1 # [tamanho do array - 1]

        while ponteiroNums2 >= 0:
            if ponteiroNums1 >= 0 and nums1[ponteiroNums1] > nums2[ponteiroNums2]:
                nums1[indice_final] = nums1[ponteiroNums1]
                ponteiroNums1 -= 1
            else:
                nums1[indice_final] = nums2[ponteiroNums2]
                ponteiroNums2 -= 1
            
            indice_final -= 1

# checa os números dos arrays e adiciona cronoloficamente o maior em cada posição de nums1