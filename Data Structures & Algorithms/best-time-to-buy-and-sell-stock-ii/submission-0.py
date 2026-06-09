class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for today, tomorrow in zip(prices, prices[1:]):
            if tomorrow > today:
                profit+=tomorrow-today
        return profit


        