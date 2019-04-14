```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = len(nums)-1
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                count -= 1
            else: 
                i += 1        
                nums[i] = nums[j]
            j += 1
        return count+1
```

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1
```
