class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        cur = -1

        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = cur
            cur = max(temp, cur)
        return arr