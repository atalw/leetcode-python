```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        
        pointer = len(string)-1
        
        for i in range(len(string)//2):
            if string[i] != string[pointer]:
                return False
            else:
                pointer -= 1
                continue
        
        return True
```

```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reversed_x = 0
        while x > 0:
            reversed_x = (10*reversed_x) + x%10
            x //= 10
        
        if reversed_x == num:
            return True
        else:
            return False

```
