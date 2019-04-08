```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        result = []
        
        for num in range(numRows):
            result.append([])    
        
        res = ""
        
        difference = numRows - 2
        
        pointer = 0
        i = 0
        
        while i in range(len(s)):
        
            result[pointer].append(s[i])
            i += 1
            pointer += 1
                        
            while pointer < numRows:
                if i < len(s):
                    result[pointer].append(s[i])
                else:
                    break
                pointer += 1
                i += 1    
                
                
            while difference >= 1:
                if i < len(s):
                    result[difference].append(s[i])
                else:
                    break
                difference -= 1
                i += 1
                
            pointer = 0
            difference = numRows - 2
            
        for ls in result:
            res += ''.join(ls)
        return res
```
