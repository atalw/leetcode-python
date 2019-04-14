```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        i = 0
        
        for j in range(0, len(nums)):
            if nums[j] == val:
                count -= 1
            else:
                nums[i] = nums[j]
                i += 1
        
        return count
```
