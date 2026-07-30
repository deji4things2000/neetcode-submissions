class Solution:
    def mySqrt(self, x: int) -> int:
        i,j = 0, x

        while i<=j:
            mid = (i+j)//2
            res = mid * mid

            if res == x:
                return mid
            elif res < x:
                i = mid + 1
            else:
                j = mid - 1
        return j
        