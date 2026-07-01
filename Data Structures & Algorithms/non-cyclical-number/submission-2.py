class Solution:
    def isHappy(self, n: int) -> bool:
        nums_set = set()
        while(True):
            res = 0
            while(n > 0):
                digit = n % 10
                res += pow(digit, 2)
                n = n // 10
            if res == 1:
                return True  
            if res in nums_set:     
                return False
            nums_set.add(res)
            n = res
            
