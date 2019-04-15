```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        max_sum = max_so_far = nums[i]
        i += 1
        
        while i < len(nums):
            max_sum = max(nums[i], max_sum + nums[i])
            max_so_far = max(max_so_far, max_sum)
            i += 1
        
        return max_so_far
```
