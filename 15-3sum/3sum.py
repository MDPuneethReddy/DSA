class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates
            x = i + 1
            j = len(nums) - 1
            while x < j:
                total_sum = nums[i] + nums[x] + nums[j]
                if total_sum == 0:
                    result.append([nums[i], nums[x], nums[j]])
                    while x < j and nums[x] == nums[x + 1]:
                        x += 1  # Skip duplicates
                    while x < j and nums[j] == nums[j - 1]:
                        j -= 1  # Skip duplicates
                    x += 1
                    j -= 1
                elif total_sum < 0:
                    x += 1
                else:
                    j -= 1
        return result



                    
                    
            