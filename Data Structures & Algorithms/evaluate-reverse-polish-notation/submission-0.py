class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sign = '+-*/'
        for a in tokens:
            if a not in sign:
                stack.append(int(a))
            else:
                y = stack.pop()
                x = stack.pop()
                if a == '+':
                    res = x + y 
                elif a == '-':
                    res = x - y
                elif a == '*':
                    res = x * y
                elif a == '/':
                    res = x / y
                stack.append(int(res))
        return stack[0]   