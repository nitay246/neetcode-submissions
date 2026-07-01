from collections import defaultdict
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = sorted(s)
#         t = sorted(t)
#         if s == t:
#             return True
#         else:
#             return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)
        for a in s:
            char_count[a] += 1
        for a in t:
            char_count[a] -= 1
        for key in char_count:
            if char_count[key] != 0:
                return False
        return True