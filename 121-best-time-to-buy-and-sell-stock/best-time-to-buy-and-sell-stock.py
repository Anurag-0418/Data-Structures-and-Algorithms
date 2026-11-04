class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        current_price = sys.maxsize
        for i in prices:
            max_profit = max(max_profit, i - current_price)
            current_price = min(current_price, i)
        return max_profit           


        