class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        # Start with full array as window
        left = 0
        right = n - 1
        
        # Shrink until window size = k
        while (right - left + 1) > k:
            if abs(x - arr[left]) <= abs(x - arr[right]):
                right -= 1  # Remove from right
            else:
                left += 1   # Remove from left
        
        return arr[left:right+1]