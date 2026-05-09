from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price,price)
            if price>min_price:
                max_profit = max(price-min_price,max_profit)
        return max_profit


if __name__ == "__main__":
    # prices = [7,1,5,3,6,4]
    prices = [7, 6, 4, 3, 1]
    sol = Solution()
    print(sol.maxProfit(prices))