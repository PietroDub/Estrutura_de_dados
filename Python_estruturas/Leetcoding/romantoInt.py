# solução única
class Solution:
    def romanToInt(self, s: str) -> int:
    # Mapa valor das letras
        valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
    
        for i in range(len(s)):
            # Se atual < próximo → SUBTRAI
            if i < len(s)-1 and valores[s[i]] < valores[s[i+1]]:
                total -= valores[s[i]]
            else:
                total += valores[s[i]]
        return total