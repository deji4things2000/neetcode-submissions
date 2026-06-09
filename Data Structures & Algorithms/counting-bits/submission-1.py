from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits(n):
            count = 0
            while n:
                n&= n-1
                count+=1
            return count
        
        res = []
        for i in range(n+1):
            res.append(count_bits(i))
        return res
