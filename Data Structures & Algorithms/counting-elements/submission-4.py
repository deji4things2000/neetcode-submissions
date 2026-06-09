class Solution:
    def countElements(self, arr: List[int]) -> int:
        hm = set(arr)
        cnt = 0

        for a in arr:
            if a+1 not in hm:
                cnt+=0
            else:
                cnt+=1

        return cnt

