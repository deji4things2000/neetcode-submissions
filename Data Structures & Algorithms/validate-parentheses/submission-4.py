class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')': '(', '}': '{', ']': '['}
        res = []

        for i in range(len(s)):
            if s[i] in hm:
                if res != [] and res[-1] == hm[s[i]]:
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])
        return True if res == [] else False

