class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x

        while lo<=hi:
            mid = (lo+hi) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            elif sqr< x:
                lo = mid+1
            else:
                hi = mid-1
        return hi