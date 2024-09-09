class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        maxi=prices[l-1]
        value=0
        for i in range(l):
            v=prices[l-i-1]
            if v<maxi:
                value=max(value,maxi-v)
            maxi=max(maxi,v)

        return value

        