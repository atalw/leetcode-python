```
import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = re.findall("\S+", s)
        if len(words) >= 2:
            return len(words[-1])
        else:
            if len(words) == 0:
                return 0
            else:
                return len(words[0])
```
