class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = 0
        left = 0
        for right in range(1, n):
            if prices[right] < prices[left]:
                left = right
            else:
                diff = prices[right] - prices[left]
                maxi = max(maxi, diff)
        return maxi

        