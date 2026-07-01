class Solution:
    def maxDifference(self, s: str) -> int:
        dic = {}
        maxi, mini= 0, 100

        for a in s:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1

        
        for b in dic:
            if (dic[b] % 2) != 0:
                maxi = max(maxi, dic[b])
            else:
                mini = min(mini, dic[b])
        
        return maxi - mini