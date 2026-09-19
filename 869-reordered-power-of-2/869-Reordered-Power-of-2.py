class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter

        target_count = Counter(str(n))

        for i in range(30):
            if Counter(str(1<<i)) == target_count:
                return True
        
        return False
