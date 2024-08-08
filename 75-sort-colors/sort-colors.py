class Solution:
    def sortColors(self, nums: List[int]) -> None:
        changes=False
        while(1):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    temp=nums[i]
                    nums[i]=nums[i-1]
                    nums[i-1]=temp
                    changes=True
            if changes==False:
                return
            else:
                changes=False
        