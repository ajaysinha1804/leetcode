class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right = 0 ,1 #left =buy right = sell
        maxprofit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(profit , maxprofit) 
            else:
                left =right
            right +=1 
        return maxprofit              
                