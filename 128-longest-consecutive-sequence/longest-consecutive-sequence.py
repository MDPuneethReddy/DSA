class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #tiime complexity - o(n) space- o(n)
        setValues=set(nums)
        count=0
        for i in range(len(nums)):
            v=1
            if nums[i]-1 not in setValues:
                j=1
                while(1):
                    # print(nums[j]+j)
                    if nums[i]+j in setValues:
                        j+=1
                    else:
                        break
                count=max(count,j)
        return count


        