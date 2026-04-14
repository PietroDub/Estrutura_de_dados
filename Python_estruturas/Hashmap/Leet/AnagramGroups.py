from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        result = []

        for s in strs:
            reajustado = tuple(sorted(s)) #listas n podem ser valoresmas tuplas s
            anagram[reajustado].append(s)               

        #adicione o valor ao resultado
        for v in anagram.values():
            result.append(value) 

        return result