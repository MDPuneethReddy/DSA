class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        zeroCount=0
        maxLength=0
        count=0
        while(r<len(nums) and l<len(nums)):
            if nums[r]==1:
                count+=1
            else:
                zeroCount+=1
                count+=1
            r+=1
            if zeroCount>k:
                if nums[l]==0:
                    zeroCount-=1
                l+=1
                count-=1
            if zeroCount<=k:
                    maxLength=max(maxLength,count)
        return maxLength
            

        