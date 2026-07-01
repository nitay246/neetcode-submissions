class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = s.replace(" ", "")
        w = "".join(a.lower() for a in s if a.isalnum())
        if w == w[::-1]:
            return True
        else:
            return False