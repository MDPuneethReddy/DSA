class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                v=d[nums[i]]
                if(abs(i-v))<=k:
                    return True
                else:
                    d[nums[i]]=i
        return False

        