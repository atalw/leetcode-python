```
class Solution:
    def reverse(self, x: int) -> int:
        max_range = 2**31-1
        min_range = -max_range

        if x == 0 or x < min_range or x > max_range:
            return 0
        
        num_string = str(x)
        num_string = num_string[::-1]
        
        res_string = ""
        digit_found = False
        
        
        for char in num_string:
            if char == '-':
                res_string = '-' + res_string
                continue
            if (char == '0' and not digit_found):
                continue
            else:
                res_string += char
                digit_found = True
                
        result_int = int(res_string)
        
        if result_int < min_range or result_int > max_range:
            return 0
        
        return result_int
```
