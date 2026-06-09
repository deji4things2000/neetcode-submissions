class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        prof = prices[0]
        val = 0
        
        for i in range(1, n):
            diff = prices[i]-prices[i-1]
            if diff>0:
                val+=diff
        return val

        