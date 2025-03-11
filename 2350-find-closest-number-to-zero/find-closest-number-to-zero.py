class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dif=math.inf
        val=nums[0]
        for i in range(len(nums)):
            d=abs(nums[i]-0)
            if d<dif:
                val=nums[i]
                dif=d
            elif d==dif:
                if nums[i]>val:
                    val=nums[i]
        return val
        