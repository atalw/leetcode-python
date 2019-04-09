```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # one pointer traveses from front
        # another pointer traveses from back
        # max height of the two is considered and distance is base
        
        p_one = 0
        p_two = len(height)-1
        max_area = 0
        
        while p_one < p_two:
            
            height_one = height[p_one]
            height_two = height[p_two]
                
            base = p_two - p_one
                
            area = min(height_one, height_two)*base
                    
            if area > max_area:
                max_area = area
                
            if height_one < height_two:
                p_one += 1
            else:
                p_two -= 1
                    
        return max_area

```
