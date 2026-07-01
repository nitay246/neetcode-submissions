class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = 0
        dic = {}
        for a in s:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        for i in range(len(s)):
            if dic[s[i]] < 2:
                return i
        return -1
