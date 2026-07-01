class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luck = -1
        dic = {}

        for a in arr:
            if a in dic:
                dic[a] += 1
            else: 
                dic[a] = 1


        for b in dic:
            if b == dic[b]:
                luck = max(b, luck)

        return luck