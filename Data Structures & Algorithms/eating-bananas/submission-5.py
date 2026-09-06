class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        i, j = 1, max(piles)


        while i<=j:
            mid = (i+j)//2
            k = 0

            for pile in piles:
                k+=math.ceil(pile/mid)
            
            if h < k:
                i = mid + 1
            else:
                j = mid - 1

        return i

            

        