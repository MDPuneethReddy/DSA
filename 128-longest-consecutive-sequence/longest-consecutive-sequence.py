class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        else:
            v=1
            for i in range(1,len(nums)):
                if (nums[i]-nums[i-1])==1:
                    v+=1
                elif (nums[i]-nums[i-1])==0:
                    continue
                else:
                    count=max(v,count)
                    v=1
            count=max(v,count)
        return count

        