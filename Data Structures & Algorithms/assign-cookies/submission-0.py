class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r, l = 0, 0

        while r<len(g) and l<len(s):
            if g[r] <= s[l]:
                r+=1
            l+=1
        return r
