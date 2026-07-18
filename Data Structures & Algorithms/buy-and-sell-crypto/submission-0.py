class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf= 1000
        tmp= inf 
        profit= 0

        for coin in prices:
            profit= max(profit, coin-tmp)
            tmp= min(tmp, coin)

        return profit