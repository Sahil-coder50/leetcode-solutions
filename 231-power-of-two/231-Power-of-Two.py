class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0 or (n & (n-1)) !=0:
            return False

        base=2

        return (n-1) % (base-1) == 0