```
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(x) = f(x-1) + f(x-2)
        available_steps = [1,2]
        cache = [0 for _ in range(n + 1)]
        cache[0] = 1
        for i in range(n + 1):
            cache[i] += sum(cache[i - x] for x in available_steps if i - x > 0)
            cache[i] += 1 if i in available_steps else 0
        return cache[-1]
```
