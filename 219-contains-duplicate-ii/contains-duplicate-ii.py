class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # time complexity - O(n)
        # space complexity - O(n)
        # save the values in dictionary and check get the difference between the present and already saved index else just update the dictionary
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

        