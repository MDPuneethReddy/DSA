class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maxi=-math.inf
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            s+=nums[i]
            maxi=max(maxi,s)
            if s<=0:
                s=0
        return maxi
            

        