class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count<=0:
                count=1
                res=nums[i]
            else:

                if nums[i]!=res:
                    count-=1
                else:
                    count+=1
        return res
            
        