class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        #we will save tuples (pairs) in the stack
        stack = [] 

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #pop the head tuple
                stackT, stackInd = stack.pop()
                #calculate the diff between the current position to the greater before 
                res[stackInd] = i - stackInd
            #append to the stack the tuple (and we create monotonic decreasing stack)    
            stack.append([t,i])
        return res
