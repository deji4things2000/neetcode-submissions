class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 0, num


        while lo<=hi:
            mid = (lo+hi)//2
            sq = mid * mid

            if sq==num:
                return True
            elif sq<num:
                lo=mid+1
            else:
                hi = mid - 1
        return False


        