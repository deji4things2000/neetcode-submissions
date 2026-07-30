class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)

        while i<=j:
            mid = (i+j)//2
            hour = 0
            
            for p in piles:
                hour += math.ceil(p/mid)
            
            if hour > h:
                i =  mid + 1
            else:
                j = mid - 1
        return i
                