class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        profit = 0
        for i in range(len(prices)-1):
            j = i+1
            cost_price = prices[i]
            max_selling_price = 0
            while j < len(prices):
                if prices[j] >= cost_price and prices[j] > max_selling_price:
                    max_selling_price = prices[j]
                j += 1
            profit = max(profit, max_selling_price-cost_price)

        return profit