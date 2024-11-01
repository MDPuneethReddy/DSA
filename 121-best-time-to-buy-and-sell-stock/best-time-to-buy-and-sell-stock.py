class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        if len(prices)==1:
            return 0
        l=0
        r=1
        while(r<len(prices)):
            if prices[l]>=prices[r]:
                l=r
                r+=1
            else:
                maxi=max(maxi,prices[r]-prices[l])
                r+=1
        return maxi

        