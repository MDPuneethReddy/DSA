class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # I solved in o(nlogn)
        # nums.sort()
        # count=0
        # if len(nums)==0:
        #     return 0
        # elif len(nums)==1:
        #     return 1
        # else:
        #     v=1
        #     for i in range(1,len(nums)):
        #         if (nums[i]-nums[i-1])==1:
        #             v+=1
        #         elif (nums[i]-nums[i-1])==0:
        #             continue
        #         else:
        #             count=max(v,count)
        #             v=1
        #     count=max(v,count)
        # return count
        setValues=set(nums)
        print(setValues)
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


        