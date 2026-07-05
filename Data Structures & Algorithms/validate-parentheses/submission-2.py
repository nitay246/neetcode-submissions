class Solution:
    def isValid(self, s: str) -> bool:
        # #simple but without stack- n^2
        # while "()" in s or "{}" in s or "[]" in s:
        #     s=s.replace("()", "")
        #     s=s.replace("[]", "")
        #     s=s.replace("{}", "")
        # if s: 
        #     return False
        # else:
        #     return True 
        
        #stack solution with array as stack
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            #check the keys in the dict
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []
