class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for i in range(len(s)):
            if s[i] in hm:
                if stack != [] and stack[-1] == hm[s[i]]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(s[i])
        return True if stack == [] else False

        