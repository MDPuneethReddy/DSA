class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=prices[len(prices)-1]
        value=0
        for i in range(len(prices)):
            if prices[len(prices)-i-1]<maxi:
                value=max(value,maxi-prices[len(prices)-i-1])
            maxi=max(maxi,prices[len(prices)-i-1])

        return value

        