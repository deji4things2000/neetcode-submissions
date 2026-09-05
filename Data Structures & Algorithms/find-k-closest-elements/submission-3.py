class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n-1

        while (right-left+1) > k:
            a = arr[left]
            b = arr[right]

            if abs(a-x) <= abs(b-x) and a<b:
                right-=1
            else:
                left+=1
        return arr[left:right+1]

        