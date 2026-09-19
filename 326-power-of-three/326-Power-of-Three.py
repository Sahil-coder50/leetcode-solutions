class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        base=3
        if n<=0 or base<2:
            return False
        if n==1:
            return True

        INT_MAX = (1<<31)-1

        import math

        max_comp = int(math.log(INT_MAX) / math.log(base))
        max_power = base ** max_comp

        return max_power % n == 0