class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #time complexity- 0(n), space complexity-o(n)
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return [i,d[nums[i]]]
            d[target-nums[i]]=i
        
        #withoutspace complexity then we can sort it use left and right to find the solutiuon. the time is o(nlogn)


        