class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pro = 0

        for i in range(n):
            j=i+1
            while j<n:
                diff = prices[j] - prices[i]
                pro = max(pro, diff)
                j+=1
        return pro
