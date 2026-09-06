class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 1, x

        while i<=j:
            mid = (i+j)//2

            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                i = mid + 1
            else:
                j = mid - 1
        return j
        