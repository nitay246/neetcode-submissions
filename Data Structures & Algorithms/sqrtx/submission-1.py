class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
           s = l + ((r - l) // 2)
           if s * s >  x:
               r = s -1
           elif s * s < x:
               l = s + 1
           elif s * s == x: 
               return s
        return r