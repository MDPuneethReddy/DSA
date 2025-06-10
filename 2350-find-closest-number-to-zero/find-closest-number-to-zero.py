class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        #time complexity -o(n)
        #space complexity - o(1)
        closetLargestNumsValue=nums[0]
        closestValue=abs(nums[0])
        for i in range(1,len(nums)):
            if abs(nums[i])<closestValue:
                closetLargestNumsValue=nums[i]
                closestValue=abs(nums[i])
            elif abs(nums[i])==closestValue:
                if nums[i]>closetLargestNumsValue:
                    closetLargestNumsValue=nums[i]
        return closetLargestNumsValue


        