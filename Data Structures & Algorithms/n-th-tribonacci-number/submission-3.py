class Solution:
    def tribonacci(self, n: int) -> int:
        # if n <= 2:
        #     return 1 if n != 0 else 0
        # return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        t = [0, 1, 1]
        if n<3:
            return t[n]
        for i in range(3, n+1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        
        return t[2]