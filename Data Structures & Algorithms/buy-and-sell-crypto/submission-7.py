class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = start + 1

        maxProfit = 0

        while end<len(prices):
            profit = prices[end] - prices[start]
            # print(start, end, prices[start], prices[end], profit)
            if profit < 0:
                start = end
            end = end + 1
            maxProfit = max(maxProfit,profit)
            # print(profit)

        return maxProfit