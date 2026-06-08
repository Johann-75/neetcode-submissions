class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,len(prices)-1
        max_profit = 0

        while buy<sell:
            profit = prices[sell] - prices[buy]
            print(prices[buy], prices[sell]," " , profit)
            if profit>max_profit:
                max_profit = profit

            if sell == buy+1:
                buy+=1
                sell=len(prices)-1
            else:
                sell-=1
                
        return max_profit    