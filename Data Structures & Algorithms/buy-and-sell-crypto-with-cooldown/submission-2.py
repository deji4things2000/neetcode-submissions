class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, n):
            new_hold = max(hold, rest-prices[i])
            new_sold = hold + prices[i]
            new_rest = max(rest, sold)

            hold, sold, rest = new_hold, new_sold, new_rest
        return max(hold, sold, rest)