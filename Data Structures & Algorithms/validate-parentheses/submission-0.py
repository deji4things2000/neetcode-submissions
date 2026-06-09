class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c2o = { ")" : "(", "]" : "[", "}" : "{" }

        for i in range(len(s)):
            c = s[i]
            if c in c2o:
                if stack != [] and stack[-1] == c2o[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack == []:
            return True
        else:
            return False

