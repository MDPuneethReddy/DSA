class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        maxprofit=0
        while(i<len(prices) and j<len(prices)):
            if prices[i]>=prices[j]:
                i=j
            
            else:
                maxprofit=max(maxprofit,prices[j]-prices[i])
            j+=1
        return maxprofit

        