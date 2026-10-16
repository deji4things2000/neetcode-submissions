class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        left = 0
        n = len(prices)

        for right in range(1, n):
            if prices[left] >= prices[right]:
                left = right
            else:
                diff = prices[right] - prices[left]
                maxi = max(maxi, diff)
        return maxi



        