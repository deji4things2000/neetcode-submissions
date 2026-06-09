class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        hm= {')': '(', '}':'{', ']':'['}
        n = len(s)

        for i in range(n):
            if s[i] in hm:
                if res != [] and hm[s[i]] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])

        return True if res == [] else False

        



