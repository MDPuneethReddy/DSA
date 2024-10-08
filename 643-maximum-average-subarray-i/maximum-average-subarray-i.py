class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s+=nums[i]
        maxi=s/k
        for i in range(k,len(nums)):
            s+=nums[i]
            s-=nums[i-k]
            maxi=max(maxi,s/k)
        return maxi        