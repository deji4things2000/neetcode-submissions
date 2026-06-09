class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        l,r=0, 1
        pft=0
        res=0
        while r<len(p):
            if p[l] < p[r]:
                pft = p[r]-p[l]
                res=max(pft, res)
            else:
                l=r
            r+=1
        return res 
