class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cost_price_candidate = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < cost_price_candidate:
                cost_price_candidate = prices[i]
            else:
                profit = max(profit, prices[i]-cost_price_candidate)
        return profit