class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #time- o(n), space-o(1)
        if len(nums)==0:
            return []
        start=nums[0]
        end=nums[0]
        mainValues=[]
        for i in range(1,len(nums)):
            if nums[i]-end==1:
                end=nums[i]
            else:
                if start==end:
                    mainValues.append(str(start))
                else:
                    mainValues.append(f'{str(start)}->{str(end)}')
                start=nums[i]
                end=nums[i]
        if start==end:
            mainValues.append(str(start))
        else:
            mainValues.append(f'{str(start)}->{str(end)}')
        return mainValues
        

        