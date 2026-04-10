
#testes

#The original array
arr = [11, 22, 33, 44, 55]
x= arr
print("Before reversal Array is :",arr)
 
arr.reverse() #reversing using reverse()
print("After reversing Array:",arr)

if(arr == x):
    print("VDD")
else:
    print("NOPE")

#resolução
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        a = x[:]  # ← MUDE SÓ ISSO!
        x.reverse()
        return x == a
    
# modo fácil
#palindrome string

def check_if_palindrome(s:str) ->bool :
    left = 0
    rigth = len(s) - 1

    while s[left] < s[rigth]:

        if s[left] != s[rigth]:
            return False
        
        left = left+1
        rigth = rigth - 1

    return True
