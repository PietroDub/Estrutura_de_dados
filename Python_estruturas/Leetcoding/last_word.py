# minha solução
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip() #trim
        string = s.split() # tira todos os espacos " ", "  "
        return len(string[-1])