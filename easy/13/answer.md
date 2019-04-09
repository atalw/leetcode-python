```
class Solution:
    def romanToInt(self, s: str) -> int:
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        numerals = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        
        res = 0
        i = 0
        while i < len(s):
            
            if i == len(s)-1:
                index = numerals.index(s[i])
                res += values[index]
                break
                            
            first = s[i]
            second = s[i+1]
            index_first = numerals.index(first)
            index_second = numerals.index(second)
            
            
            if values[index_first] < values[index_second]:
                res += values[index_second-1]
                i += 2
            else:
                i += 1
                res += values[index_first]
                
        return res
            
```
