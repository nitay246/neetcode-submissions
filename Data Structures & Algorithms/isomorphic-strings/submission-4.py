class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        n = len(s)
        for i in range(n):
            if s[i] not in dic and t[i] not in dic.values():
                dic[s[i]] = t[i]
            else:
                if s[i] not in dic or dic[s[i]] != t[i]:
                    return False
        return True


        