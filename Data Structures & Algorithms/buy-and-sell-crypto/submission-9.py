class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        left = 0
        maxi = 0

        for right in range(1, n):
            if prices[right] < prices[left]:
                left=right
            else:
                diff = prices[right] - prices[left]
                maxi = max(maxi, diff)
        return maxi
        