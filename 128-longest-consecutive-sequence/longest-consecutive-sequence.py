class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq=set()
        for i in nums:
            uniq.add(i)
        maxcount=1
        for i in range(len(nums)):
            if nums[i]-1 not in uniq:
                v=1
                inc=0
                while(True):
                    if nums[i]+inc in uniq:
                        
                        inc+=1
                        v+=1
                    else:
                        break
                maxcount=max(maxcount,v)
        return maxcount-1

        