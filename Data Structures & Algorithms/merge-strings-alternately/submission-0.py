class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []
        word1 = list(word1)
        word2 = list(word2)

        while word1 and word2:
                res.append(word1[0])
                word1.pop(0)
                res.append(word2[0])
                word2.pop(0) 
        
        res += word1 
        res += word2   
        
        return "".join(res)