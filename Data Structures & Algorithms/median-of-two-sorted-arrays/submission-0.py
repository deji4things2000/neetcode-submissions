class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m+n
        half = total//2

        i, j = 0, m

        while i<=j:
            p1 = (i+j)//2
            p2 = half - p1

            max1_i = nums1[p1-1] if p1 > 0 else float('-inf')
            min1_j = nums1[p1] if p1 < m else float('inf')

            max2_i = nums2[p2-1] if p2 > 0 else float('-inf')
            min2_j = nums2[p2] if p2 < n else float('inf')

            if max1_i <= min2_j and max2_i <= min1_j:
                if total%2 == 0:
                    return (max(max1_i, max2_i) + min(min1_j, min2_j)) /2
                else:
                    return min(min1_j, min2_j)

            elif max1_i > min2_j:
                j = p1 - 1
            else:
                i = p1 + 1


