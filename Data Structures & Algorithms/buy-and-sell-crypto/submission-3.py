class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        n= len(prices)

        for i in range(n):
            j=i+1
            while j<n:
                ip = prices[j] - prices[i]
                pro=max(pro, ip)
                j+=1
        return pro
