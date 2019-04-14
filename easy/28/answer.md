```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(needle) == 1:
                    return i
                if i+len(needle) <= len(haystack):
                    for j in range(1, len(needle)):
                        if haystack[i+j] != needle[j]:
                            break
                        else:
                            if j == len(needle)-1:
                                return i
                else:
                    return -1
                        
        return -1
```
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```
