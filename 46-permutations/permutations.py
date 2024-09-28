class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mainList=[]
        def recurr(nums,visited,values,length):
            if length==(len(nums)):
                mainList.append(values.copy())
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.append(i)
                    values.append(nums[i])
                    recurr(nums,visited,values,length+1)
                    visited.pop()
                    values.pop()
            return
        recurr(nums,[],[],0)
        return mainList