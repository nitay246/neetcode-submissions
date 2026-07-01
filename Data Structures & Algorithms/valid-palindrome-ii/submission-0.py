class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = "".join(a.lower() for a in s if a.isalnum())
        if w == w[::-1]:
            return True
        else:
            return False
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        else:
            for i in range(len(s)):
                a = s.replace(s[i], "")
                if self.isPalindrome(a):
                    return True
                else:
                    continue
        return False