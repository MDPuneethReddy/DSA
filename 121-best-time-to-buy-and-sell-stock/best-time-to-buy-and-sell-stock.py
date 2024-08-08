class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=-math.inf
        maxprof=[0]*len(prices)
        for i in range(len(prices)):
            maxi=max(maxi,prices[len(prices)-i-1])
            maxprof[len(prices)-i-1]=maxi
        profit=0
        for i in range(len(prices)):
            profit=max(profit,maxprof[i]-prices[i])
        return profit

        