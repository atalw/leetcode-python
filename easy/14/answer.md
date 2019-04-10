```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substring = ""
        
        results = []
        
        if len(strs) == 0:
            return ""
        min_length = len(min(strs))
        
        for i in range(min_length):
                        
            if i <= len(strs[0])-1:
                substring += strs[0][i]
            else:
                break
                        
            if len(strs) == 1:
                results.append(substring)
            else:
                for string in strs[1:]:

                    if i < len(string):
                        if substring[len(substring)-1] == string[i]:
                            continue
                        else:
                            # print(substring)
                            results.append(substring[:len(substring)-1])
                            substring = ""
                            return max(results) if len(results) != 0 else ""

                    else:
                        return max(results) if len(results) != 0 else ""
                        
                results.append(substring)
                                
        return max(results) if len(results) != 0 else ""

                    
```
