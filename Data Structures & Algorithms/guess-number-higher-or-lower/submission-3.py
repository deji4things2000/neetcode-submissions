class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n

        while i <= j:  # ← Fixed: use <=
            mid = (i + j) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == 1:
                i = mid + 1
            else:  # res == 1 (guess is lower than the picked number)
                j = mid - 1
        