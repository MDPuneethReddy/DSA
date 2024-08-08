class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[i]>0:
        #         nums=nums[i:]
        #         break
        # print(nums)
        # if len(nums)==0:
        #     return max(nums)
        s=0
        maxi=float(-inf)
        for i in range(len(nums)):
            s+=nums[i]
            maxi=max(maxi,s)
            if s<=0:
                s=0
            
        return maxi

        