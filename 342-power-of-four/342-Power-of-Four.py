class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        base = 4
        if n<=0 or (n & (n-1)) !=0:
            return False

        return (n-1) % (base-1) == 0