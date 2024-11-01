class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=prices[len(prices)-1]
        value=0
        for i in range(len(prices)-2,-1,-1):
            if maxi-prices[i]>0:
                value=max(value,abs(prices[i]-maxi))
            maxi=max(maxi,prices[i])
        return value

        