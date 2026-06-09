class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        n=len(arr)

        for i in range(n-1, -1, -1):
            cur = arr[i]
            arr[i] = maxi
            maxi = max(cur, maxi)
        return arr